# celery_config.py
# Configuration for define celery tasks in a separate file.
import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv() # to load environment variables

celery_app = Celery(__name__, broker=os.getenv("CELERY_BROKER_URL"), backend=os.getenv("CELERY_RESULT_BACKEND"))

celery_app.conf.update(
    imports=['app.tasks.celery_tasks'], # path to your celery tasks file
    broker_connection_retry_on_startup=True,
    task_track_started=True
)