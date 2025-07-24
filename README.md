# 🏡 Previsão de Preços de Imóveis

Este é um projeto de Machine Learning que realiza a análise, o treinamento e a implantação de um modelo de regressão para prever o preço de imóveis. O projeto inclui um Jupyter Notebook com todo o processo de análise e modelagem e uma aplicação web interativa criada com Streamlit para realizar previsões em tempo real.

# ✨ Funcionalidades

Análise Exploratória de Dados (EDA): Investigação detalhada do conjunto de dados para identificar correlações, distribuições e outliers.

Treinamento de Modelo: Utilização de um modelo de Regressão Linear Regularizada (ElasticNet) para aprender os padrões dos dados.

Aplicação Web Interativa: Uma interface simples onde o usuário pode inserir as características de um imóvel e receber uma estimativa de preço instantaneamente.

Histórico de Previsões: A aplicação web armazena e exibe um histórico das previsões realizadas durante a sessão.

Exportação de Dados: Permite baixar o histórico de previsões como um ficheiro CSV.

# Escolha do modelo

O modelo de Regressão Linear foi escolhido devido a linearidade da coluna 'Square_Footage' com a coluna alvo 'House_Price', com uma correlação
de 99%. Devido aos outliers, foi criada uma coluna categórica para separá-los com ranges ('Square_Footage_Category'), o baixo e o alto foram colocados para os outliers, e o médio para os valore normais aumentando assim a eficiência do modelo.

# 💻 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

### Linguagem: Python 3

### Análise e Modelagem:

 - Jupyter Notebook

 - Pandas

 - NumPy

 - Scikit-learn

### Visualização de Dados:

 - Matplotlib

 - Seaborn

### Aplicação Web:

 - Streamlit

### Serialização do Modelo:

 - Pickle

# 📁 Estrutura do Projeto
.
├── notebook/
│   └── main.ipynb                      # Notebook com a análise e treinamento do modelo
├── Linear Regression.pkl               # Modelo de regressão treinado e salvo
├── README.md                           # Este ficheiro
├── app.py                              # Script da aplicação Streamlit
├── house_price_regression_dataset.csv  # Dataset original
└── requirements.txt                    # Dependências do projeto

# 📈 Uso da Aplicação

### Modo de Previsão (Price Predict):

1. Use os seletores e campos de entrada para inserir as características do imóvel (área, ano de construção, etc.).

2. Clique no botão "Realizar Previsão".

3. O preço estimado será exibido na tela.

### Modo de Histórico (Predicted Data):

1. Acesse esta opção na barra lateral para visualizar uma tabela com todas as previsões feitas na sessão atual.

2. Utilize os botões para limpar o histórico ou baixá-lo como um ficheiro .csv.

# 🔗 Link da Aplicação

https://previsaodeprecosdecasas.streamlit.app/
