# from .config import Config
# from flask_mongoengine import MongoEngine
from celery import Celery
from flask import Flask

app = Flask(__name__)
cel_app = Celery('tasks',
                 broker='amqp://user:pass@rabbit:5672',
                 backend='mongodb://mongodb:27017/backdb')


