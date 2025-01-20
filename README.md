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


## Testing

The system includes comprehensive test coverage for core functionality across different apps. Here's an overview of the test suite:

### Ministry App Tests

#### View Tests (`MinistryViewTests`)
- **Dashboard Access Tests**
  - Verifies admin access to dashboard
  - Confirms patient access is denied
  - Tests template rendering
- **Hospital Management Tests**
  - Tests hospital creation functionality
  - Validates form submission
  - Verifies user role assignment

#### Form Tests (`MinistryFormTests`)
- **Registration Form Tests**
  - Validates email format
  - Tests password confirmation
  - Checks required fields
- **Civil Status Form Tests**
  - Validates nationality ID format
  - Tests date formatting
  - Verifies gender choices

#### Decorator Tests (`DecoratorTests`)
- Tests role-based access control
- Verifies allowed_users decorator functionality
- Checks permission enforcement

#### Integration Tests (`ModelIntegrationTests`)
- **Patient Creation Flow**
  - Tests complete patient registration process
  - Verifies automatic profile creation
  - Validates civil status linkage
- **Civil Status Integration**
  - Tests civil status requirements
  - Verifies data relationships
  - Checks constraint enforcement

### Running Tests

To run the complete test suite:
   ```bash
   python manage.py test
   ```

To run specific app tests:
   ```bash
   python manage.py test ministry
   ```

### Test Coverage

The test suite covers:
- User authentication and authorization
- Form validation and submission
- Model relationships and constraints
- View permissions and access control
- Integration between different components

### Writing New Tests

When adding new features, please ensure:
1. Write tests before implementing features (TDD approach)
2. Cover both success and failure cases
3. Test edge cases and boundary conditions
4. Include integration tests for complex features
5. Follow the existing test structure and naming conventions
   

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
