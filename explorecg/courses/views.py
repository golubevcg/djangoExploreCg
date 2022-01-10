from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from courses.models import Article
from users.models import ECGUser


def courses_list(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'courses/courses_list.html', context=context)


# def course_detail(request, pk):
#     course = get_object_or_404(Article, pk=pk)
#     context = {
#         "course": course
#     }
#
#     return render(request, 'courses/article_detail.html', context)


def users_list(request):
    context = {
        'users': ECGUser.objects.all()
    }
    return render(request, 'courses/users_list.html', context=context)


class ArticleDetailView(DetailView):
    model = Article
    # template_name = 'courses/article_detail.html'
    context_object_name = 'course'
