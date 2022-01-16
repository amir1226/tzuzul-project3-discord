from email import message
from django.test import TestCase, Client
from django.urls import reverse
from base import models

class TestsViews(TestCase):
    
    def setUp(self):
        self.user = models.User.objects.create(username="test-user", email="test@example.com", password="testpassword") 
        self.other_user = models.User.objects.create(username="test-user-2", email="test2@example.com", password="test2password")
        self.user.save()
        self.user_id = self.user.id  
        self.wrong_user_id = self.user.id + 10
        
        topic = models.Topic.objects.create(name="Test")
        
        room = models.Room.objects.create(
            host=self.user,
            topic = topic,
            name = "Test room",
            description = "A room for testing",
        )
        self.room_id = room.id
        
        message = models.Message.objects.create(
           user=self.user,
           room=room,
           body="This is a test message"
        )
        self.message_id = message.id
        
        self.client = Client()
        self.logged_client = Client()
        self.logged_client.force_login(self.user)
        self.other_logged = Client()
        self.other_logged.force_login(self.other_user)

        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')
        self.user_profile_url = reverse('user-profile', args=[self.user_id])
        self.user_profile_inexistent_url = reverse('user-profile', args=[self.wrong_user_id])
        self.create_room_url = reverse('create-room')
        self.update_room_url = reverse('update-room', args=[self.room_id])
        self.delete_room_url = reverse('delete-room', args=[self.room_id])
        self.delete_message_url = reverse('delete-message', args=[self.message_id])
        self.update_user_url = reverse('update-user')
        self.topics_url = reverse('topics')
        self.activity_url = reverse('activity')
        

        
    def test_base_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')
    
    def test_base_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login_register.html')

    def test_base_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login_register.html')
        
    def test_base_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.home_url)
    
    def test_base_profile_GET(self):
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/profile.html')
        
    def test_base_profile_GET_innexistent(self):
        response = self.client.get(self.user_profile_inexistent_url)
        self.assertEquals(response.status_code, 404)
        
    def test_base_create_room_GET_not_logged_in(self):
        response = self.client.get(self.create_room_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.create_room_url}')
        
    def test_base_create_room_GET(self):
        response = self.logged_client.get(self.create_room_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/room_form.html')

    def test_base_update_room_GET_not_logged_in(self):
        response = self.client.get(self.update_room_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.update_room_url}')

    def test_base_update_room_GET(self):
        response = self.logged_client.get(self.update_room_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/room_form.html')
        
    def test_base_delete_message_GET(self):
        response = self.logged_client.get(self.delete_message_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/delete.html')
        
    def test_base_other_user_try_delete_message(self):
        response = self.other_logged.post(self.delete_message_url)
        self.assertEquals(response.content, b'You are not allowed to delete this message!')
        message = models.Message.objects.get(id=self.message_id)
        self.assertIsInstance(message, models.Message)
        
    def test_base_delete_message(self):
        response = self.logged_client.post(self.delete_message_url)
        self.assertRedirects(response, self.home_url)
        self.assertIsNone(models.Message.objects.filter(id=self.message_id).first())
    
        
    def test_base_update_user_GET(self):
        response = self.logged_client.get(self.update_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/update-user.html')


    def test_base_topics_GET(self):
        response = self.client.get(self.topics_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/topics.html')
        
    def test_base_activity_GET(self):
        response = self.client.get(self.activity_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/activity.html')