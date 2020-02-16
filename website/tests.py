from django.test import TestCase
from website.models import Users

import json

class TestViews(TestCase):
    def test_users(self, fname="fname1", lname = "lname2"):
        return user.objects.create(fname = fname,lname = lname)

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, user))
        self.assertEqual(w.__unicode__(), w.fname)