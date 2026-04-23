````markdown
# 📊 Manipulador de Dados

<p align="center">
  <img src="assets/capa.png" alt="Capa do projeto" width="800"/>
</p>

<h3 align="center">
Aplicação interativa para tratamento de dados com Python
</h3>

<p align="center">
  <strong>Upload • Visualização • Limpeza • Exportação</strong>
</p>

---

## 🚀 Funcionalidades

- 📂 Upload de arquivos `.csv` e `.xlsx`  
- 👀 Visualização interativa do DataFrame  
- 📊 Resumo automático:
  - número de linhas e colunas  
  - valores nulos  
  - duplicatas  
  - tipos de dados  

- 🧹 Tratamento de dados:
  - Remoção de duplicados  
  - Remoção de valores nulos  
  - Preenchimento de nulos:
    - numéricos → média  
    - não numéricos → moda  
  - Remoção de linhas por índice  
  - 🔄 Reset do dataset  

- 💾 Exportação:
  - CSV  
  - Excel  

---

## 🧠 Objetivo

Ferramenta simples para manipulação de dados, inspirada em ferramentas como Power BI, com foco em:

- prática com pandas  
- construção de aplicações com Streamlit  
- análise rápida de datasets  

---

## 🛠️ Tecnologias

- Python  
- Streamlit  
- pandas  

---

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
````

```bash
python -m venv .venv
```

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

```bash
streamlit run app.py
```

---

## 📁 Estrutura

```
📦 projeto
 ┣ 📜 app.py
 ┣ 📂 pages
 ┃ ┗ 📜 Tratativas_dos_Dados.py
 ┣ 📜 requirements.txt
 ┗ 📂 assets
    ┗ 📜 capa.png
```

---

## ⚠️ Observações

* Dados processados apenas em memória
* Nenhum arquivo salvo no servidor
* Indicado para uso local com dados sensíveis

---

## 🔮 Roadmap

* 🤖 Integração com IA (LLM)
* 📈 Correlação e insights automáticos
* 🧾 Histórico de alterações
* 🌐 Deploy compartilhado

---

## 👨‍💻 Autor

**Murilo Moreno**
[LinkedIn](https://www.linkedin.com/in/murilo-moreno-almeida-da-silva-ornelas-54885b29b/)

```
```
