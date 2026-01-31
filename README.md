# 📧 EmailIA

EmailIA é uma aplicação web que utiliza **Inteligência Artificial** para **analisar emails automaticamente**, **classificá-los como Produtivos ou Improdutivos** e **gerar respostas profissionais sugeridas**, auxiliando equipes a lidar com grandes volumes de mensagens de forma eficiente.

O projeto foi desenvolvido com **frontend e backend desacoplados**, simulando um cenário real de produto corporativo, com deploy em nuvem e integração com um provedor externo de modelos de linguagem.

---

## 🚀 Funcionalidades

* 📩 Análise semântica do conteúdo de emails
* 🧠 Classificação automática em:

  * **Produtivo** (requer ação, resposta ou acompanhamento)
  * **Improdutivo** (não requer ação imediata)
* ✍️ Geração automática de respostas profissionais
* 📎 Suporte a texto digitado e upload de arquivos (.txt e .pdf)
* 🌐 API REST documentada com Swagger

---

## 🧱 Arquitetura da Solução

```
Frontend (Vue 3)
        ↓
Backend (FastAPI)
        ↓
OpenRouter API
        ↓
Modelo de Linguagem (LLM)
```

A aplicação utiliza o **OpenRouter** como provedor de IA, permitindo acesso a diferentes modelos de linguagem de forma flexível, sem dependência de um único fornecedor.

---

## 🧠 Inteligência Artificial

### Provedor de IA

* **OpenRouter** ([https://openrouter.ai](https://openrouter.ai))

### Modelo Utilizado

* `mistralai/mistral-7b-instruct`

### Estratégia

* Uma única chamada ao modelo realiza:

  * a **classificação semântica** do email (Produtivo ou Improdutivo)
  * a **geração da resposta automática**

O backend controla o formato da resposta, garantindo que a IA **não retorne JSON**, apenas texto estruturado, aumentando a robustez da aplicação.

---

## 🛠️ Tecnologias Utilizadas

### Frontend

* Vue 3
* Vite
* HTML5
* CSS3
* Google Fonts (Montserrat)

### Backend

* Python 3
* FastAPI
* Uvicorn
* Requests
* PyPDF2

### Infraestrutura

* Backend: **Render**
* Frontend: **Vercel**
* IA: **OpenRouter API**

---

## ⚙️ Configuração do Backend (Local)

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2️⃣ Instalar dependências

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Variáveis de ambiente

Crie um arquivo `.env` na pasta `back-end`:

```env
OPENROUTER_API_KEY=sua_chave_openrouter
```

### 4️⃣ Rodar o servidor

```bash
python -m uvicorn app.main:app --reload
```

Acesse:

```
http://localhost:8000/docs
```

---

## ☁️ Deploy do Backend (Render)

* **Root Directory:** `back-end`
* **Build Command:**

```bash
pip install -r requirements.txt
```

* **Start Command:**

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

* **Environment Variables:**

```
OPENROUTER_API_KEY
```

---

## 🎨 Configuração do Frontend

### Variável de ambiente

```env
VITE_API_URL=https://sua-api-no-render.onrender.com
```

### Rodar localmente

```bash
npm install
npm run dev
```

---

## 📡 Integração Frontend ↔ Backend

O frontend envia o conteúdo do email via `multipart/form-data` para o endpoint:

```
POST /process-email
```

Resposta esperada:

```json
{
  "categoria": "Produtivo",
  "resposta": "Texto gerado automaticamente pela IA"
}
```

---

## 🧪 Exemplos de Teste

### Email Produtivo

```
Olá, estou com erro no sistema e preciso de ajuda.
```

### Email Improdutivo

```
Obrigado pelo excelente atendimento!
```

---
## 🔗 Acesso à Aplicação

O frontend da aplicação está disponível online via **Vercel**:

🌐 **EmailIA – Aplicação Web**  
👉 https://email-ai-fawn.vercel.app/

> ⚠️ Observação: a aplicação depende do backend hospedado no Render. Em casos de inatividade prolongada, o primeiro acesso pode levar alguns segundos até o serviço iniciar.


## 👩‍💻 Autoria

Projeto desenvolvido por **Laura Ferreira**
Estudante de Ciência da Computação

---

## 📝 Licença

Projeto desenvolvido para fins educacionais e de portfólio.
