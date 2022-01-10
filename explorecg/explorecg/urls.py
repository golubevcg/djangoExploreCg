from django.contrib import admin
from django.urls import path, include
import courses.views as courses

urlpatterns = [
    path('', include('courses.urls', namespace='courses')),
    path('admin/', admin.site.urls),
]
