from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import NewsForm, RedactorForm, RedactorCreateForm
from newspaper.models import Newspaper


class NewsListView(generic.ListView):
    model = Newspaper
    template_name = 'newspaper/news_list.html'
    paginate_by = 4


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


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 2


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = RedactorCreateForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = RedactorForm


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("newspaper:redactor-list")
