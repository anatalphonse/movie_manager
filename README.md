# MoviesDb

# MoviesDB Manager

A Django-based application for managing a movie database. This project uses PostgreSQL as its database backend.

## Features
- Manage movies and related data.
- Supports PostgreSQL database for efficient data storage and querying.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python (3.8 or later)
- PostgreSQL
- Virtualenv (optional but recommended)

---

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anatalphonse/MoviesDb.git
   cd MoviesDb/movie_manager
   ```

2. **Set Up the Virtual Environment:**
   ```bash
   pip install virtualenv
   virtualenv --version
   virtualenv my_env
   ```

3. **Activate the Virtual Environment:**
   ```bash
   cd my_env
   cd Scripts
   activate
   ```

4. **Install Django:**
   ```bash
   pip install django
   python -m django --version
   ```

5. **Deactivate and Reactivate the Virtual Environment (if needed):**
   ```bash
   deactivate
   activate
   ```

6. **Install Required Packages:**
   ```bash
   cd ..
   cd movie_manager
   pip install psycopg2
   pip install psycopg2-binary
   pip install psycopg
   pip list  # Ensure either psycopg2 or psycopg appears in the list.
   python -m pip install Pillow
   ```

7. **Configure the Database:**
   Update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

8. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

9. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

10. **Access the Application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'django'`
- Ensure the virtual environment is activated.
- Install Django:
  ```bash
  pip install django
  ```

### Error: `No module named 'psycopg'` or `No module named 'psycopg2'`
- Install the PostgreSQL adapter:
  ```bash
  pip install psycopg2-binary
  ```
  Or use the modern `psycopg`:
  ```bash
  pip install psycopg
  ```

### Error: `django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module`
- Double-check your database settings in `settings.py` and ensure the correct adapter is installed.

---

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the [MIT License](LICENSE).

