from django.urls import path
from .views import (
    add_course_view, 
    list_courses_view, 
    add_category_view, 
    list_categories_view, 
    course_detail_view, 
    add_to_bucket, 
    bucket_view, 
    delete_from_bucket,
    add_to_wishlist,
    wishlist_view,
    purchase_history_view
)


app_name = 'course'

urlpatterns = [
    path('add-course/', add_course_view, name='add_course'),
    path('list/', list_courses_view, name='list_courses'),
    path('add-category/', add_category_view, name='add_category'),
    path('categories/', list_categories_view, name='list_categories'),
    path('list/<int:course_id>/', course_detail_view, name='course_detail'),
    path('add-to-bucket/<int:course_id>/', add_to_bucket, name='add_to_bucket'),
    path('delete-from-bucket/<int:course_id>/', delete_from_bucket, name='delete_from_bucket'),
    path('bucket/', bucket_view, name='bucket'),
    path('add-to-wishlist/<int:course_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('history/', purchase_history_view, name='history'),
]