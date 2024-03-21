from django.urls import path

from newspaper.views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView, \
    RedactorDetailView

urlpatterns = [
    path("", NewsListView.as_view(), name="index"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("news/create/", NewsCreateView.as_view(), name="news-create"),
    path("news/<int:pk>/update/", NewsUpdateView.as_view(), name="news-update"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("news/<int:pk>/delete/", NewsDeleteView.as_view(), name="news-delete"),

    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail")
]
app_name = 'newspaper'
