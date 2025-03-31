from django.urls import path
from . import views

urlpatterns = [
    path('api/lectures', views.lecture_list, name='lecture-list'),
    path('api/lectures/add-form', views.lecture_post, name='lecture-post'),
    path('api/lectures/form', views.lecture_form, name='lecture-form'),
    path('api/lectures/main', views.lecture_main, name='lecture-main'),
    path('api/lectures/callendar', views.lecture_calendar, name='lecture-callendar'),
]
