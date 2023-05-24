from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileModelTest(TestCase):
    

    def test_avatar_field(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=user, avatar='profiles/no-avatar.jpg', bio='Test bio', link='http://www.google.com')
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('avatar').verbose_name
        self.assertEqual(field_label, 'avatar')

    def test_bio_field(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=user, avatar='profiles/no-avatar.jpg', bio='Test bio', link='http://www.google.com')
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_link_field(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=user, avatar='profiles/no-avatar.jpg', bio='Test bio', link='http://www.google.com')
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('link').verbose_name
        self.assertEqual(field_label, 'link')
