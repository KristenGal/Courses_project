from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import CourseForm, CategoryForm
from .models import Course, Category, Bucket
from .filters import CourseFilter

# Create your views here.

@login_required
def add_course_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('course:list_courses')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})


def list_courses_view(request):
    courses = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=courses)
    courses = course_filter.qs.order_by('id')
    paginator = Paginator(courses, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    elided_page_range = paginator.get_elided_page_range( # type: ignore
        number=page_obj.number,
        on_each_side=2,
        on_ends=1
    )
    return render(request, 'course/list_courses.html', {'courses': page_obj, 'elided_page_range': elided_page_range})


@login_required
def add_category_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:list_categories')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})


def list_categories_view(request):
    categories = Category.objects.all()
    return render(request, 'category/list_categories.html', {'categories': categories})


@login_required
def course_detail_view(request, course_id):
    course = Course.objects.get(id=course_id)
    bucket = Bucket.objects.filter(user=request.user, course=course).first()
    status = bucket.status if bucket else None
    return render(request, 'course/course_detail.html', {'course': course, 'status': status})


@login_required
def add_to_bucket(request, course_id):
    course = Course.objects.get(id=course_id)
    bucket_item, created = Bucket.objects.get_or_create(user=request.user, course=course)
    bucket_item.status = Bucket.Status.IN_BUCKET
    bucket_item.save()
    return redirect('course:bucket')


@login_required
def add_to_wishlist(request, course_id):
    course = Course.objects.get(id=course_id)
    bucket_item, created = Bucket.objects.get_or_create(user=request.user, course=course)
    bucket_item.status = Bucket.Status.WISHLISTED
    bucket_item.save()
    return redirect('course:wishlist')


@login_required
def delete_from_bucket(request, course_id):
    bucket_item = Bucket.objects.filter(user=request.user, course__id=course_id).first()
    if bucket_item:
        bucket_item.delete()
    return redirect('course:list_courses')


@login_required
def bucket_view(request):
    courses = Bucket.objects.filter(user=request.user, status=Bucket.Status.IN_BUCKET).select_related('course')
    return render(request, 'course/bucket.html', {'courses': courses})


@login_required
def wishlist_view(request):
    courses = Bucket.objects.filter(user=request.user, status=Bucket.Status.WISHLISTED).select_related('course')
    return render(request, 'course/wishlist.html', {'courses': courses})


@login_required
def purchase_history_view(request):
    courses = Bucket.objects.filter(user=request.user, status=Bucket.Status.BOUGHT).select_related('course')
    return render(request, 'course/history.html', {'courses': courses})
