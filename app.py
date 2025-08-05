import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open("Linear Regression.pkl", "rb") as f:
    modelo = pickle.load(f)

if "historic" not in st.session_state:
    st.session_state.historic = pd.DataFrame()

# configurando a sidebar
with st.sidebar:
    st.header('Options')
    decision = st.selectbox("Mode", ['Price Predict', 'Predicted Data'])
    st.markdown("### 🔗 Links Úteis")
    st.markdown("[📁 Este Projeto](https://github.com/IvandroMacheque/HousePricePrediction.git)")
    st.markdown("[👨‍💻 Meu GitHub](https://github.com/IvandroMacheque/IvandroMacheque.git)")
    st.markdown("[💼 Meu LinkedIn](https://www.linkedin.com/in/ivandromacheque?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.markdown("[🗂️ Outros Projetos](https://machequeivandro.notion.site/21c3f356a4b180d3a221ede7e8f1a0a3)")

if decision == 'Price Predict':

    st.title("🏡 House Price Prediction")
    st.write('## Insira os Dados da Casa')

    # input dos dados
    col1, col2 = st.columns(2)
    with col2:
        lot_size = st.slider('Lot Size', 0.500000, 5.000000, 2.000000)
    with col1:
        square_meters = st.slider('Área da Casa (m²)', 30.0, 500.0, 245.0)
        square_footage = square_meters * 10.7639104

    col6, col7 = st.columns(2)
    with col6:
        Neighborhood_Quality = st.slider('Qualidade dos Vizinhos', 1, 5, 10)
    with col7:
        year_built = st.number_input("Ano de Construção")

    col3, col4, col5 = st.columns(3)
    with col3:
        num_bedrooms = st.radio(
                "Número de Quartos",
                options=[1, 2, 3, 4, 5, 6],
            )
    with col4:
        num_bathrooms = st.radio(
                "Número de Banheiros",
                options=[1, 2, 3, 4],
            )
    with col5:
        garage_size = st.radio(
                "Tamanho da Garagem",
                options=["Sem Garagem", 1, 2, 3],
            )
        if garage_size == "Sem Garagem":
            garage_size = 0

    # criar e modelar o dataset para o modelo
    data_modelo = {'Square_Footage': square_footage,
            'Year_Built': year_built,
            'Lot_Size': lot_size}
    dados_modelo = pd.DataFrame(data_modelo, index=[0])
    bins = [0 , 1600, 3999, np.inf]
    labels = ['baixo', 'medio', 'alto']
    dados_modelo['Square_Footage_Category'] = pd.cut(dados_modelo['Square_Footage'], bins=bins, labels=labels)
    dados_modelo['Square_Footage_Category'] = dados_modelo['Square_Footage_Category'].map({'baixo': 0,
                                                                            'medio': 1,
                                                                            'alto': 2})
    # previsao do preco
    def prever():
        previsao = modelo.predict(dados_modelo)
        with container:
            st.success(f"### O Preço previsto da casa é de {previsao[0]:.2f}")
        data = {'Square_Footage': square_footage,
            'Num_Bedrooms': num_bedrooms,
            'Num_Bathrooms': num_bathrooms,
            'Year_Built': year_built,
            'Lot_Size': lot_size,
            'Garage_Size': garage_size,
            'Neighborhood_Quality': Neighborhood_Quality,
            'House_Price': previsao[0]}
        dados = pd.DataFrame(data, index=[0])
        st.session_state.historic = pd.concat([st.session_state.historic, dados], ignore_index=True)

    # botao de previsao
    container = st.container()
    st.button("Realizar Previsão", on_click=prever)

else:
    st.title("📜 Forecast History")

    # visualizacao do histórico de previsão 
    st.dataframe(st.session_state.historic)

    # linha de botoes
    but1, but2 = st.columns(2)
    # funcao para limpar o historico
    with but1:
        if not st.session_state.historic.empty:
            def limpar():
                st.session_state.historic = pd.DataFrame()
            st.button("Limpar histórico", on_click=limpar)

    # funcao para salvar o historico
    with but2:
        if not st.session_state.historic.empty:
            def convert_for_download(df):
                return df.to_csv(index=False).encode("utf-8")
            
            file = convert_for_download(st.session_state.historic)
            st.download_button(
                label="Baixar Histórico",
                data=file,
                file_name='Precos Previstos.csv',
                mime='text/csv'
            )

