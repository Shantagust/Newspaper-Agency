from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Newspaper, Topic
from tests.test_models import init_data


class PublicViewsTest(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username=init_data["USERNAME"],
            password=init_data["PASSWORD"],
            last_name=init_data["LAST_NAME"],
            first_name=init_data["FIRST_NAME"],
            years_of_experience=init_data["YEARS_OF_EXPERIENCE"]
        )

        self.topic = Topic.objects.create(
            name=init_data["TOPIC_NAME"],
        )

        self.news = Newspaper.objects.create(
            title=init_data["TITLE"],
            content=init_data["CONTENT"],
            publisher=self.redactor
        )
        self.news.topic.add(self.topic)

    def test_without_login_news_list(self):
        res = self.client.get(reverse("newspaper:news-list"))
        self.assertTrue(res.status_code == 200)

    def test_without_login_news_detail(self):
        res = self.client.get(reverse("newspaper:news-detail", kwargs={"pk": 1}))
        self.assertEqual(res.status_code, 200)

    def test_login_required_news_create(self):
        res = self.client.get(reverse("newspaper:news-create"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_news_delete(self):
        res = self.client.get(reverse("newspaper:news-delete", kwargs={"pk": self.news.id}))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_redactor_list(self):
        res = self.client.get(reverse("newspaper:redactor-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_redactor_detail_page(self):
        res = self.client.get(reverse("newspaper:redactor-detail", kwargs={"pk": self.redactor.id}))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_redactor_edit_page(self):
        res = self.client.get(reverse("newspaper:redactor-update", kwargs={"pk": self.redactor.id}))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_redactor_delete_page(self):
        res = self.client.get(reverse("newspaper:redactor-delete", kwargs={"pk": self.redactor.id}))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_topic_list(self):
        res = self.client.get(reverse("newspaper:topic-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_topic_edit_page(self):
        res = self.client.get(reverse("newspaper:topic-update", kwargs={"pk": self.topic.id}))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_topic_delete_page(self):
        res = self.client.get(reverse("newspaper:topic-delete", kwargs={"pk": self.topic.id}))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_redactor_detail(self):
        res = self.client.get(
            reverse(
                "newspaper:redactor-detail",
                args=[self.redactor.id])
        )
        self.assertNotEqual(res.status_code, 200)


class PrivateViewsTest(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username=init_data["USERNAME"],
            password=init_data["PASSWORD"],
            last_name=init_data["LAST_NAME"],
            first_name=init_data["FIRST_NAME"],
            years_of_experience=init_data["YEARS_OF_EXPERIENCE"]
        )

        self.topic = Topic.objects.create(
            name=init_data["TOPIC_NAME"],
        )

        self.news = Newspaper.objects.create(
            title=init_data["TITLE"],
            content=init_data["CONTENT"],
            publisher=self.redactor
        )
        self.news.topic.add(self.topic)
        self.client.force_login(self.redactor)

    def test_redactor_access_to_topic_list(self):
        response = self.client.get(reverse("newspaper:topic-list"))
        self.assertEqual(response.status_code, 200)

    def test_redactor_access_to_redactor_list(self):
        response = self.client.get(reverse("newspaper:redactor-list"))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_manufacturer_list(self):
        topic_list = Topic.objects.all()
        response = self.client.get(reverse("newspaper:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topic_list)
        )
        self.assertTemplateUsed(response, "newspaper/topic_list.html")

    def test_retrieve_redactor_list(self):
        redactor_list = get_user_model().objects.all()
        response = self.client.get(reverse("newspaper:redactor-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactor_list)
        )
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")
