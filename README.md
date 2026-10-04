# redis task

A beginner-friendly DevOps project called **redis task** demonstrating a **multi-container application** using Docker Compose.

The application contains a frontend, Flask backend, and Redis database. Docker Compose manages all services, networking, dependencies, health checks, and persistent storage for the redis task project.

---

## 🚀 Project Overview

This redis task project demonstrates how multiple application services can work together using Docker Compose.

The application allows users to:

- View total tasks
- Add tasks
- Delete tasks
- Refresh the task count
- Store task data in Redis
- Keep Redis data persistent using a Docker volume

---

## 🏗️ Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │    Browser      │
                  │                 │
                  │ localhost:8082  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Frontend     │
                  │      Nginx      │
                  │                 │
                  │    Port 80      │
                  └────────┬────────┘
                           │
                           │ HTTP API
                           ▼
                  ┌─────────────────┐
                  │     Backend     │
                  │  Python Flask   │
                  │                 │
                  │    Port 5000    │
                  └────────┬────────┘
                           │
                           │ Redis connection
                           ▼
                  ┌─────────────────┐
                  │      Redis      │
                  │    Database     │
                  │                 │
                  │    Port 6379    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Docker Volume  │
                  │   redis-data    │
                  └─────────────────┘
```

---

## 🔄 Application Flow

```text
Browser
   ↓
Frontend / Nginx
   ↓
Flask Backend
   ↓
Redis
   ↓
Persistent Docker Volume
```

Docker Compose manages the complete application stack.

---

## 🐳 Containers

| Container       | Technology   | Purpose                   | Port        |
| --------------- | ------------ | ------------------------- | ----------- |
| `task-frontend` | Nginx        | Serves frontend           | 8082 → 80   |
| `task-backend`  | Python Flask | API and application logic | 5002 → 5000 |
| `task-redis`    | Redis        | Stores task count         | 6379        |

---

## 🛠️ Technologies Used

- Docker
- Docker Compose
- Python
- Flask
- Redis
- Nginx
- HTML
- JavaScript
- Linux
- Git
- GitHub

---

## 📁 Project Structure

```text
docker-compose-task-app/
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   └── index.html
│
└── docker-compose.yml
```

---

## ⚙️ Docker Compose Configuration

The `docker-compose.yml` file defines three services:

### Frontend

The frontend uses Nginx to serve the web application.

```yaml
frontend:
  build: ./frontend
  ports:
    - "8082:80"
```

### Backend

The backend runs the Flask application.

```yaml
backend:
  build: ./backend
  ports:
    - "5002:5000"
```

The backend receives the Redis hostname through an environment variable:

```yaml
environment:
  REDIS_HOST: redis
```

### Redis

Redis stores the task count.

```yaml
redis:
  image: redis:7-alpine
```

---

## 💾 Persistent Storage

Redis uses a Docker named volume:

```yaml
volumes:
  - redis-data:/data
```

This means Redis data can survive container recreation.

Example:

```text
Container
    ↓
Redis
    ↓
redis-data volume
```

The volume is intentionally **not removed** by:

```bash
docker compose down
```

---

## ❤️ Health Check

Redis has a health check:

```yaml
healthcheck:
  test: ["CMD", "redis-cli", "ping"]
  interval: 5s
  timeout: 3s
  retries: 5
```

The backend waits for Redis to become healthy:

```yaml
depends_on:
  redis:
    condition: service_healthy
```

This helps prevent the backend from starting before its database dependency is ready.

---

## 🌐 API Endpoints

### Home

```text
GET /
```

Returns:

```text
Docker Compose Task App is Running!
```

### Get Tasks

```text
GET /tasks
```

Example:

```json
{
  "tasks": 5,
  "message": "Tasks retrieved successfully"
}
```

### Add Task

```text
GET /add-task
```

Example:

```json
{
  "tasks": 6,
  "message": "Task added successfully"
}
```

### Delete Task

```text
GET /delete-task
```

Example:

```json
{
  "tasks": 5,
  "message": "Task deleted successfully"
}
```

### Health Check

```text
GET /health
```

Example:

```json
{
  "status": "healthy"
}
```

---

## 🚀 Run the Project

Clone the repository:

```bash
git clone https://github.com/maryamkhanum0632/docker-compose-task-app.git
```

Enter the project:

```bash
cd docker-compose-task-app
```

Start all services:

```bash
docker compose up -d --build
```

Check containers:

```bash
docker compose ps
```

Expected:

```text
task-frontend   Up
task-backend    Up
task-redis      Up (healthy)
```

---

## 🌐 Access the Application

Open the frontend:

```text
http://localhost:8082
```

Backend:

```text
http://localhost:5002
```

Health check:

```text
http://localhost:5002/health
```

---

## 🛑 Stop the Application

```bash
docker compose down
```

Start it again:

```bash
docker compose up -d
```

---

## 🔍 Useful Docker Compose Commands

Check running services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

View backend logs:

```bash
docker compose logs backend
```

View Redis logs:

```bash
docker compose logs redis
```

Rebuild services:

```bash
docker compose up -d --build
```

Stop containers:

```bash
docker compose down
```

---

## 🎯 DevOps Concepts Learned

This project helped me practice:

- Multi-container architecture
- Docker Compose
- Container networking
- Service discovery
- Environment variables
- Docker volumes
- Persistent data
- Redis
- Nginx
- Flask REST APIs
- Health checks
- Service dependencies
- Container lifecycle management
- Docker image building
- Git and GitHub

---

## 🌍 Real-World DevOps Architecture

A similar architecture can be extended in production:

```text
Users
  ↓
Load Balancer
  ↓
Frontend Containers
  ↓
Backend/API Containers
  ↓
Database / Cache
  ↓
Persistent Storage

        ↓

Monitoring
CI/CD
Logging
```

This project demonstrates the fundamental multi-container concepts used in larger DevOps environments.

---

## 📸 Screenshots

Add screenshots of:

1. Task Dashboard
2. Add Task functionality
3. Delete Task functionality
4. `docker compose ps`
5. Redis showing `healthy`
6. Docker Compose architecture

---

## 👩‍💻 Author

**Maryam Khanum**

DevOps Learner

**Skills practiced:**
Docker | Docker Compose | Linux | Git | GitHub | Python | Flask | Redis | Nginx | DevOps
