# Projeto: Gerador de Dados de Clientes e Vendas

Este projeto consiste em um código em Python que utiliza a biblioteca Faker para gerar dados fictícios de clientes. A partir desses dados, são gerados dados de vendas em formato JSON. O objetivo é simular um ambiente de vendas com informações de clientes e transações.

O projeto também utiliza as seguintes tecnologias e serviços na AWS:

- **Boto3**: O Boto3 é a biblioteca oficial da AWS para interagir com os serviços da AWS usando Python. Ele é utilizado neste projeto para fazer o upload dos dados gerados para o serviço S3 (Simple Storage Service) na AWS.

- **AWS Glue**: O AWS Glue é um serviço de descoberta, catalogação e transformação de dados. Ele é utilizado neste projeto para detectar o esquema da tabela que armazena os dados de vendas no S3. O AWS Glue permite que você defina o esquema da tabela automaticamente com base nos dados fornecidos.

- **AWS Athena**: O AWS Athena é um serviço de consulta interativa que permite analisar dados armazenados no S3 usando SQL. Neste projeto, o Athena é utilizado para realizar consultas nos dados de vendas gerados, permitindo a análise e extração de informações relevantes.

## Pré-requisitos

Antes de executar o código, você precisa ter os seguintes pré-requisitos:

- Ter o Python instalado (versão 3.6 ou superior).
- Instalar a biblioteca Faker. Você pode instalar usando o gerenciador de pacotes pip: `pip install faker`.
- Configurar as credenciais da AWS. Certifique-se de ter as credenciais corretas para acessar os serviços da AWS. Você pode configurar as credenciais executando o comando `aws configure` e fornecendo as informações necessárias.

## Executando o projeto

Siga os passos abaixo para executar o projeto:

1. Clone o repositório do projeto:

   ```
   git clone <URL DO REPOSITÓRIO>
   ```

2. Acesse o diretório do projeto:

   ```
   cd gerador-dados-vendas
   ```

3. Execute o script principal:

   ```
   python main.py
   ```

   O script irá gerar os dados de clientes e vendas usando a biblioteca Faker. Em seguida, ele fará o upload dos dados gerados para o serviço S3 na AWS usando a biblioteca Boto3.

4. Após o upload dos dados, o AWS Glue será acionado para detectar o esquema da tabela de vendas com base nos dados carregados no S3.

5. Com o esquema da tabela detectado, você pode realizar consultas nos dados de vendas usando o AWS Athena. Para isso, acesse o console do AWS Athena e execute as consultas SQL desejadas.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de arquivos:

- `main.py`: O script principal que utiliza a biblioteca Faker para gerar dados de clientes e vendas, e faz o upload dos dados para o S3 usando o Boto3.
- `README.md`: O arquivo que você está lendo atualmente, contendo informações sobre o projeto.
- `requirements.txt`: O arquivo que lista as dependências do projeto, incluindo a biblioteca Faker.

## Conclusão

O projeto "Gerador de Dados de Clientes e Vendas" demonstra como utilizar a biblioteca Faker em Python para gerar dados fictícios de clientes e vendas. Além disso, ele integra os serviços da AWS, como o S3, AWS Glue e Athena, para fazer o upload dos dados, detectar o esquema da tabela e realizar consultas nos dados gerados.

Esse projeto pode ser útil para simular um ambiente de vendas, realizar testes ou estudos de análise de dados. Fique à vontade para explorar e personalizar o projeto de acordo com suas necessidades.
