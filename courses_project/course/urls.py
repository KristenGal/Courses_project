from django.urls import path
from .views import add_course_view, list_courses_view, add_category_view, list_categories_view, course_detail_view


app_name = 'course'

urlpatterns = [
    path('add-course/', add_course_view, name='add_course'),
    path('list/', list_courses_view, name='list_courses'),
    path('add-category/', add_category_view, name='add_category'),
    path('categories/', list_categories_view, name='list_categories'),
    path('list/<int:course_id>/', course_detail_view, name='course_detail'),
]