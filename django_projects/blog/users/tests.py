from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthFlowTests(TestCase):
    def test_register_logs_user_in(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "bob",
                "email": "bob@example.com",
                "password1": "a-Strong-pass-987",
                "password2": "a-Strong-pass-987",
            },
        )
        self.assertRedirects(response, reverse("blog-home"))
        self.assertTrue(User.objects.filter(username="bob").exists())
        self.assertEqual(int(self.client.session["_auth_user_id"]), User.objects.get(username="bob").pk)

    def test_logout_is_post(self):
        User.objects.create_user("carol", password="pw-123456-xyz")
        self.client.login(username="carol", password="pw-123456-xyz")
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("_auth_user_id", self.client.session)
