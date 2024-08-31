# tasks.py
from celery import shared_task
import time

@shared_task
def process_user_request():
    data = "data"
    # Simulate a long-running task (e.g., processing data, sending emails)
    print(f"Task Started with data: {data}")
    time.sleep(10)  # Delay to simulate work
    return f"Task completed with data: {data}"