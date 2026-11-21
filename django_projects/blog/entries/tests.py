from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Entry


class EntryViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", "alice@example.com", "s3cret-pass-123")

    def test_home_requires_login(self):
        response = self.client.get(reverse("blog-home"))
        self.assertRedirects(response, f"{reverse('login')}?next=/")

    def test_create_and_read_entry(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("create_entry"),
            {"entry_title": "Hello", "entry_text": "First post"},
        )
        self.assertRedirects(response, "/")

        entry = Entry.objects.get()
        self.assertEqual(entry.entry_author, self.user)

        response = self.client.get(reverse("entry-detail", args=[entry.pk]))
        self.assertContains(response, "First post")

    def test_home_paginates_newest_first(self):
        for i in range(4):
            Entry.objects.create(entry_title=f"Post {i}", entry_text="x", entry_author=self.user)
        self.client.force_login(self.user)
        response = self.client.get(reverse("blog-home"))
        titles = [e.entry_title for e in response.context["blog_entries"]]
        self.assertEqual(titles, ["Post 3", "Post 2", "Post 1"])
        self.assertTrue(response.context["is_paginated"])
