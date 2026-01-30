<script setup>
import { ref } from "vue";
import "./EmailForm.css"; 

const emailText = ref("");
const file = ref(null);
const loading = ref(false);
const result = ref(null);
const error = ref("");

const API_URL = import.meta.env.VITE_API_URL;

const handleFileUpload = (e) => {
  file.value = e.target.files[0];
};

const submitEmail = async () => {
  error.value = "";
  result.value = null;

  if (!emailText.value && !file.value) {
    error.value = "Informe um texto ou envie um arquivo.";
    return;
  }

  loading.value = true;

  const formData = new FormData();
  if (emailText.value) formData.append("text", emailText.value);
  if (file.value) formData.append("file", file.value);

  try {
    const res = await fetch(`${API_URL}/process-email`, {
      method: "POST",
      body: formData,
    });

    if (!res.ok) throw new Error();

    result.value = await res.json();
  } catch {
    error.value = "Erro ao processar o email.";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div>
    <nav class="navbar">
      <div class="nav-content">
        <span class="logo">📧 Email AI</span>
        <span class="nav-subtitle">Classificação inteligente de emails</span>
      </div>
    </nav>
  </div>
  <div class="container">
    <div class="card">

      <header class="header">
        <h1>📧 Email AI</h1>
        <p class="subtitle">
          Classifique emails automaticamente e receba uma resposta sugerida
        </p>
      </header>

      <section class="input-section">
        <label for="emailText">Conteúdo do email</label>
        <textarea
          id="emailText"
          v-model="emailText"
          placeholder="Cole aqui o conteúdo do email..."
          rows="6"
        />
      </section>

      
      <section class="upload-section">
        <label for="fileUpload">Ou envie um arquivo (.txt ou .pdf)</label>
        <input
          id="fileUpload"
          type="file"
          accept=".txt,.pdf"
          @change="handleFileUpload"
        />
      </section>

      
      <section class="actions">
        <button
          class="primary-button"
          @click="submitEmail"
          :disabled="loading"
        >
          {{ loading ? "Processando..." : "Processar Email" }}
        </button>
      </section>

      <p v-if="error" class="error">
        {{ error }}
      </p>

      <section v-if="result" class="result">
        <div
          class="badge"
          :class="result.categoria === 'Produtivo'
            ? 'produtivo'
            : 'improdutivo'"
        >
          {{ result.categoria }}
        </div>

        <h3>Resposta sugerida</h3>
        <p class="response">
          {{ result.resposta }}
        </p>
      </section>
    </div>
  </div>
</template>

