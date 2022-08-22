from cruds.http.Request import Request


class GitHub:
    @classmethod
    def read_grass(cls, github_username):
        return Request.get(github_username)
