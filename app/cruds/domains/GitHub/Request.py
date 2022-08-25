from env import GITHUB_ACCESS_TOKEN
from modules.http.Request import Request as BaseRequest


class Request(BaseRequest):
    HEADERS = {'content-type': 'application/json',
               'Authorization': f'Bearer {GITHUB_ACCESS_TOKEN}'}
    _PREFIX = 'https://github-contributions-api.deno.dev'
    _SUFFIX = '.json'
