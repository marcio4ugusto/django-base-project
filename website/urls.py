from django.urls import path, include
from website.views import landing, features


urlpatterns = [
    path('', landing, name="landing"),
    path('features/', features, name="features"),
]
