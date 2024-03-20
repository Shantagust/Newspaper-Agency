from django import forms

from newspaper.models import Redactor, Newspaper


class NewsForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
