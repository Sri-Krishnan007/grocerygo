GroceryGo 🛒

GroceryGo is a simple Django-based web application for managing and browsing grocery products. 
The site leverages Bootstrap for responsive design and uses MySQL as the database backend. 
The admin has exclusive privileges to add and manage products, while users can view the available products.
Features

Admin Panel:  
  Admin can log in to a secure admin panel to add, update, or delete grocery products.
  
Product Catalog:  
  A user-friendly product listing page displays available grocery items.

Responsive Design:  
  Bootstrap integration ensures a sleek and mobile-friendly interface.

 Tech Stack

Backend: Django 
Frontend: Bootstrap 
Database: MySQL
Environment: Python 3.8+  

---

## Installation

### Prerequisites

1. Python 3.8 or later installed on your system.
2. MySQL server installed and configured.
3. A virtual environment manager (recommended: `venv` or `virtualenv`).

### Steps

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/grocerygo.git
   cd grocerygo
   ```

2. **Set up the Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL Database**  
   Update the `DATABASES` configuration in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'grocerygo_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Apply Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Admin)**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**  
   Open your browser and navigate to:  
   - Admin panel: `http://127.0.0.1:8000/admin/`  
   - Product listing: `http://127.0.0.1:8000/`

---

## Usage

- **Admin**:  
  - Log in to the admin panel (`/admin`) to manage products.
  - Add product details such as name, price, category, and description.
  
- **Users**:  
  - Browse the product catalog from the homepage.
  - View details of individual products.

---

## Folder Structure

```
grocerygo/
├── grocerygo/        # Project configuration files
├── products/         # App for managing products
│   ├── migrations/   # Database migrations
│   ├── templates/    # HTML templates
│   ├── static/       # Bootstrap and custom CSS/JS
├── db.sqlite3        # Default SQLite DB (for testing)
├── requirements.txt  # Python dependencies
└── manage.py         # Django's command-line utility
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: your-email@example.com  
- **GitHub**: [your-username](https://github.com/your-username)

--- 

Feel free to adjust the content as per your requirements!
