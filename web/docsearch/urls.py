from django.urls import path

from . import views

app_name = 'docsearch'
urlpatterns = [
    path('', views.top, name='top'),
    path('update/', views.update, name='update'),
    path('update_result/', views.update_result, name='update_result'),
    path('search/', views.search, name='search'),
    path('search_result/', views.SearchView.as_view(), name='search_result'),
    
]