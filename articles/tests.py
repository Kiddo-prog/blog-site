from traceback import print_tb
from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article

# Create your tests here.

# title author date_created text status slug
class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username="test_user", password="12335454")
        test_article = Article.objects.create(
            author_id=1,
            title="hello world",
            slug="hello-world",
            text="this is hello world",
            status="published",
            description="hi hello world",
        )

    def test_blog_content(self):
        post = Article.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        text = f"{post.text}"

        self.assertEqual(author, "test_user")
        self.assertEqual(title, "hello world")
        self.assertEqual(text, "this is hello world")
        self.assertEqual(str(post), "hello world")
