# 📧 Email AI

EmailIA é uma aplicação web que utiliza **Inteligência Artificial** para auxiliar na **geração e aprimoramento de emails** de forma rápida, clara e profissional.

O projeto é dividido em **frontend (Vue + Vite)** e **backend (FastAPI)**, com arquitetura desacoplada e pronta para deploy em nuvem.

---

## 🚀 Funcionalidades

* ✨ Geração automática de emails com IA
* 🎯 Ajuste de tom (formal, informal, profissional, etc.)
* 🧠 Integração com API de IA
* 🖥️ Interface moderna e responsiva
* 📡 Backend REST com documentação Swagger

---

## 🧱 Tecnologias Utilizadas

### Frontend

* Vue 3
* Vite
* HTML5
* CSS3
* Fontes Google (Montserrat)

### Backend

* Python 3.10+
* FastAPI
* Uvicorn
* Python-dotenv
* API de IA (via variável de ambiente)

### Deploy

* Backend: **Render**
* Frontend: **Vercel / Netlify**

---

## 📂 Estrutura do Projeto

```bash
EMAILIA/
│
├── back-end/
│   ├── app/
│   │   ├── services/
│   │   │   └── email_service.py
│   │   ├── utils/
│   │   │   └── openai_client.py
│   │   └── main.py
│   └── requirements.txt
│
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── icons/
│   │   ├── EmailForm.vue
│   │   ├── EmailForm.html
│   │   └── EmailForm.css
│   ├── App.vue
│   └── main.js
│
├── index.html
├── package.json
├── vite.config.js
└── README.md
```

---

## ⚙️ Configuração do Backend (Local)

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Variáveis de ambiente

Crie um arquivo `.env` dentro da pasta `back-end`:

```env
OPENAI_API_KEY=sua_chave_aqui
```

### 4️⃣ Rodar o servidor

```bash
uvicorn app.main:app --reload
```

Acesse:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ☁️ Deploy do Backend no Render

* Root Directory: `back-end`
* Build Command:

```bash
pip install -r requirements.txt
```

* Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

* Variável de ambiente:

```
OPENAI_API_KEY
```

---

## 🎨 Configuração do Frontend

### 1️⃣ Instalar dependências

```bash
npm install
```

### 2️⃣ Variável de ambiente

```env
VITE_API_URL=https://sua-api-n
```
