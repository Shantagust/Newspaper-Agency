from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Redactor"
        verbose_name_plural = "Redactors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topic = models.ManyToManyField(Topic)
    publisher = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("newspaper:news-detail", kwargs={"pk": self.pk})
