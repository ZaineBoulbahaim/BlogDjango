from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Author, Tag
from django.utils import timezone

class BlogViewsTest(TestCase):
    def setUp(self):
        # Crear autor i post de prova
        self.author = Author.objects.create(
            first_name="Test",
            last_name="User",
            email="test@example.com"
        )
        self.tag = Tag.objects.create(tag="testing")
        self.post = Post.objects.create(
            title="Test Post",
            excerpt="Resum de prova",
            image_name="blog/images/test.jpg",
            content="Contingut de prova",
            date=timezone.now(),
            author=self.author,
        )
        self.post.tags.add(self.tag)

    def test_starting_page_view(self):
        url = reverse("blog:starting-page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_posts_list_view(self):
        url = reverse("blog:posts-page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view_success(self):
        url = reverse("blog:post-detail", args=[self.post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contingut de prova")

    def test_post_detail_view_404(self):
        url = reverse("blog:post-detail", args=["slug-inexistent"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_author_detail_view(self):
        url = reverse("blog:autors-detail", args=[self.author.last_name.lower()])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test")

    def test_tag_detail_view(self):
        url = reverse("blog:tag-detail", args=[self.tag.tag.lower()])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
