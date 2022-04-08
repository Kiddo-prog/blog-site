from django.test import TestCase
from django.contrib.auth.models import User
from user.models import Profile

# Create your tests here.


class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username="kingi", password="3565368943")
        test_profile = Profile.objects.create(
            username_id=1, info="This is a test profile"
        )
        show_user = User.objects.get(id=1)
        print(show_user)

    def test_content(self):
        profile = Profile.objects.get(id=1)
        user = User.objects.get(id=1)
        username = f"{profile.username}"
        info = f"{profile.info}"

        self.assertEqual(username, "kingi")
        self.assertEqual(info, "This is a test profile")
        self.assertEqual(str(user), "kingi")
