# Django Watchlist App API

This repository contains a Django project for managing a watchlist of movies and TV shows, providing a RESTful API using the Django REST Framework.

## Features

- **Watchlists:** Manage a list of movies and TV shows with details such as name, description, and status.
- **Stream Platforms:** Keep track of different streaming platforms where content is available.
- **Reviews:** Users can review and rate items on the watchlist.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/amirjahantab/Create_Simple_RestAPI.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Visit `http://localhost:8000` in your browser to access the API.

## API Endpoints

- **Watchlist:**
  - List all watchlist items: `/list/` (GET)
  - Retrieve a specific item: `/<int:pk>/` (GET)
  - Create a new item: `/list/` (POST)
  - Update an existing item: `/<int:pk>/` (PUT)
  - Delete an item: `/<int:pk>/` (DELETE)

- **Stream Platforms:**
  - List all platforms: `/stream/` (GET)
  - Retrieve a specific platform: `/stream/<int:pk>/` (GET)
  - Create a new platform: `/stream/` (POST)
  - Update an existing platform: `/stream/<int:pk>/` (PUT)
  - Delete a platform: `/stream/<int:pk>/` (DELETE)

- **Reviews:**
  - List all reviews for a platform: `/stream/<int:pk>/review/` (GET)
  - Create a new review for a platform: `/stream/<int:pk>/review-create/` (POST)
  - Retrieve, update, or delete a review: `/stream/review/<int:pk>/` (GET, PUT, DELETE)

## Authentication

Some endpoints may require authentication. Make sure to include the necessary authentication headers in your requests.

