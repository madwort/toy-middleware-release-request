from dataclasses import dataclass
from django.http import Http404

from pathlib import Path, PurePosixPath

@dataclass
class ReleaseRequest:
    id: str
    name: str

    @classmethod
    def load(cls, user, id):
        if id == "123456" and user == "tom":
            return cls(id=id, name="My demo release request")
        elif id == "987654" and user == "bob":
            return cls(id=id, name="My other demo release request")
        else:
            raise Http404()

    def __str__():
        return f"{id}"


UrlPath = PurePosixPath

@dataclass
class RequestUrlPath:
    group: str
    urlpath: UrlPath

    @classmethod
    def load(cls, request_urlpath):
        path = PurePosixPath(request_urlpath)
        group = path.parts[0]
        urlpath = UrlPath(*path.parts[1:])
        return cls(group=group, urlpath=urlpath)


    def __str__(self):
        return f"group: {self.group} path: {self.urlpath}"
