from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls.base import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="adminpassword3"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="test_driver",
            password="Qwerty123"
        )

    def test_redactor_(self):
        """
        Test that redactor years of experience on the admin page is listed
        """
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_driver_detail_listed(self):
        """
        Test that redactor years of experience on the admin detail page
        """
        url = reverse("admin:newspaper_redactor_change", args=[self.redactor.id])
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)
