import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manipulador de Dados", page_icon=":bar_chart:", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0px;'>Manipulador de Dados</h1>
    <p style='text-align: right; margin-top: 4px; opacity: 0.5;'>
    versão 1.0.0<br>
    desenvolvido por <a href="https://www.linkedin.com/in/murilo-moreno-almeida-da-silva-ornelas-54885b29b/" target="_blank">Murilo Moreno</a>
    </p>

    <br>
    <p>Bem-vindo ao <strong>Manipulador de Dados</strong>!</p>
    <p>Esta aplicação permite que você carregue um arquivo CSV ou Excel, visualize os dados e faça manipulações básicas.</p>

    <h2 style='text-align: center;'>Como usar:</h2>

    <ol>
        <li>Clique no botão abaixo para selecionar um arquivo CSV ou Excel do seu computador.</li>
        <li>Após o upload, os dados serão exibidos em uma tabela interativa.</li>
    </ol>

    <br>

    <p><strong>Você pode:</strong></p>

    <ul>
        <li>Explorar e manipular dados</li>
        <li>Tratar dados em branco</li>
        <li>Remover duplicatas</li>
        <li>Exportar resultados</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

archive = st.file_uploader("Carregue sua Tabela", type=["csv", "xlsx"])

if archive is not None:
    if archive.name.endswith(".csv"):
        df = pd.read_csv(archive, sep=None, engine="python")
        if "Unnamed: 0" in df.columns:
            df.drop("Unnamed: 0", axis=1, inplace=True)
    else:
        df = pd.read_excel(archive)

    if "dataframe" in st.session_state:
        del st.session_state["dataframe"]
    if "dataframe_original" in st.session_state:
        del st.session_state["dataframe_original"]

    st.session_state["dataframe"] = df
    st.session_state["dataframe_original"] = df.copy()

if st.session_state.get("dataframe") is not None:
    st.success("✅ Arquivo já carregado!")