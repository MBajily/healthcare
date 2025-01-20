from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse
from api.models import User, Civil_Status, PatientProfile, Hospital, Patient
from .forms import RegisterForm, CivilStatusForm
from .decorators import allowed_users
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

class DecoratorTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create(
            email='admin@gmail.com',
            password='123123',
            role='ADMIN'
        )
        self.client = Client()

    def test_allowed_users_decorator(self):
        """Test allowed_users decorator"""
        @allowed_users(allowed_roles=['ADMIN'])
        def test_view(request):
            return HttpResponse("Test view")

        self.client.login(email='admin@gmail.com', password='123123')
        request = self.client.get('/').wsgi_request
        request.user = self.admin_user
        
        response = test_view(request)
        self.assertEqual(response.status_code, 200)

class ModelIntegrationTests(TestCase):
    def setUp(self):
        # Create test hospital user
        self.hospital_user = Hospital.objects.create(
            email='hospital@test.com',
            password=make_password('testpass123'),
            role='HOSPITAL'
        )

    def test_patient_creation_integration(self):
        """Test patient creation and profile integration"""
        # Create civil status first
        civil_status = Civil_Status.objects.create(
            nationality_id='P123',
            full_name='Test Patient',
            birth='1990-01-01',
            gender='Male'
        )
        
        # Create patient user - profile will be created automatically
        patient_user = Patient.objects.create(
            email='patient@test.com',
            password=make_password('testpass123'),
            role='PATIENT'
        )
        
        # Get the automatically created profile
        patient_profile = PatientProfile.objects.get(user=patient_user)
        
        # Update the profile with civil status
        patient_profile.civil_status = civil_status
        patient_profile.phone = '1234567890'
        patient_profile.save()

        self.assertEqual(patient_profile.user.email, 'patient@test.com')
        self.assertEqual(patient_profile.civil_status.full_name, 'Test Patient')

    def test_new_patient_registration_flow(self):
        """Test complete flow of new patient registration with civil status check"""
        # Test data
        patient_email = 'newpatient@test.com'
        nationality_id = 'P125'
        
        # Check and create civil status
        civil_status_exists = Civil_Status.objects.filter(nationality_id=nationality_id).exists()
        self.assertFalse(civil_status_exists)
        
        civil_status = Civil_Status.objects.create(
            nationality_id=nationality_id,
            full_name='New Test Patient',
            birth='1995-01-01',
            gender='Male'
        )
        
        # Create patient - profile will be created automatically
        patient_user = Patient.objects.create(
            email=patient_email,
            password=make_password('testpass123'),
            role='PATIENT'
        )
        
        # Get and update the profile
        patient_profile = PatientProfile.objects.get(user=patient_user)
        patient_profile.civil_status = civil_status
        patient_profile.phone = '9876543210'
        patient_profile.save()
        
        # Verify everything
        self.assertTrue(User.objects.filter(email=patient_email).exists())
        self.assertTrue(Civil_Status.objects.filter(nationality_id=nationality_id).exists())
        self.assertEqual(patient_profile.civil_status.nationality_id, nationality_id)
