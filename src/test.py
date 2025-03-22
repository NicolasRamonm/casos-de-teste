import os
import pytest
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")

# Fixture para obter um ID de instituição para os testes
@pytest.fixture
def institution_id():
    """Fixture que retorna um ID de instituição para os testes"""
    url = f"{BASE_URL}/institutions"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            return data[0]['id']
    
    # Falhar o teste se não conseguir um ID
    pytest.skip("Não foi possível obter um ID de instituição para os testes")

def test_get_all_institutions():
    """Testa a listagem de todas as instituições"""
    
    url = f"{BASE_URL}/institutions"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Validações
    assert response.status_code == 200, f"Status code não é 200: {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Resposta não é uma lista"
    assert len(data) > 0, "Nenhuma instituição encontrada"
    
    # Validar a estrutura de cada instituição
    for institution in data:
        # Campos obrigatórios
        assert 'id' in institution, "Campo 'id' não encontrado na instituição"
        assert isinstance(institution['id'], int), "Campo 'id' não é um inteiro"
        
        assert 'name' in institution, "Campo 'name' não encontrado na instituição"
        assert isinstance(institution['name'], str), "Campo 'name' não é uma string"
        
        # Campo opcional
        if 'students_count' in institution:
            assert isinstance(institution['students_count'], int), "Campo 'students_count' não é um inteiro"
    
    # Não é necessário retornar nada em testes pytest

def test_get_institution_by_id(institution_id):
    """Testa a busca de uma instituição específica pelo ID"""
    
    url = f"{BASE_URL}/institutions/{institution_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Validações
    assert response.status_code == 200, f"Status code não é 200: {response.status_code}"
    institution = response.json()
    assert isinstance(institution, dict), "Resposta não é um objeto"
    
    # Validar a estrutura da instituição
    assert 'id' in institution, "Campo 'id' não encontrado na instituição"
    assert isinstance(institution['id'], int), "Campo 'id' não é um inteiro"
    
    assert 'name' in institution, "Campo 'name' não encontrado na instituição"
    assert isinstance(institution['name'], str), "Campo 'name' não é uma string"
    
    # Campo opcional
    if 'students_count' in institution:
        assert isinstance(institution['students_count'], int), "Campo 'students_count' não é um inteiro"

def test_get_institution_students(institution_id):
    """Testa a listagem de alunos de uma instituição específica"""
    
    url = f"{BASE_URL}/institutions/{institution_id}/students"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Validações
    assert response.status_code == 200, f"Status code não é 200: {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Resposta não é uma lista"

# Se você quiser executar manualmente sem o pytest
if __name__ == "__main__":
    print("Esse script é feito para ser executado com pytest.")
    print("Execute com: python -m pytest test.py -v")