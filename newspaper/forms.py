from django import forms

from newspaper.models import Newspaper, Topic


class NewsForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = ("title", "publisher", "content")
