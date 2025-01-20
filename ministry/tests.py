from django.test import TestCase, Client
from django.urls import reverse
from api.models import User
from .forms import RegisterForm, CivilStatusForm
from django.contrib.auth.hashers import make_password

class MinistryViewTests(TestCase):
    def setUp(self):
        # Create test admin user with hashed password
        self.admin_user = User.objects.create(
            email='admin@test.com',
            password=make_password('testpass123'),
            role='ADMIN'
        )
        
        # Create test patient user
        self.patient_user = User.objects.create(
            email='patient@test.com',
            password=make_password('testpass123'),
            role='PATIENT'
        )
        
        # Create test hospital user
        self.hospital_user = User.objects.create(
            email='hospital@test.com',
            password=make_password('testpass123'),
            role='HOSPITAL'
        )
        
        self.client = Client()

    def test_dashboard_view_admin_access(self):
        """Test dashboard view is accessible by admin"""
        # Login properly with the client
        login_successful = self.client.login(email='admin@test.com', password='testpass123')
        self.assertTrue(login_successful)
        
        # Force authentication for the request
        self.client.force_login(self.admin_user)
        
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ministry/dashboard/dashboard.html')  # Updated template path

    def test_dashboard_view_patient_access_denied(self):
        """Test dashboard view is not accessible by patient"""
        # Login properly with the client
        login_successful = self.client.login(email='patient@test.com', password='testpass123')
        self.assertTrue(login_successful)
        
        # Force authentication for the request
        self.client.force_login(self.patient_user)
        
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 403)  # Should be forbidden for patients

    def test_add_hospital_view(self):
        """Test add hospital functionality"""
        # Login and force authentication
        self.client.login(email='admin@test.com', password='testpass123')
        self.client.force_login(self.admin_user)
        
        data = {
            'email': 'newhospital@test.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'role': 'HOSPITAL'  # Added role field
        }
        response = self.client.post(reverse('add_hospital'), data, follow=True)  # Added follow=True
        
        # Check if the hospital was created
        self.assertTrue(User.objects.filter(email='newhospital@test.com', role='HOSPITAL').exists())
        self.assertEqual(response.status_code, 200)  # Should be 200 after following redirect

class MinistryFormTests(TestCase):
    def test_register_form_valid(self):
        """Test RegisterForm validation"""
        form_data = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_civil_status_form_valid(self):
        """Test CivilStatusForm validation"""
        form_data = {
            'nationality_id': '1234567890',
            'full_name': 'Test User',
            'birth': '1990-01-01',
            'gender': 'Male'
        }
        form = CivilStatusForm(data=form_data)
        self.assertTrue(form.is_valid())
