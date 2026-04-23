import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Tratativas de Dados", page_icon=":bar_chart:", layout="centered")

df = st.session_state.get("dataframe")

if df is not None:
    st.markdown(
        """
        <h1 style='text-align: center;'>Tratativas de Dados</h1>

        <p>Agora que você carregou seu arquivo, é hora de tratar os dados!</p>
        <p>Esta seção permite que você faça manipulações básicas nos seus dados, como:</p>

        <ul>
            <li>Tratar dados em branco</li>
            <li>Remover duplicatas</li>
            <li>Exportar resultados</li>
        </ul>

        <br>

        <h3 style='text-align: center;'>Seu Dataframe</h3>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(df)
    
    total_nas = df.isna().sum().sum()
    

    if total_nas == 0:
        color = "lightgreen"
    else:
        color = "red"
    
    st.markdown(
        f"""
        <p style='margin-bottom:0px;'>Número de linhas: <strong>{df.shape[0]}</strong></p>
        <p>Número de colunas: <strong>{df.shape[1]}</strong></p><br>
        <p style= margin-bottom:0px;'>Valores duplicados: <strong>{df.duplicated().sum()}</strong></p>
        <p style='color: {color};'>Valores faltantes: <strong>{total_nas}</strong></p>
        
        <h3 style='text-align: center;'>Tipos de dados</h3>
        """,
    unsafe_allow_html=True
    )
    
    tipos_df = df.dtypes.reset_index()
    tipos_df.columns = ["Coluna", "Tipo"]

    nulos_df = df.isna().sum().reset_index()
    nulos_df.columns = ["Coluna", "Nulos"]
    
    tab1, tab2 = st.tabs(["Tipos de Dados", "Valores Faltantes"])

    with tab1:
        st.dataframe(tipos_df, hide_index=True)

    with tab2:
        st.dataframe(nulos_df, hide_index=True)
        
    
    if df.empty:
        st.warning("O dataframe está vazio.")
    else:    
        option = st.selectbox(
        "O que deseja fazer?",
        [
            "Remover duplicados",
            "Remover nulos",
            "Preencher nulos (numéricos)",
            "Preencher nulos (não numéricos)",
            "Remover linhas por índice",
            "Redefinir dataframe"
        ]
        )

        if option == "Remover linhas por índice":
            min_idx = int(df.index.min())
            max_idx = int(df.index.max())

            range_idx = st.slider(
                "Selecione o intervalo de índices para remover",
                min_value=min_idx,
                max_value=max_idx,
                value=(min_idx, max_idx)
            )

        if st.button("Executar", help="Clique duas vezes para confirmar (segurança)"):

            if option == "Remover duplicados":
                df = df.drop_duplicates()

            elif option == "Remover nulos":
                df = df.dropna()
            
            elif option == "Preencher nulos (numéricos)":
                num_cols = df.select_dtypes(include="number").columns
                df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
            
            elif option == "Preencher nulos (não numéricos)":
                for col in df.columns:
                    if not pd.api.types.is_numeric_dtype(df[col]):
                        
                        df[col] = df[col].replace(r"^\s*$", pd.NA, regex=True)
                        
                        moda = df[col].mode()
                        
                        if not moda.empty:
                            df[col] = df[col].fillna(moda[0])

            elif option == "Remover linhas por índice":
                inicio, fim = range_idx
                idx_para_remover = df.index[(df.index >= inicio) & (df.index <= fim)]
                df = df.drop(idx_para_remover)
            
            elif option == "Redefinir dataframe":
                df = st.session_state["dataframe_original"].copy()

            st.session_state["dataframe"] = df

    if df is None or df.empty:
        st.warning("Nenhum dado disponível para exportação.")
    else:
        st.markdown(f"""
                    <h3 style='text-align: center; margin-top: 150px;'>Exportação do Dataframe</h3>
                    """, unsafe_allow_html=True)

        nome_arquivo = st.text_input("Nome do arquivo (sem extensão)", "dados_tratados")

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Baixar CSV",
            data=csv,
            file_name=f"{nome_arquivo}.csv",
            mime="text/csv"
        )

        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)

        st.download_button(
            label="Baixar Excel",
            data=buffer,
            file_name=f"{nome_arquivo}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
else:
    st.markdown(
        """
        <h1 style='text-align: center;'>Tratativas de Dados</h1>

        <p>Ops! Parece que você ainda não carregou nenhum arquivo.</p>
        <p>Por favor, volte para a página inicial e carregue seu arquivo para começar a tratar os dados.</p>
        """,
        unsafe_allow_html=True
    )