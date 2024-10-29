# FastAPI Application

A FastAPI-based application designed for high-performance web APIs.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:Morvin-Ian/fastapi.git
   cd fastapi

2. **Environment Variables:**
   - Create a `.env` file in the root directory with the following variables:
     ```plaintext
     DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>:<port>/<database>
     ```
   - Replace `<user>`, `<password>`, `<host>`, `<port>`, and `<database>` with your PostgreSQL credentials.

3. **Build and Run the Application:**

   - Using Docker Compose:
     ```bash
     docker-compose build
     docker-compose up
     ```

   - Alternatively, with Makefile commands:
     ```bash
     make build
     make up
     ```

4. **Accessing the Application:**
   - Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the application.
   - Swagger documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs) for testing API endpoints.

## Features

- **Asynchronous Database Operations** using SQLAlchemy with PostgreSQL.
- **Automatic Interactive Documentation** with Swagger UI and Redoc.
- **Environment Configuration** for secure database management.

## Additional Commands

- **Run Tests:**
  ```bash
  make test
