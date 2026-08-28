import pytest
import importlib

# Importa el archivo de tu aplicación sample_app.py o aplicación_de_muestra.py
try:
    app_module = importlib.import_module("sample_app")
except ImportError:
    app_module = importlib.import_module("aplicación_de_muestra")

app = app_module.app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 500