from django.test import TestCase
from base import models
import datetime
class TestModels(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(username="test-user", email="test@example.com", password="testpassword") 
        
    def test_user_id_added_in_DB(self):
        self.assertIsNotNone(self.user.id)
        
    def test_room_model_created(self):
        room = models.Room.objects.create(
            host = self.user,
            topic = models.Topic.objects.create(name="Test topic"),
            name = "Test room",
            description = "Test description"
        )
        self.assertEqual(room.created.date(),datetime.datetime.now().date())
        self.assertEqual(room.updated.date(),datetime.datetime.now().date())
