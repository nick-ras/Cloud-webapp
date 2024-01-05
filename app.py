import sys
import unittest
from src import create_app

#instance
app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
