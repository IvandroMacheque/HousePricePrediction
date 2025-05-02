
# Previsão de preços com Machine Learning


Projeto de regressão que utiliza algoritmos de Machine Learning para prever os preços de imóveis com base em características como área, número de quartos, ano de construção, entre outros.

Os modelos foram avaliados com métricas como Erro Absoluto Médio, Raíz do Erro Quadrático Médio e R2(Coeficiente de Determinação).Após ajustes, os modelos atingiram ótima perfomance.


## Installation

1. Clone o repositório
 - git.clone
 - https://github.com/seu-usuario/nome-do-repositorio.git
2. Instale as dependências
 - pip install -r requirements.txt
    
# Uso


1. Execute o notebook "main.ipynb"
2. O notebook realiza:
 - caregamento e tratamento dos dados;
 - Treinamento com KNN e Random Forest;
 - Avaliação das métricas de regressão;
 - Visuaização dos erros e a distribuição dos preços.


## Resultados

**KNN:**
 - Erro Absoluto Médio: 21.025
 - RMSE: 25.756
 - R2: 0.99
 - Validação cruzada: média de 0.983

**Random Forest:**
 - Erro Absoluto Médio: 8.057
 - RMSEÇ 10.053
 - R2: 1.00
 - Validação cruzada: média de 0.988
## Visualização 

 - Distribuição dos preços
 - Correlação entre variáveis
 - Distribuição dos erros do modelo
 - Comparação entre preços reais e previstos
## Tecnologias Usadas

 - Python
 - Pandas
 - Scikit-Learn
 - Matplotlib / Seaborn
 - Jupyter Notebook
## Conclusão 

 - A Random Forest teve desempenho excelente com R2 próximo de 1, o que indica alto poder preditivo.

 - Após ajustes nos dados e escalonamento, o KNN também teve grande melhoria.

 - O modelo Random Forest é recomendado para esse tipo de projecto.