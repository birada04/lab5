from django.urls import path
from .apiviews import PublicPostList

urlpatterns = [
    path("api/public/", PublicPostList.as_view(), name="api_public"),
]
