import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

def logging_setup(app: Flask):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(
        'logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    
def create_app():
    app = Flask("app",template_folder="client/templates")
    logging_setup(app)
    from client.routes import bp
    app.register_blueprint(bp)
    return app



