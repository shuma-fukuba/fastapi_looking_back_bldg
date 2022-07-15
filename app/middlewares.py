from utils.logger import get_logger
import env
from fastapi import Request

logger = get_logger(__name__)


async def http_log(request: Request, call_next):
    logger.info(
        'START - %s %s from %s',
        request.method,
        request.url.path,
        request.client.host)
    if env.APP_ENV == 'development':
        message = f'\n** before *****************************************: {request.url.path}\n'
        message += f'   [request]request_uri={request.url}\n'
        message += f'   [httpMethod]{request.method}\n'
        message += f'   [clientIp]ip={request.client.host}\n'
        for header_name in request.headers:
            header_val = request.headers[header_name]
            message += f'   [header]{header_name}={header_val}\n'
        logger.debug(message)
    response = await call_next(request)
    if env.APP_ENV == 'development':
        message = f'\n** after *****************************************: {request.url.path}\n'
        message += f'   [status]{response.status_code}\n'
        for header_name in response.headers:
            header_val = response.headers[header_name]
            message += f'   [headers]{header_name}={header_val}\n'
        logger.debug(message)
    logger.info('END - statusCode is $d', response.status_code)
    return response
