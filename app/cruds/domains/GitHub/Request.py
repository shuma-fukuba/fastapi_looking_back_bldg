from modules.http.Request import Request as BaseRequest


class Request(BaseRequest):
    _PREFIX = 'https://github-contributions-api.deno.dev'
    _SUFFIX = '.json'
