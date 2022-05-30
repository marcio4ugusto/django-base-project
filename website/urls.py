from django.urls import path, include
from website.views import landing, blank


urlpatterns = [
    path('', landing, name="landing"),
    path('blank/', blank, name="blank"),
]
