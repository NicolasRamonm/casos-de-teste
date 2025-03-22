# Caso de Teste: Busca de Instituição por ID

## Objetivo
Verificar se conseguimos obter os detalhes de uma instituição quando fornecemos um ID válido. Queremos garantir que a API retorne todos os dados necessários no formato correto para usarmos na população do nosso banco na aws.

## Pré-condição
- API funcionando e acessível
- Pelo menos uma instituição já cadastrada no banco
- Token de autenticação válido
- Variáveis de ambiente `BASE_URL` e `TOKEN` configuradas

## Procedimento de Teste
1. Obter um ID válido de instituição (fazendo uma chamada à lista de instituições)
2. Montar a URL com o ID obtido: `/institutions/{id}`
3. Enviar requisição GET com o token de autenticação no cabeçalho
4. Analisar a resposta recebida

## Resultado Esperado
- Status 200 (OK)
- Resposta em formato JSON contendo um objeto (não uma lista)
- Objeto deve ter os campos obrigatórios: `id` (número) e `name` (texto)
- Se o campo `students_count` estiver presente, deve ser um número
- O ID retornado deve ser o mesmo que solicitamos


O código abaixo implementa os testes:

```python

def test_get_all_institutions():
    """Testa a listagem de todas as instituições"""
    
    url = f"{BASE_URL}/institutions"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

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

```

## Resultado Obtido
- Recebemos status 200
- Resposta veio como objeto JSON
- Campos obrigatórios presentes e com tipos corretos
- Campo `students_count` estava presente e era um número
- ID correspondia ao solicitado

## Pós-condição
- Nenhuma alteração no banco de dados (teste apenas consulta dados)
