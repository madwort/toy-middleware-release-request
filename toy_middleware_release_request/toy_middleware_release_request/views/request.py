from django.template.response import TemplateResponse

from toy_middleware_release_request.business_logic import ReleaseRequest, UrlPath, RequestUrlPath

def request_view(request, release_request_id: str):
    assert isinstance(release_request_id, str), "bad type"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)

def request_add(request, release_request_id: str, group: str, urlpath: UrlPath):
    assert isinstance(urlpath, UrlPath), "bad type"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request_add.html"
    context = { "release_request": release_request, "group": group, "urlpath": urlpath }
    return TemplateResponse(request, template, context)

def request_edit(request, release_request_id: str, request_urlpath: RequestUrlPath):
    assert isinstance(request_urlpath, RequestUrlPath), f"bad type {request_urlpath.__class__}"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    group = request_urlpath.group
    urlpath = request_urlpath.urlpath

    template = "request_edit.html"
    context = { "release_request": release_request, "group": group, "urlpath": urlpath, "request_urlpath": request_urlpath }
    return TemplateResponse(request, template, context)

def request_remove(request, release_request_id: str):
    user = "nottom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)
