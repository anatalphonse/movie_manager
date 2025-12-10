# Movie Manager

**Movie Manager** is a Django-based web application designed to manage a collection of movies. It provides features for adding, viewing, updating, and deleting movie records, along with user authentication.

## Features

### 🎬 Movies App (`movies`)
The core application handles movie data management:
*   **Create**: Add new movies with details like title, year, description, and poster image.
*   **Read**: View a list of all movies and detailed views for specific movies.
*   **Update**: Edit existing movie details.
*   **Delete**: Remove movies from the collection.
*   **Relations**: Manages related data such as:
    *   **Directors**: Linked to movies via Foreign Key.
    *   **Actors**: Linked to movies via Many-to-Many relationship.
    *   **Censor Info**: Linked via One-to-One relationship (Rating, Certification).

### 👤 Users App (`users`)
Handles user access and authentication:
*   **Signup**: Register new users.
*   **Login**: Authenticate existing users.
*   **Logout**: Securely end user sessions.

## 🛠️ Utility Scripts
The project includes standalone scripts for data maintenance:
*   `check_data.py`: Verifies the integrity of movie data (e.g., checking years and ratings).
*   `fix_data.py`: Automatically patches missing data (e.g., sets default year to 2023 if missing).
*   `fix_ratings.py`: Normalizes rating data, converting string ratings to numeric values.

## 🚀 Getting Started

### Prerequisites
*   Python 3.x
*   PostgreSQL (configured in `settings.py`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/anatalphonse/movie_manager.git
    cd movie_manager
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    (Ensure you have Django and other required packages installed)
    ```bash
    pip install django pillow psycopg2
    ```

4.  **Database Configuration:**
    Ensure your PostgreSQL server is running and matches the credentials in `settings.py`:
    *   **Name**: `movies_db`
    *   **User**: `postgres`
    *   **Password**: `1236`
    *   **Host**: `localhost`

5.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    Access the app at `http://127.0.0.1:8000/`.

## 📂 Project Structure

*   `manage.py`: Django's command-line utility.
*   `settings.py`: Main configuration (Apps, Database, Static/Media roots).
*   `urls.py`: Main URL routing.
*   `movies/`: App folder for movie logic (models, views, urls).
*   `users/`: App folder for authentication logic.
*   `templates/`: HTML templates.
*   `static/`: CSS, JS, and image assets.
*   `media/`: User-uploaded content (movie posters).
