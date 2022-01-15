from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views

class TestsUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.home)
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, views.login_page)
        
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, views.register_user)
        
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, views.logout_user)
        
    def test_profile_url_resolves(self):
        url = reverse('user-profile', args=["1"])
        self.assertEquals(resolve(url).func, views.user_profile)
        
    def test_create_room_url_resolves(self):
        url = reverse('create-room')
        self.assertEquals(resolve(url).func, views.create_room)
 
    def test_update_room_url_resolves(self):
        url = reverse('update-room', args=["1"])
        self.assertEquals(resolve(url).func, views.update_room)       
        
    def test_delete_room_url_resolves(self):
        url = reverse('delete-room', args=["1"])
        self.assertEquals(resolve(url).func, views.delete_room)       
    
    def test_delete_message_url_resolves(self):
        url = reverse('delete-message', args=["1"])
        self.assertEquals(resolve(url).func, views.delete_message)  
        
    def test_update_user_url_resolves(self):
        url = reverse('update-user')
        self.assertEquals(resolve(url).func, views.update_user)  

    def test_topics_url_resolves(self):
        url = reverse('topics')
        self.assertEquals(resolve(url).func, views.topics_page)  
        
    def test_activity_url_resolves(self):
        url = reverse('activity')
        self.assertEquals(resolve(url).func, views.activity_page)  
        
