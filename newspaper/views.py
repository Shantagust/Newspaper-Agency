from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from newspaper import forms
from newspaper.models import Newspaper, Topic


class NewsListView(generic.ListView):
    model = Newspaper
    template_name = 'newspaper/news_list.html'
    paginate_by = 4


class NewsDetailView(generic.DetailView):
    model = Newspaper
    template_name = 'newspaper/news_detail.html'


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = forms.NewsForm
    template_name = "newspaper/news_form.html"
    success_url = reverse_lazy("newspaper:index")


class NewsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = forms.NewsForm
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
    form_class = forms.RedactorCreateForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = forms.RedactorForm


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("newspaper:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = forms.TopicForm


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = forms.TopicForm


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")
