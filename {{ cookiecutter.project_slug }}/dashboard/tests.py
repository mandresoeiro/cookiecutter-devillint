import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from model_bakery import baker

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return baker.make(User)

@pytest.mark.django_db
class TestDashboardViews:
    def test_dashboard_home_view(self, client, user):
        client.force_login(user)
        url = reverse('dashboard:home')
        response = client.get(url)
        assert response.status_code == 200
        assert 'total_users' in response.context

@pytest.mark.django_db
class TestUserAPI:
    def test_list_users(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse('dashboard:user-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        
    def test_create_user(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse('dashboard:user-list')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username='testuser').exists()