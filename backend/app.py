from flask import Flask, jsonify
from flask_cors import CORS
import redis
import os

app = Flask(__name__)
CORS(app)

redis_host = os.getenv("REDIS_HOST", "localhost")

r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)


@app.route("/")
def home():
    return "Docker Compose Task App is Running!"


@app.route("/tasks")
def tasks():
    task_count = r.get("task_count")

    if task_count is None:
        task_count = 0

    return jsonify({
        "tasks": int(task_count),
        "message": "Tasks retrieved successfully"
    })


@app.route("/add-task")
def add_task():
    count = r.incr("task_count")

    return jsonify({
        "tasks": count,
        "message": "Task added successfully"
    })


@app.route("/delete-task")
def delete_task():
    current_count = r.get("task_count")

    if current_count is None or int(current_count) <= 0:
        return jsonify({
            "tasks": 0,
            "message": "No tasks available"
        })

    count = r.decr("task_count")

    return jsonify({
        "tasks": count,
        "message": "Task deleted successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
