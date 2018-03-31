from django.urls import path

from . import views

app_name = 'docsearch'
urlpatterns = [
    path('', views.top, name='top'),
    path('update/', views.update, name='update'),
]