from django.test import TestCase
from blog.models import Author, Tag, Post
from django.utils import timezone

# Create your tests here.

class AuthorModelTest(TestCase):
    def setUp(self):
        # Creem un autor per a les proves
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )

    def test_author_creation(self):
        # Comprovem que s'ha creat correctament
        self.assertEqual(self.author.first_name, "John")
        self.assertEqual(self.author.last_name, "Doe")
        self.assertEqual(str(self.author), "John Doe")  # __str__

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(tag="django")

    def test_tag_creation(self):
        self.assertEqual(self.tag.tag, "django")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "django")

    def test_tag_uniqueness(self):
        with self.assertRaises(Exception):
            Tag.objects.create(tag="django")  # Ja existeix, hauria de fallar si el camp és únic

class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com"
        )
        self.post = Post.objects.create(
            title="Test Post",
            excerpt="This is a test excerpt.",
            image_name="blog/images/test.jpg",
            content="This is the content of the post which should be long enough.",
            author=self.author,
            date=timezone.now(),
        )

    def test_post_creation(self):
        # Comprovem que el post s'ha creat i està vinculat a l'autor
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.first_name, "Alice")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post - Alice Smith")

    def test_slug_autogeneration(self):
        self.assertTrue(self.post.slug)  # El slug s'hauria d'haver generat automàticament

    def test_post_can_have_tags(self):
        tag1 = Tag.objects.create(tag="python")
        tag2 = Tag.objects.create(tag="web")
        self.post.tags.set([tag1, tag2])
        self.assertEqual(self.post.tags.count(), 2)
