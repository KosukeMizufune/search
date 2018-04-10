from django.urls import path

from . import views

app_name = 'docsearch'
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('update/', views.update, name='update'),
    path('update_result/', views.UploadView.as_view(), name='update_result'),
    path('search_result/', views.SearchView.as_view(), name='search_result'),
    path('<int:pk>/search_text/', views.TextView.as_view(), name='search_text')
]
