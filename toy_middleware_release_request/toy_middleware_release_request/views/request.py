from django.template.response import TemplateResponse

from toy_middleware_release_request.business_logic import ReleaseRequest

def request_view(request, release_request_id: str):
    assert isinstance(release_request_id, str), "bad type"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)

def request_edit(request, release_request_id: str):
    user = "nottom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)

def request_remove(request, release_request_id: str):
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)
