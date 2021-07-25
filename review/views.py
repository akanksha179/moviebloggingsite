from django.shortcuts import render
from .models import Review, Genre, Knowledge, Cast


def function():
    pass


# Create your views here.
def review(request, get_id):
    data = Review.objects.get(id=get_id)
    context = {
        'heading': 'Review',
        'review': data,
        'cast': data.cast.all(),
        'baseUrl': request.build_absolute_uri('/')
    }
    return render(request, 'review/review.html', context)


def home(request):
    top_featured, featured_1, featured_2 = Review.objects.all().order_by('id').reverse()[:3]
    context = {
        'top_featured': top_featured,
        'featured_1': featured_1,
        'featured_2': featured_2,
        'baseUrl': request.build_absolute_uri('/')
    }
    return render(request, 'review/home.html', context)


def tos(request):
    return render(request, 'review/tos.html', {'heading': 'Terms of Service'})


def privacy(request):
    return render(request, 'review/privacy.html', {'heading': 'Privacy Policy'})


def knowledge(request):
    context = {
        'heading': 'Knowledge Section',
        'paragraphs': Knowledge.objects.all().reverse()
    }
    return render(request, 'review/knowledge.html', context)


def about(request):
    return render(request, 'review/about.html', {'heading': 'About Us'})


def cast(request, get_id):
    cast_data = Cast.objects.get(id=get_id)
    context = {
        'heading': 'Cast Details',
        'cast': cast_data,
        'baseUrl': request.build_absolute_uri('/')
    }
    return render(request, 'review/cast.html', context)


def filter_page(request, genre_var):
    if genre_var == 1:
        post = Review.objects.all()
    else:
        post = Review.objects.filter(genre=genre_var)
    context = {
        'heading': str(Genre.objects.filter(id=genre_var)[0]) + ' Reviews',
        'posts': post,
        'baseUrl': request.build_absolute_uri('/')
    }
    return render(request, 'review/filter.html', context)


def weekly_recommend(request):
    context = {
        'heading': 'Weekly Recommendations',
        'posts': Review.objects.filter(weekly_recommendation=True),
        'baseUrl': request.build_absolute_uri('/')
    }
    return render(request, 'review/weekly.html', context)
