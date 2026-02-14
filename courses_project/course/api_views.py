from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from ninja import NinjaAPI
from ninja.security import django_auth
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Bucket, Category
from .serializer import CourseSerializer, BucketSerializer

from user.models import CustomUser

from .shemas import CourseOut, CourseIn



class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BucketListAPI(generics.ListAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class CourseCreateAPI(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


api_ninja = NinjaAPI()


@api_ninja.get("/", response=list[CourseOut])
def list_courses(request):
    return Course.objects.all()


@api_ninja.get("/{course_id}", response=CourseOut)
def get_course(request, course_id: int):
    return get_object_or_404(Course, id=course_id)


@api_ninja.post("/", response=CourseOut, auth=django_auth)
def create_course(request, data: CourseIn):
    category = get_object_or_404(Category, id=data.category_id)

    course = Course.objects.create(
        title=data.title,
        description=data.description,
        price=data.price,
        duration=data.duration,
        rate=data.rate,
        category=category,
        teacher=request.user,
    )
    return course


@api_ninja.put("/{course_id}", response=CourseOut, auth=django_auth)
@csrf_exempt
def update_course(request, course_id: int, data: CourseIn):
    course = get_object_or_404(Course, id=course_id)

    for field, value in data.dict().items():
        if field != "category_id":
            setattr(course, field, value)

    course.save()
    return course


@api_ninja.delete("/{course_id}", auth=django_auth)
@csrf_exempt
def delete_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return {"success": True}