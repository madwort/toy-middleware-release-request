from django.template.response import TemplateResponse

from toy_middleware_release_request.business_logic import ReleaseRequest, UrlPath

def request_view(request, release_request_id: str):
    assert isinstance(release_request_id, str), "bad type"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)

def request_add(request, release_request_id: str, group: str, urlpath: str):
    assert isinstance(urlpath, str), "bad type"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    relpath = UrlPath(urlpath)

    template = "request_add.html"
    context = { "release_request": release_request, "group": group, "urlpath": relpath }
    return TemplateResponse(request, template, context)

def request_edit(request, release_request_id: str, urlpath: str):
    assert isinstance(urlpath, str), "bad type"
    user = "tom"
    release_request = ReleaseRequest.load(user, release_request_id)

    request_urlpath = UrlPath(urlpath)
    group = request_urlpath.parts[0]
    urlpath = UrlPath(*request_urlpath.parts[1:])

    template = "request_edit.html"
    context = { "release_request": release_request, "group": group, "urlpath": urlpath, "request_urlpath": request_urlpath }
    return TemplateResponse(request, template, context)

def request_remove(request, release_request_id: str):
    user = "nottom"
    release_request = ReleaseRequest.load(user, release_request_id)

    template = "request.html"
    context = { "release_request": release_request }
    return TemplateResponse(request, template, context)
