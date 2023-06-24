# Sistema de Gestão de Propostas de Empréstimo Pessoal

- [Requisitos](#Requisitos)
- [Bibliotecas](#Bibliotecas)
- [Ambientes](#Ambientes)
- [Clonando repositório](#Clonando-repositório)
- [Como buildar e upar o servidor](#Como-buildar-e-upar-o-servidor)
- [Acessando admin](#Acessando-admin)
- [Acessando página de empréstimos](#Acessando-pagina-de-emprestimos)
- [Broker(celery)](#Broker-celery)
- [Acessando admin](#Acessando-admin)
- [Documentação da API](#Documentação-da-API)
  - [Gerar uma nova proposta](#Gerar-uma-nova-proposta)
  - [Request](#Request)
  - [Response](#Response)
  - [Rota raiz](#Rota-raiz)
  - [Retorna todas as propostas](#Retorna-todas-as-propostas)
  - [Retorna uma proposta](#Retorna-uma-proposta)
- [Dúvidas](#Duvidas)

## [Requisitos](https://readme.so/pt/editor#Requisitos)

- docker
- docker-compose

## Bibliotecas

- django>=3.2.18
- psycopg2-binary>=2.9
- djangorestframework>=3.14
- markdown>=3.4
- django-filter>=22.1
- celery>=5.3.1
- django-celery-results>=2.5.1
- django-cors-headers>=4.1.0

## Ambientes

**Environment:** Docker, docker compose

**Backend:** Django, djangorestframework, celery

**Frontend:** React

**Database:** PostgresSQL

**Broker:** RabbitMQ

## Clonando repositório

Clone o projeto para sua máquina

```bash
  git clone https://link-para-o-projeto
```

Acesso o diretório do projeto

```bash
  cd my-project
```

## Como buildar e upar o servidor

Isso ira criar as imagens do backend e frontend, e criara os containers para cada serviço.

```
$ docker-compose up
```

ou

```
$ docker-compose up --build
```

## Acessando admin

Após a criação dos containers, para acessar o [**Admin**](`localhost:8000/admin`)(`localhost:8000/admin`).

**Usuário:** `admin`

**Senha:** `admin`

Incluido nas variáveis de ambiente `DJANGO_SUPERUSER_USERNAME` e `DJANGO_SUPERUSER_PASSWORD`

## Acessando página de empréstimos

Para acessar a aplicação [**Web**](`localhost:3000`)(`localhost:3000/`), preencha todos os campos, para receber as informações abaixo.

## Broker(celery)

Após a criação da propostas, ele envia o **ID** da proposta/cliente para a fila da função `approve_proposal` e executa todas as validações após 10 segundo.

```python
  def perform_create(self, serializer):
      proposal = serializer.save()
      approve_proposal.apply_async((proposal.id,), countdown=10)
```

## Documentação da API

### Gerar uma nova proposta

```http
  POST /api/customers
```

### Request

| Parâmetro                     | Tipo     | Descrição                                          |
| :---------------------------- | :------- | :------------------------------------------------- |
| (**Obrigatório**) `full_name` | `string` | Nome completo do cliente.                          |
| (**Obrigatório**) `cpf_cnpj`  | `number` | CPF ou CNPJ do cliente. (Number apenas para teste) |
| (**Obrigatório**) `address`   | `string` | Endereço completo                                  |
| (**Obrigatório**) `value`     | `number` | Valor do empréstimo.                               |

```json
{
  "full_name": "Funalo de Tal",
  "cpf_cnpj": "12345678910",
  "address": "Rua xxx, 123",
  "value": 15000
}
```

### Response

Adicionei alguns campos extras, apenas para deixar mais interativo.

| Parâmetro        | Tipo     | Descrição                                                               |
| :--------------- | :------- | :---------------------------------------------------------------------- |
| `full_name`      | `string` | Nome completo do cliente.                                               |
| `cpf_cnpj`       | `number` | CPF ou CNPJ do cliente. (Number apenas para teste)                      |
| `address`        | `string` | Endereço completo                                                       |
| `value`          | `number` | Valor do empréstimo.                                                    |
| `approved_value` | `number` | Valor do empréstimo aprovado, baseado no score.                         |
| `status`         | `string` | Status da proposta. `Em analise`, `Aprovado parcialmente` ou `Aprovado` |
| `score`          | `number` | Numério gerado automaticamente.                                         |
| `updated_at`     | `date`   | Ultima atualização.                                                     |
| `created_at`     | `date`   | Data de criação.                                                        |

```json
{
  "id": "c7426ed1-ff4b-4bde-b547-cd1e4d0a99ad",
  "full_name": "Funalo de Tal",
  "cpf_cnpj": "12345678910",
  "address": "Rua xxx, 123",
  "value": "15000.00",
  "approved_value": "0.00",
  "status": "Em analise",
  "score": 424,
  "updated_at": "2023-06-24T08:52:41.228920-03:00",
  "created_at": "2023-06-24T08:52:41.228894-03:00"
}
```

### Rota raiz

_OBS.:_ Basta adicionar o cookie de sessão do admin, para fazer requisições nos demais endpoints, exceto **POST**, ou acessando a path raiz do **DRF** para exibir todos os _endpoints_.

```http
  GET /api
```

### Retorna todas as propostas

```http
  GET /api/customers
```

| Cookie                        | Tipo     | Descrição                     |
| :---------------------------- | :------- | :---------------------------- |
| (**Obrigatório**) `sessionid` | `string` | Cookie de autorização da API. |

### Retorna uma proposta

```http
  GET /api/customers/${id}
```

| Parâmetro              | Tipo     | Descrição                       |
| :--------------------- | :------- | :------------------------------ |
| (**Obrigatório**) `id` | `string` | O ID da proposta que você quer. |

| Cookie                        | Tipo     | Descrição                     |
| :---------------------------- | :------- | :---------------------------- |
| (**Obrigatório**) `sessionid` | `string` | Cookie de autorização da API. |

## Dúvidas

Qualquer duvidas ou problemas para executar a aplicação, entrar em contato leonardo.ventura@outlook.com
