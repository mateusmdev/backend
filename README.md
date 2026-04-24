[English](README.md) | [Portuguese](README.pt-br.md)

# Project Technical Documentation - Movie API

This documentation provides a detailed overview of the Movie API, a movie management system developed as part of a technical challenge for Wattio. The system allows performing CRUD (Create, Read, Update, Delete) operations on a movie database.

---

## 1. Project Overview
The **Movie API** is a backend application designed to manage a movie catalog. The primary goal is to provide a RESTful interface so that users can register, list, and remove movies, ensuring data persistence and a scalable, organized architecture.

### Key Features:
- Listing of all registered movies.
- Detailed search for a movie by ID.
- Registration of new movies (Name, Genre, Duration, and Rating).
- Deletion of existing movies.
- Centralized error handling.

---

## 2. Architecture and Structure
The project adopts a **Layered Architecture**, which facilitates maintenance, testing, and separation of concerns.

### Folder Organization:
```text
C:\Users\User\Documents\Mateus\Programação\projetos\Github\python\backend\
├── main.py                # Application entry point
├── controller/            # Control layer (request orchestration)
├── service/               # Business logic layer
├── repository/            # Data access layer (Persistence)
├── model/                 # Database models and validation schemas (Pydantic)
├── database/              # Database connection configurations
├── router/                # Definition of routes and endpoints
└── docker-compose.yml     # Container configuration
```

### Role of each directory:
- **`router/`**: Defines API paths and directs requests to controllers.
- **`controller/`**: Receives data from the route, validates resource existence, and calls the necessary services.
- **`service/`**: Contains the core business logic, filtering or processing data before passing it to the repository.
- **`repository/`**: Abstract database operations (SQLAlchemy), isolating persistence logic.
- **`model/`**: Defines data structures for both the database (`movie_model.py`) and API input/output (`movie_schema.py`).
- **`database/`**: Configures the SQLite engine and the SQLAlchemy session.

---

## 3. Application Flow
Data flow follows a unidirectional line to ensure consistency:

1. **Request**: The client makes an HTTP call (e.g., `GET /filmes/`).
2. **Router**: `movie_router.py` identifies the endpoint and injects the `MovieController` dependency.
3. **Controller**: `MovieController` triggers the `MovieService`.
4. **Service**: `MovieService` requests data from the `MovieRepository`.
5. **Repository**: `MovieRepository` executes the query via SQLAlchemy on the `movies.db` database.
6. **Response**: The data returns through the same path, being validated by `MovieSchema` before reaching the client.

---

## 4. Technologies Used
- **Language**: Python 3.11.
- **Web Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Performance and auto-generated documentation).
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Object-Relational Mapping).
- **Data Validation**: [Pydantic](https://docs.pydantic.dev/) (Schemas and typing).
- **Database**: SQLite (Lightweight and no external server required).
- **ASGI Server**: Uvicorn.
- **Containerization**: Docker and Docker Compose.

---

## 5. Prerequisites
Before starting, ensure you have installed:
- **Python 3.11** or higher.
- **Pip** (Python package manager).
- **Docker** and **Docker Compose** (Optional, for containerized execution).

---

## 6. Installation and Execution (Pure Python)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd backend
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## 7. Installation and Execution (Docker)

The project is configured for quick startup using Docker Compose.

### Commands:
```bash
# To start the container
docker-compose up --build

# To run in the background
docker-compose up -d
```

- **Port**: The API will be exposed on port `8000`.
- **Volumes**: Local code is mapped into the container, allowing real-time updates (hot reload).

---

## 8. Project Configuration
- **Database**: The `movies.db` file is automatically created in the project root on the first run.
- **CORS**: The application is configured to accept requests from `localhost` and `localhost:8080` (adjustable in `main.py`).
- **Environment Variables**: Uses `PYTHONUNBUFFERED=1` to ensure logs are displayed immediately in the console.

---

## 9. Module Detailing

### `repository/movie_repository.py`
Manages the active database connection. An important detail is that the `create` and `delete` functions return the updated list of all movies, facilitating state updates in the frontend.

### `controller/movie_controller.py`
Implements HTTP error handling. If a requested movie by ID does not exist, the controller raises an `HTTPException` with status 404.

### `main.py`
Features a global `exception_handler` that captures any unexpected system errors and returns a user-friendly "Custom internal error" message, preventing stacktrace leaks to the end-user.

---

## 10. API Endpoints

### Movies
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/filmes/` | Returns a list of all movies. |
| **GET** | `/filmes/{id}/` | Returns details of a specific movie. |
| **POST** | `/filmes/` | Registers a new movie. |
| **DELETE** | `/filmes/{id}/` | Removes a movie from the system. |

#### Payload Example (POST):
```json
{
  "name": "Interstellar",
  "genre": "Sci-Fi",
  "duration": 169,
  "rate": 8.7
}
```

---

## 11. Best Practices and Conventions
- **Dependency Injection**: Extensive use of FastAPI's `Depends` to manage class instances.
- **Type Hinting**: The entire project uses static typing in Python for better clarity and bug reduction.
- **DRY (Don't Repeat Yourself)**: Database logic isolated in repositories.
- **Surgical Updates**: The database is automatically initialized via `Base.metadata.create_all` in the repository.

---

## 12. Possible Improvements
1. **Pagination**: Add pagination to the `GET /filmes/` endpoint to handle large volumes of data.
2. **Automated Testing**: Implement unit tests with `pytest` and integration tests for routes.
3. **Logging**: Implement a structured logging system for production monitoring.
4. **Migrations**: Use `Alembic` to manage database schema changes instead of `create_all`.
5. **Authentication**: Add protection to write routes (POST/DELETE) using JWT.

---
Documentation generated for development support and onboarding.
