from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper

init_data = {
    "USERNAME": "test_user",
    "FIRST_NAME": "test_firstname",
    "LAST_NAME": "test_last_name",
    "PASSWORD": "test_password123",
    "YEARS_OF_EXPERIENCE": 2,
    "TITLE": "test title",
    "CONTENT": "test content",
    "TOPIC_NAME": "test topic name",
}


class TestNewspaper(TestCase):

    def setUp(self):
        redactor = get_user_model().objects.create_user(
            username=init_data["USERNAME"],
            password=init_data["PASSWORD"],
            last_name=init_data["LAST_NAME"],
            first_name=init_data["FIRST_NAME"],
            years_of_experience=init_data["YEARS_OF_EXPERIENCE"]
        )

        topic = Topic.objects.create(
            name=init_data["TOPIC_NAME"],
        )

        news = Newspaper.objects.create(
            title=init_data["TITLE"],
            content=init_data["CONTENT"],
            publisher=redactor
        )
        news.topic.add(topic)

    def test_topic_model(self):
        topic = Topic.objects.get(id=1)
        self.assertEqual(topic.name, init_data["TOPIC_NAME"])

    def test_str_topic(self):
        topic = Topic.objects.get(id=1)
        self.assertEqual(str(topic), topic.name)

    def test_redactor_model(self):
        driver = get_user_model().objects.get(id=1)
        self.assertEqual(driver.first_name, init_data["FIRST_NAME"])
        self.assertEqual(driver.last_name, init_data["LAST_NAME"])
        self.assertTrue(driver.check_password(init_data["PASSWORD"]))
        self.assertEqual(driver.username, init_data["USERNAME"])
        self.assertEqual(driver.years_of_experience, init_data["YEARS_OF_EXPERIENCE"])

    def test_str_redactor(self):
        redactor = get_user_model().objects.get(id=1)
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_str_newspaper(self):
        news = Newspaper.objects.get(id=1)
        self.assertEqual(str(news), init_data["TITLE"])

    def test_newspaper_model(self):
        news = Newspaper.objects.get(id=1)
        publisher = get_user_model().objects.get(id=1)
        topic = Topic.objects.get(id=1)
        self.assertTrue(topic in news.topic.all())
        self.assertEqual(news.publisher, publisher)
        self.assertEqual(news.content, init_data["CONTENT"])
