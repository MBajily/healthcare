# Healthcare Management System

A comprehensive Django-based healthcare management system that connects patients, hospitals, and healthcare ministry administrators. The system facilitates medical record management, patient tracking, and healthcare service delivery.

## Features

### For Patients
- Personal health record management
- View medical history
- Track prescriptions and medical examinations
- Monitor basic health metrics (heart rate, oxygen saturation, etc.)
- Connect with hospitals and healthcare providers

### For Hospitals
- Patient management
- Medical examination records
- Prescription management
- Disease tracking
- Basic health state monitoring
- Patient history tracking

### For Ministry Administrators
- Hospital management
- System-wide patient oversight
- Healthcare statistics and analytics
- User management
- Data validation and verification

## Technical Stack

### Backend
- Django 4.1.2
- Python 3.x
- SQLite3 database

### Frontend
- HTML5/CSS3
- JavaScript
- jQuery
- Bootstrap
- Chart.js for analytics
- DataTables for data presentation

### Additional Libraries
- django-crispy-forms==1.14.0
- Pillow==11.1.0 (for image processing)
- bcrypt==4.0.1 (for security)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MBajily/healthcare
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Key Components

- **API App**: Core models and database structure
- **Home App**: Landing pages and authentication
- **Hospital App**: Hospital-specific features
- **Ministry App**: Administrative features
- **Patient App**: Patient portal features

## User Roles

1. **Patient**
   - View personal medical history
   - Track health metrics
   - Access prescriptions

2. **Hospital Staff**
   - Manage patient records
   - Create medical examinations
   - Issue prescriptions
   - Monitor patient health

3. **Ministry Administrator**
   - Manage hospitals
   - Overview of healthcare system
   - Access analytics and reports

## Security Features

- User authentication and authorization
- Role-based access control
- Password hashing with bcrypt
- Form validation and sanitization
- Protected file uploads

## Database Schema

The system uses a relational database with the following key models:

- User (Extended Django User)
- Patient Profile
- Hospital Profile
- Medical Examination
- Prescription
- Basic Health State
- Disease
- Civil Status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Authors

Mohammed Elgaily (@MBajily)

## Acknowledgments

- Django community
- Bootstrap contributors
- Other third-party package maintainers

## Support

For support, please contact elgaily.com
