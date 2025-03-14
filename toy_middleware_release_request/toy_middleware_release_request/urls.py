"""
URL configuration for toy_middleware_release_request project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import toy_middleware_release_request.views.request

urlpatterns = [
    path('request/view/<str:release_request_id>', toy_middleware_release_request.views.request_view),
    path('request/add/<str:release_request_id>/<str:group>/<path:urlpath>', toy_middleware_release_request.views.request_add),
    path('request/edit/<str:release_request_id>/<path:request_urlpath>', toy_middleware_release_request.views.request_edit),
    path('request/remove/<str:release_request_id>', toy_middleware_release_request.views.request_remove),
    path('admin/', admin.site.urls),
]
