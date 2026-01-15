
# 📦 Market Management – Backend API

API RESTful desenvolvida em **Python + Flask** para gerenciamento de marketplace, permitindo autenticação de sellers, gerenciamento de produtos, controle de estoque e registro de vendas, utilizando **JWT** para segurança e arquitetura em camadas.

---

## 🧠 Visão Geral

O **Market Management Backend** é responsável por fornecer serviços de autenticação, controle de vendedores (sellers), produtos e vendas, garantindo segurança, escalabilidade e organização do código seguindo boas práticas de desenvolvimento.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Flask**
* **Flask-JWT-Extended**
* **Flask-SQLAlchemy**
* **Flask-Bcrypt**
* **SQLite / PostgreSQL** (configurável)
* **JWT (JSON Web Token)**
* **Arquitetura em Camadas (Controller / Service / Model)**

---

## 🗂️ Arquitetura do Projeto

```
src/
├── Application/
│   ├── Controllers/
│   │   ├── auth_controller.py
│   │   ├── product_controller.py
│   │   ├── sale_controller.py
│   │   └── seller_controller.py
│   └── Service/
│       ├── seller_service.py
│       ├── product_service.py
│       └── sale_service.py
│
├── Infrastructure/
│   ├── Model/
│   │   ├── seller.py
│   │   ├── product.py
│   │   ├── sale.py
│   │   ├── sale_item.py
│   │   └── activation_code.py
│   └── http/
│       └── whats_app.py
│
├── routes/
│   ├── auth_routes.py
│   ├── product_routes.py
│   ├── sale_routes.py
│   ├── seller_routes.py
│   └── health_routes.py
│
├── config/
│   └── data_base.py
│
└── run.py
```

---

## 🔐 Autenticação & Segurança

* Autenticação baseada em **JWT**
* Token gerado no login do seller
* Rotas protegidas com `@jwt_required()`
* Controle de acesso por **seller_id** (multi-tenant)

---

## 🔑 Fluxo de Autenticação

1. Seller se cadastra
2. Recebe código de ativação via WhatsApp
3. Ativa a conta
4. Realiza login
5. Recebe token JWT
6. Acessa rotas protegidas

---

## 📌 Endpoints Principais

### 🔐 Autenticação

| Método | Rota              | Descrição                   |
| ------ | ----------------- | --------------------------- |
| POST   | `/api/auth/login` | Login do seller             |
| GET    | `/api/auth/me`    | Dados do seller autenticado |

---

### 🧑 Seller

| Método | Rota                    | Descrição        |
| ------ | ----------------------- | ---------------- |
| POST   | `/api/sellers`          | Criar seller     |
| POST   | `/api/sellers/activate` | Ativar seller    |
| PUT    | `/api/sellers/:id`      | Atualizar seller |
| DELETE | `/api/sellers/:id`      | Remover seller   |

---

### 📦 Produtos

| Método | Rota                | Descrição                 |
| ------ | ------------------- | ------------------------- |
| POST   | `/api/products`     | Criar produto             |
| GET    | `/api/products`     | Listar produtos do seller |
| GET    | `/api/products/:id` | Buscar produto por ID     |
| PUT    | `/api/products/:id` | Atualizar produto         |
| DELETE | `/api/products/:id` | Remover produto           |

---

### 🧾 Vendas

| Método | Rota         | Descrição     |
| ------ | ------------ | ------------- |
| POST   | `/api/sales` | Criar venda   |
| GET    | `/api/sales` | Listar vendas |

---

## 📤 Exemplo de Requisição (Login)

```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "seller@email.com",
  "senha": "123456"
}
```

### 📥 Resposta

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 🔄 Exemplo de Requisição Protegida

```http
GET /api/products
Authorization: Bearer SEU_TOKEN_AQUI
```

---

## 🧪 Validações e Regras de Negócio

* Seller precisa estar **ativo** para login
* Produtos pertencem exclusivamente ao seller autenticado
* Estoque não pode ser negativo
* Venda exige lista de itens válida
* Código de ativação é único e de uso único

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/market-management-backend.git
cd market-management-backend
```

### 2️⃣ Crie o ambiente virtual

```bash
python -m venv venv
```

### 3️⃣ Ative o ambiente

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 5️⃣ Execute a aplicação

```bash
python run.py
```

API disponível em:

```
http://localhost:5000
```

---

## 🚀 Próximas Melhorias

* Refresh Token
* Controle automático de estoque na venda
* Relatórios financeiros
* Testes automatizados (pytest)
* Deploy em nuvem (Render / Railway)

---

## 👩‍💻 Autora

**Bruna Ferreira**
Estudante de Análise e Desenvolvimento de Sistemas
Projeto acadêmico com foco em boas práticas, segurança e escalabilidade.

---