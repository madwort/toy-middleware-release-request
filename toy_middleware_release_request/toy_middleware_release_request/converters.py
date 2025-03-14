from toy_middleware_release_request.business_logic import ReleaseRequest, UrlPath, RequestUrlPath

class UrlPathConverter:
    regex = ".*"

    def to_python(self, value):
        return UrlPath(value)

    def to_url(self, value):
        return value

class RequestUrlPathConverter:
    regex = ".*"

    def to_python(self, value):
        return RequestUrlPath.load(value)

    def to_url(self, value):
        return value
