from toy_middleware_release_request.business_logic import ReleaseRequest, UrlPath, RequestUrlPath

class ViewKwargsUpgrade:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        # this would be request.user in airlock
        user = "tom"

        # TODO: if we had a consistent interface on these classes, we could just
        # iterate over view_kwargs with an allowed list of convertible kwargs
        if 'urlpath' in view_kwargs:
            urlpath = UrlPath(view_kwargs['urlpath'])
            view_kwargs['urlpath'] = urlpath

        if 'request_urlpath' in view_kwargs:
            request_urlpath = RequestUrlPath.load(view_kwargs['request_urlpath'])
            view_kwargs['request_urlpath'] = request_urlpath

        return view_func(request=request, *view_args, **view_kwargs)
