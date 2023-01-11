from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class Test_Create_Post(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="django dev")
        test_user = User.objects.create_user(username='banryuuuu', password='1234562342fjpvafpiajwe')
        test_post = Post.objects.create(
            category_id = 2,
            author_id = 1,
            title = 'ang bantola',
            slug = 'post-title',
            status = 'published',
            content = 'post-content',
            excerpt = 'Post extension wire'
        )

        def test_blog_content (self):
            post = Post.post_objects.get(id=1)
            cat = Category.objects.get(id=1)
            author = f'{post.author}'
            excerpt = f'{post.excerpt}'
            title = f'{post.title}'
            content = f'{post.content}'
            status = f'{post. status}'
            self.assertEqual(author, 'banryuuuu')
            self.assertEqual(title, 'ang bantola')
            self.assertEqual(content, 'post-content')
            self.assertEqual(status, 'published')
            self.assertEqual(str(post), "Post Title")
            self.assertEqual(str(cat), "django ")