from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import NewsForm
from newspaper.models import Newspaper, Redactor


class NewsListView(generic.ListView):
    model = Newspaper
    template_name = 'newspaper/news_list.html'
    paginate_by = 6


class NewsDetailView(generic.DetailView):
    model = Newspaper
    template_name = 'newspaper/news_detail.html'


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewsForm
    template_name = "newspaper/news_form.html"
    success_url = reverse_lazy("newspaper:index")


class NewsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewsForm
    template_name = "newspaper/news_form.html"
    success_url = reverse_lazy("newspaper:index")


class NewsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:index")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
