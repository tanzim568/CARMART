# Car Rental Management System

A comprehensive Django web application for managing car rentals, brands, user profiles, and shopping carts. This project provides a complete solution for a car rental platform with user authentication, inventory management, and order tracking capabilities.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Usage Guide](#usage-guide)
- [Contributing](#contributing)
- [License](#license)

---

## Features

✨ **Core Features:**
- **Brand Management** - Create, read, update, and delete car brands with images and slug-based URLs
- **Car Inventory** - Manage cars with details including price, quantity, description, and associated brands
- **User Authentication** - Secure user registration and login with profile management
- **Shopping Cart** - Add cars to cart with quantity management
- **User Profiles** - View and edit user information with profile pictures
- **Responsive Design** - Bootstrap 5 integrated UI with crispy forms for professional styling
- **Admin Dashboard** - Django admin interface for comprehensive management of all models

---

## Project Structure

```
car_project/
├── BrandModel/                  # Car brands management app
│   ├── models.py               # Brand model definition
│   ├── views.py                # Brand-related views
│   ├── urls.py                 # Brand URL routing
│   ├── admin.py                # Admin interface configuration
│   ├── migrations/             # Database migration files
│   ├── templates/              # Brand-related templates
│   └── media/uploads/          # Brand image uploads
│
├── CarModel/                    # Car inventory management app
│   ├── models.py               # Car model definition (with ForeignKey to Brand)
│   ├── views.py                # Car-related views
│   ├── urls.py                 # Car URL routing
│   ├── admin.py                # Admin interface configuration
│   ├── migrations/             # Database migration files
│   ├── templates/              # Car-related templates
│   └── media/uploads/          # Car image uploads
│
├── Profile/                     # User profile management app
│   ├── models.py               # Profile model definition
│   ├── views.py                # Profile-related views
│   ├── forms.py                # User forms (registration, profile editing)
│   ├── urls.py                 # Profile URL routing
│   ├── admin.py                # Admin interface configuration
│   ├── migrations/             # Database migration files
│   └── templates/
│       ├── register.html       # User registration template
│       ├── profile.html        # User profile template
│       ├── edit_profile.html   # Profile editing template
│       └── pass.html           # Password management template
│
├── cart/                        # Shopping cart management app
│   ├── models.py               # Cart model (User -> Car relationship)
│   ├── views.py                # Cart-related views
│   ├── admin.py                # Admin interface configuration
│   └── migrations/             # Database migration files
│
├── car_project/                 # Main project configuration
│   ├── settings.py             # Django settings and configuration
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── static/                      # Static files (CSS, JavaScript, images)
│   └── css/
│       └── app.css             # Application styles
│
├── templates/                   # Global templates
│   ├── base.html               # Base template with navigation
│   ├── home.html               # Homepage template
│   └── components/
│       ├── navbar.html         # Navigation bar component
│       ├── footer.html         # Footer component
│       ├── buttons.html        # Button components
│       ├── form_field.html     # Form field component
│       └── messages.html       # Messages component
│
├── manage.py                    # Django management command
├── db.sqlite3                   # SQLite database
└── README.md                    # Project documentation
```

---

## Technologies

**Backend:**
- Django 5.1.1
- Python 3.x
- SQLite (default database)

**Frontend:**
- HTML5
- CSS3 / Bootstrap 5
- Django Crispy Forms with Bootstrap 5 template pack

**Additional Libraries:**
- Pillow (for image handling)
- crispy-bootstrap5 (for form styling)

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd car_project
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install django==5.1.1
pip install pillow
pip install django-crispy-forms
pip install crispy-bootstrap5
```

---

## Configuration

### Database Setup

Apply migrations to initialize the database:

```bash
python manage.py migrate
```

### Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Enter your preferred username, email, and password when prompted.

### Static Files (if needed for production)

```bash
python manage.py collectstatic
```

---

## Running the Project

### Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Access Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Manage brands, cars, users, and cart items

---

## API Endpoints

### Home & Browsing
- `GET /` - Homepage with all cars
- `GET /brandmodel/<slug:brand_slug>/` - View cars filtered by brand

### Car Management
- Accessible via `/carmodel/` (see CarModel.urls)

### Brand Management
- Accessible via `/brandmodel/` (see BrandModel.urls)

### User Accounts
- `GET/POST /accounts/register/` - User registration
- `GET/POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout
- `GET /accounts/profile/` - User profile
- `GET/POST /accounts/edit-profile/` - Edit user profile

### Admin
- `GET /admin/` - Django admin interface

---

## Database Models

### Brand Model
```python
class Brand(models.Model):
    name = CharField(max_length=100)
    image = ImageField(upload_to='BrandModel/media/uploads')
    slug = SlugField(max_length=200, unique=True)
```

### Car Model
```python
class Car(models.Model):
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity = IntegerField()
    description = TextField()
    image = ImageField(upload_to='CarModel/media/uploads')
    brand = ForeignKey(Brand, on_delete=CASCADE, related_name='brand')
```

### Cart Model
```python
class Cart(models.Model):
    user = ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    car = ForeignKey(Car, on_delete=CASCADE, null=True, blank=True)
    quantity = IntegerField(default=1, null=True, blank=True)
```

### Profile Model
- Extends Django's built-in User model for additional user information

---

## Usage Guide

### For Customers

1. **Browse Cars** - Visit the homepage to see all available cars
2. **Filter by Brand** - Click on a brand to view cars from that brand
3. **Register** - Create a new account via `/accounts/register/`
4. **Manage Profile** - View and edit your profile information
5. **Add to Cart** - Add desired cars to your shopping cart
6. **View Cart** - Review items in your cart and manage quantities

### For Administrators

1. **Access Admin Panel** - Log in at `/admin/` with superuser credentials
2. **Manage Brands** - Create, update, and delete car brands
3. **Manage Inventory** - Add new cars, update prices, and manage stock
4. **Manage Users** - View user accounts and manage permissions
5. **Monitor Orders** - Track cart items and customer activity

---

## Future Enhancements

- [ ] Payment gateway integration
- [ ] Order confirmation and tracking
- [ ] Email notifications
- [ ] Advanced search and filtering
- [ ] Car rental date management
- [ ] Review and rating system
- [ ] API endpoints (REST API)
- [ ] Mobile application
- [ ] Deployment to production server

---

## Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'django'`
- **Solution:** Ensure virtual environment is activated and run `pip install -r requirements.txt`

**Issue:** Images not displaying
- **Solution:** Ensure `DEBUG = True` in settings.py and media URLs are properly configured

**Issue:** Database errors after model changes
- **Solution:** Create and run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is part of the Mid Term Exam for Week 5 of the Phitron Django course.

---

## Support

For questions or issues, please create an issue in the repository or contact the project maintainer.

---

**Last Updated:** August 2024  
**Django Version:** 5.1.1  
**Python Version:** 3.8+
