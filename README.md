# data-engineer-pl-test

Teste técnico para vaga de engenharia de dados

## Objetivo

O objetivo do teste é processar um grande arquivo CSV de forma performática, considerando que o script possa ser executado em uma máquina com pouca memória.

## Requisitos
Ler o arquivo por partes e trazer as seguintes análises:
1. Identificar o produto mais vendido em termos de quantidade e canal;
3. Determinar qual pais e região teve o maior volume de vendas em valor;
4. Calcular a média de vendas mensais por produto, considerando o período dos dados disponíves.

## Processo
Para tentar otimizar esse processo, utilizei o parâmetro chunksize do método read_csv passando o valor 50.000 para carregar uma quantidade menor de linhas em cada 'chunk', e também selecionei apenas as colunas que considerei necessárias ao criar o dataframe.  

Para as análises, criei o arquivo `utils.py` com as funções para fazer o processamento do dataframe, e para cada resultado, salvei um arquivo CSV na pasta `results`. Também usei o comando print para poder visualizar uma parte do dataframe no momento da execução.  

## Como executar
1. Crie uma pasta chamada `data` na raíz do projeto e adicione o arquivo CSV. Não foi possível fazer isso pelo tamanho do arquivo que ultrapassa os limites do Github.

2. Crie um ambiente virtual
```bash
virtualenv .env  
```

3. Ative o ambiente virtual
```bash
source .env/bin/activate  
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

5. Execute o script
```bash
python main.py
```
