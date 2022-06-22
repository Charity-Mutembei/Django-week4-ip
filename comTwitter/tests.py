from django.test import TestCase
from .models import Post,NeighbourHood, UserProfile, Business

#create tests for the model classes

class PostTestClass(TestCase):
    """
    this test class is one to test the class model Post
    """
    #setupmethod
    def setUp(self):
        self.body = Post(body= '')

    #testing whether we are being instanciated properly

    def test_instance (self):
        self.assertTrue(isinstance(self.body, Post))


    #testing the save method

    def test_save_method(self):
        self.body.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)>0)

class UserProfileTestClass(TestCase):
    """
    a test class of the model class Profile
    """
    #setup method for this class
    def setUp(self):
        self.author = UserProfile(author = '')

    #testing whether we are being instanciated in the right way
    def test_instance(self):
        self.assertTrue(isinstance(self.author, UserProfile))

    #testing the save method for this class
    def test_save_method(self):
        self.author.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles)>0)
class NeighbourHoodTestClass(TestCase):
    """
    a test class of the model class tags
    """
    #setup method for the class tags
    def setUp(self):
        self.location = NeighbourHood(location= '')

    #testing whether the instance is properly made
    def test_instance(self):
        self.assertTrue(isinstance(self.location, NeighbourHood))

    #testing that the save method is proper for this class
    def test_save_method(self):
        self.location.save_neighborhood()
        tags = NeighbourHood.objects.all()
        self.assertTrue(len(tags)>0)
class  BusinessTestClass(TestCase):
    """
    a test class of the model class tags
    """
    #setup method for the class tags
    def setUp(self):
        self.name =  Business (name= '')


    def test_instance(self):
        self.assertTrue(isinstance(self.name, Business))