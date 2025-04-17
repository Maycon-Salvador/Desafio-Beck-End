# Kartado - Desafio Backend

## Objetivo

Criar um novo endpoint na API Django para o modelo `Occurrence`, seguindo o padrão de resposta especificado pela Kartado.

---

## Tecnologias Utilizadas

- Python 3.11
- Django
- Django Rest Framework
- SQLite (banco local)
- Git e GitHub

---

## Implementações Realizadas

- Criação do serializer `OccurrenceSerializer` com campos extras `road_name` e `status_name`.
- Utilização de `HyperlinkedModelSerializer` para exibir `road` e `status` como links.
- Criação do `OccurrenceViewSet` com `ModelViewSet`.
- Registro da rota `/occurrences/` em `urls.py` usando o `DefaultRouter`.
- Resposta no formato esperado, com paginação e campos relacionados.

---

## Autenticação

- Endpoint protegido por autenticação básica (Django Rest Framework).
- Usuário de teste disponível:
  - **usuário**: `desafio`
  - **senha**: `desafio`

---

## Como executar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/Maycon-Salvador/Desafio-Beck-End

# Acesse a pasta do projeto
cd Desafio-Beck-End

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python manage.py runserver
```

---

## Endpoint criado

`GET /occurrences/` → lista paginada de ocorrências com os seguintes campos:

```json
{
  "description": "Texto...",
  "road": "http://localhost:8000/roads/1/",
  "road_name": "BR-101",
  "km": "65",
  "status": "http://localhost:8000/status/1/",
  "status_name": "Para fazer",
  "created_at": "2021-01-20",
  "updated_at": "2021-01-20"
}
```

---

## Autor

Desenvolvido por Maycon Salvador – desafio técnico Kartado
