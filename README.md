# 🌺 Reconhecimento de Flores com Rede Neural Convolucional (CNN) 🌻

Este projeto consiste em uma aplicação de reconhecimento de flores utilizando uma Rede Neural Convolucional (CNN). A aplicação permite aos usuários enviar imagens de flores e obter uma previsão sobre qual tipo de flor a imagem representa, juntamente com uma pontuação de confiança.

## Funcionalidades

- **Carregamento e Pré-processamento de Dados**: O código carrega um conjunto de dados de imagens de flores, divide-o em conjuntos de treinamento e validação e aplica técnicas de pré-processamento, como redimensionamento e data augmentation.

- **Construção e Treinamento da CNN**: Uma CNN é construída usando a biblioteca TensorFlow/Keras. A arquitetura da CNN inclui camadas de convolução, pooling, dropout e densas para realizar a classificação das imagens.

- **Classificação de Imagens**: Os usuários podem fazer upload de suas próprias imagens de flores. O sistema classifica essas imagens usando o modelo treinado e retorna o tipo de flor previsto, juntamente com uma pontuação de confiança.

## Como Usar

1. **Instalação de Dependências**: Certifique-se de ter todas as dependências instaladas. Você pode instalá-las executando `pip install -r requirements.txt`.

2. **Treinamento do Modelo (Opcional)**: Se desejar treinar o modelo novamente com seus próprios dados, siga as instruções no código para carregar seus dados de imagens.

3. **Execução da Aplicação**: Para executar a aplicação, simplesmente execute o arquivo `streamlit run app.py` com Python. Isso iniciará o servidor web e abrirá a aplicação no navegador.

4. **Upload de Imagens**: Na aplicação web, os usuários podem fazer upload de suas próprias imagens de flores clicando no botão "Upload an Image".

5. **Visualização dos Resultados**: Após o upload da imagem, a aplicação exibirá a imagem enviada e a classificação prevista, juntamente com uma pontuação de confiança.

## Arquivos e Diretórios

- **`app.py`**: Contém o código para a aplicação web desenvolvida com Streamlit. Gerencia o upload de imagens e exibe os resultados da classificação.

- **`Classificação de flores.ipynb`**: Contém o código para construir, treinar e salvar o modelo CNN usando TensorFlow/Keras.

- **`requirements.txt`**: Lista as dependências do Python necessárias para executar a aplicação.

- **`imagens/`**: Diretório que contém o conjunto de dados de imagens de flores para treinamento e validação.

- **`amostra/`**: Diretório de amostra contendo imagens de flores para teste da aplicação.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para obter mais detalhes.

<img align="right" width ='40px' src ='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg'> </a>
<img align="right" width ='40px' src ='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg'> </a>
