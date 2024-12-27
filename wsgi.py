from flask import Flask
from client import create_app


app: Flask = create_app()

if __name__ == "__main__":
    app.run(host = "localhost", port=50051, debug=True)