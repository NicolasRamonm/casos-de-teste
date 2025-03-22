# Caso de Teste: Busca de Instituição por ID

## Identificação
**ID:** TC-INST-002  
**Nome:** Busca de instituição por ID  
**Módulo:** API de Instituições  

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

```

## Resultado Obtido
- Recebemos status 200
- Resposta veio como objeto JSON
- Campos obrigatórios presentes e com tipos corretos
- Campo `students_count` estava presente e era um número
- ID correspondia ao solicitado

## Pós-condição
- Nenhuma alteração no banco de dados (teste apenas consulta dados)
