from django.urls import path
from django.views.generic import TemplateView

import courses.views as courses

app_name = 'courses'

urlpatterns = [
    path('',
         courses.courses_list,
         name='index'),
    path('course/detail/<int:pk>',
         # courses.course_detail,
         courses.ArticleDetailView.as_view(),
         name='course_detail'),
    path('users/',
         courses.users_list,
         name='users'),
    path('about/',
         TemplateView.as_view(template_name='courses/about.html'),
         name='about'),
]
