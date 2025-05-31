# EscolaDjango

Um projeto de sistema de gerenciamento escolar desenvolvido com Django REST Framework, onde é possível cadastrar alunos, cursos e matrículas de alunos em cursos.

![Static Badge](https://img.shields.io/badge/3.12.4-fcce4e?logo=python&label=python)
![Static Badge](https://img.shields.io/badge/5.1-0C4B33?label=django) 
![PyPI - Version](https://img.shields.io/pypi/v/djangorestframework?label=rest%20framework&color=A30000)

## Tecnologias Utilizadas

* 💻 **Python:** Linguagem de programação principal.
* 🌐 **Django:** Framework web de alto nível para desenvolvimento rápido e design pragmático e limpo.
* 🚀 **Django REST Framework:** Toolkit poderoso e flexível para construir APIs web.
* 🗄️ **SQLite3:** Banco de dados leve e de código aberto (utilizado em desenvolvimento).
* 🐳 **Docker/Docker Compose:** Utilizado para orquestração e conteinerização do ambiente de desenvolvimento e produção do [frontend](https://github.com/Rolig4n/3697-django-frontend).
* ☁️ **AWS EC2:** Para hospedagem da aplicação em ambiente de produção.

## Deploy do Projeto

O projeto está atualmente em deploy na AWS. Abaixo estão algumas informações importantes sobre o deploy:

* **Instância:** AWS EC2 (Ubuntu Server)

## Link do Projeto na AWS

Você pode acessar a aplicação em produção através do [link](http://18.217.233.248:8000)

Caso não carregue o instancia esta inativa para evitar custos supresas. Aqui esta uma previa da aplicação rodando:

<img src="hiago.gif" height="250"/>


**Observação:** O link aponta para o endpoint da API. Para interagir, você pode usar ferramentas como Postman, Insomnia ou a interface navegável do Django REST Framework. Tambem é nec

## Funcionalidades Disponíveis

O sistema oferece as seguintes funcionalidades através de sua API:

* **Alunos:**
    * Cadastrar novos alunos.
    * Listar todos os alunos cadastrados.
    * Visualizar detalhes de um aluno específico.
    * Atualizar informações de um aluno existente.
    * Deletar um aluno.
* **Cursos:**
    * Cadastrar novos cursos.
    * Listar todos os cursos disponíveis.
    * Visualizar detalhes de um curso específico.
    * Atualizar informações de um curso existente.
    * Deletar um curso.
* **Matrículas:**
    * Matricular um aluno em um curso.
    * Listar todas as matrículas.
    * Visualizar detalhes de uma matrícula específica.
    * Atualizar informações de uma matrícula (ex: status, período).
    * Deletar uma matrícula.
    * Listar cursos matriculados por um aluno específico.
    * Listar alunos matriculados em um curso específico.

Tudo documentado, tanto com [swagger](http://18.217.233.248:8000/swagger) ou [redoc](http://18.217.233.248:8000/redoc)

Alem da implementação de testes, unitários e de integração. Basta executar o comando a baixo

```
python manage.py test
```

## Repositório no GitHub

O código fonte completo deste projeto está disponível no GitHub:

[API - EscolaDjango](https://github.com/Rolig4n/EscolaDjango)

[Frontend - EscolaDjango](https://github.com/Rolig4n/3697-django-frontend)