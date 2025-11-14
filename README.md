# projeto_sprint_5
GitHub criado no âmbito de completar o projeto da Sprint 5 - Análise de Dados Tripleten


# Vehicle Data Analysis App

Este projeto foi bem interessante! Fiz um aplicativo web interativo, básico, criado com **Streamlit** para explorar um conjunto de dados de anúncios de vendas de carros.

## Funcionalidades do Aplicativo

O app permite visualizar informações do dataset por meio de dois tipos de gráficos interativos:

* **Histograma**: Mostra a relação entre os preço vs a distância marcada pelo odômetro dos veículos.
* **Gráfico de Dispersão**: exibe a relação entre preço e quilometragem.

O usuário pode escolher qual visualização deseja gerar utilizando **botões**.

## Tecnologias Utilizadas

* Python
* Pandas
* Plotly Express
* Streamlit

## Como Executar o Aplicativo

1. Ativa o seu ambiente virtual (caso esteja usando):

   ```bash
   conda activate vehicles_env
   ```
2. Executa o aplicativo:

   ```bash
   streamlit run app.py  #nesta parte levei horas até descobrir meu erro, mas ok!
   ```
3. O navegador abrirá automaticamente o app. Caso contrário, acesse o link mostrado no terminal.

## Estrutura do Projeto

```
projeto_sprint_5/

│── notebooks
    └── EDA.ipynb
│── .gitignore
│── app.py
│── README.md
│── requirements.txt
└── vehicles.csv
    
```

## Objetivo do Projeto

Este projeto faz parte do módulo de análise de dados da TripleTen e tem como objetivo ensinar os alunos a:

* Ler arquivos CSV
* Criar visualizações interativas
* Construir e executar um app com Streamlit

## Autor

Camila Costa de Mesquita.

## Nota pessoal:

Passei raiva, mas sobrevivi e no fim, adorei! Loucura!
