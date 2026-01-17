from django.contrib import admin
from .models import Course, Category, Bucket

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'teacher',
    )
    list_editable = (
        'title',
        'price',
        'teacher',
    )
    list_filter = (
        'level',
        'category',
        'price',
        'teacher',
    )
    ordering = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_editable = (
        'title',
    )
    ordering = ('id',)


@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'course',
        'status',
    )
    list_filter = (
        'status',
        'user',
        'course',
    )
    list_editable = (
        'status',
    )
    ordering = ('id',)
