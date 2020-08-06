from django.urls import path
from tutorial import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'tutorial'
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
