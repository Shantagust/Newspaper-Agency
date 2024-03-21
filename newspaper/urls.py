from django.urls import path

from newspaper import views

urlpatterns = [
    path("", views.NewsListView.as_view(), name="index"),
    path("news/create/", views.NewsCreateView.as_view(), name="news-create"),
    path("news/<int:pk>/update/", views.NewsUpdateView.as_view(), name="news-update"),
    path("news/<int:pk>/delete/", views.NewsDeleteView.as_view(), name="news-delete"),
    path("news/<int:pk>/", views.NewsDetailView.as_view(), name="news-detail"),

    path("redactors/create/", views.RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/<int:pk>/update/", views.RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactors/<int:pk>/", views.RedactorDetailView.as_view(), name="redactor-detail"),
]
app_name = 'newspaper'


