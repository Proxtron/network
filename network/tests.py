from django.test import TestCase, Client
from .models import User, Post
# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(
            username="proxtron", 
            email="bratan_pavel@yahoo.com",
        )
        post = Post.objects.create(
            message="Hello, World",
            author=user,
        )

    def testUser(self):
        user = User.objects.get(username='proxtron')
        self.assertTrue(user.username == 'proxtron' and user.email == 'bratan_pavel@yahoo.com')

    def testPostToAuthor(self):
        user = User.objects.get(username='proxtron')
        post = Post.objects.get(message="Hello, World")
        self.assertTrue(post.author == user)

    def testUserToPosts(self):
        user = User.objects.get(username='proxtron')
        post = Post.objects.get(message="Hello, World")
        
        self.assertTrue(post == user.posts.get(message="Hello, World"))


    
        