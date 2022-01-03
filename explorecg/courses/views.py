from django.shortcuts import render

from courses.models import Article


def courses_list(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'courses/courses_list.html', context=context)