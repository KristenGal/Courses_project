from django.urls import path
from .api_views import CourseListAPI, CourseCreateAPI, BucketListAPI

urlpatterns = [
    path("courses/", CourseListAPI.as_view(), name="api_courses"),
    path("courses/create/", CourseCreateAPI.as_view(), name="api_course_create"),
    path("buckets/", BucketListAPI.as_view(), name="api_buckets"),
]