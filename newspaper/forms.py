from django import forms

from newspaper.models import Newspaper, Topic


class NewsForm(forms.ModelForm):
    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
