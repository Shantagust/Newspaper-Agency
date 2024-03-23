from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.forms import RedactorCreateForm, SearchForm
from newspaper.models import Newspaper, Topic


class CreateFormsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="TeJus2pwd",
            last_name="test_last_name",
            first_name="test_first_name"
        )
        self.topic = Topic.objects.create(
            name="test_topic"
        )
        self.newspaper = Newspaper.objects.create(
            title="test title",
            content="test content",
            publisher=self.user
        )
        self.newspaper.topic.add(self.topic)
        self.client.force_login(user=self.user)

    def test_form_create_topic(self):
        topic_data = {
            "name": "test topic",
        }
        self.client.post(reverse("newspaper:topic-create"), data=topic_data)
        topic = Topic.objects.get(name=topic_data["name"])
        self.assertEqual(topic.name, topic_data["name"])

    def test_form_create_redactor(self) -> None:
        redactor_data = {
            "username": "testuser",
            "password1": "MNBJD*@2",
            "password2": "MNBJD*@2",
            "first_name": "first_name_test",
            "last_name": "last_name_test",
            "years_of_experience": 2
        }
        self.client.post(reverse("newspaper:redactor-create"), data=redactor_data)
        new_redactor = get_user_model().objects.get(
            username=redactor_data["username"]
        )

        self.assertEqual(new_redactor.username, redactor_data["username"])
        self.assertEqual(new_redactor.first_name, redactor_data["first_name"])
        self.assertEqual(new_redactor.last_name, redactor_data["last_name"])
        self.assertEqual(
            new_redactor.years_of_experience,
            redactor_data["years_of_experience"]
        )

    def test_check_user_creation_form_with_valid_data(self):
        user_data = {
            "username": "test_user2",
            "password1": "smthp2swd",
            "password2": "smthp2swd",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 2,
        }
        form = RedactorCreateForm(data=user_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, user_data)

    def test_search_form_for_redactor_by_username(self):
        search_data = {"username": self.user.username}
        form = SearchForm(data=search_data)
        response = self.client.get(reverse("newspaper:redactor-list"), data=search_data)
        self.assertTrue(form.is_valid())
        self.assertContains(response, self.user.username)
        self.assertEqual(response.status_code, 200)

    def test_search_form_for_news_by_title(self):
        search_data = {"title": self.newspaper.title}
        form = SearchForm(data=search_data)
        response = self.client.get(reverse("newspaper:news-list"), data=search_data)
        self.assertTrue(form.is_valid())
        self.assertContains(response, self.newspaper.title)
        self.assertEqual(response.status_code, 200)
