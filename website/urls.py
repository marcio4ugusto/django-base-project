from django.urls import path, include
from website.views import default, app


urlpatterns = [
    path('', default, name="default"),
    path('app/', app, name="app"),
]
