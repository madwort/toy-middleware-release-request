from toy_middleware_release_request.business_logic import ReleaseRequest

class ViewKwargsUpgrade:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        # this would be request.user in airlock
        user = "tom"

        if 'release_request' in view_kwargs:
            release_request = ReleaseRequest.load(user, view_kwargs['release_request'])
            view_kwargs['release_request'] = release_request

        return view_func(request=request, *view_args, **view_kwargs)
