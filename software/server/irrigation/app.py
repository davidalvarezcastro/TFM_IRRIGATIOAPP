from api.api import app
from settings import API_HOST, API_PORT

if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)
