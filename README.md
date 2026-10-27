IFRN
Tópicos Específicos (IA)
Atividade 3: Geração de Embeddings com Ollama Local

Este repositório contém a solução da atividade 3, cujo objetivo é demonstrar habilidade em instalar e operar o Ollama localmente, bem como gerar vetores de embeddings a partir de um texto simples utilizando Python.

O aluno deve instalar e configurar o Ollama localmente em sua máquina.
Desenvolver um script em Python ou um notebook Jupyter que execute as seguintes ações:
Conectar ao Ollama localmente.
Fornecer um texto simples (por exemplo, uma frase curta em português ou inglês).
Gerar os vetores de embeddings correspondentes ao texto utilizando o Ollama.
Exibir o vetor de embeddings, seja de forma integral ou por meio de um sumário, como o tamanho do vetor e alguns valores iniciais.
Criar um repositório público no GitHub contendo:
O código-fonte do script Python ou notebook Jupyter.
Um README.md com:
Instruções para reprodução do ambiente.
Orientações para instalação de dependências e execução do script ou notebook.
Gravar um vídeo objetivo (máximo de 3 minutos) demonstrando as seguintes etapas:
Execução do Ollama localmente, exibindo o comando de inicialização e/ou a saída que confirma que o serviço está ativo.
Execução do script Python ou notebook Jupyter, mostrando a geração do vetor de embeddings e a saída no console.
O vídeo deve ser claro e objetivo, de forma a evidenciar a execução bem-sucedida de todas as etapas.

-

Visão Geral

O script `embeddings.py` conecta-se ao Ollama rodando localmente, envia um texto simples e gera o vetor de embeddings correspondente. A saída exibe o tamanho do vetor e alguns valores numéricos, comprovando o funcionamento.

- Modelo utilizado: `nomic-embed-text`
- Texto de entrada: "Obrigada, professor Thiago Medeiros Barros."
- Dimensões do vetor gerado: 768

Requisitos do Ambiente

- Sistema Operacional: macOS (Sonoma 14 ou superior), Linux ou Windows
- Python: 3.10 ou superior
- Ollama: instalado e em execução
- Conexão com a internet

Instalação do Ollama

1. Acesse a página oficial de download: [https://ollama.com/download](https://ollama.com/download)
2. Baixe e instale o aplicativo conforme o seu sistema operacional.
3. Após a instalação, verifique se o Ollama está ativo: ollama --version
A saída deve exibir a versão instalada (ex: ollama version is 0.x.x).

Download do modelo de embeddings
O script utiliza o modelo nomic-embed-text, especializado na geração de embeddings. Baixe-o com:
ollama pull nomic-embed-text
⚠️ Nota: modelos de chat (como llama3.2) não suportam a geração de embeddings e retornarão erro. Por isso, é obrigatório utilizar um modelo específico para essa finalidade.

Instalação das dependências Python
O script depende da biblioteca oficial ollama para Python. Instale-a com:
pip3 install ollama
Se pip3 não estiver disponível, instale o Python via Homebrew (brew install python) ou utilize python3 -m pip install ollama.

Execução do Script
Com o Ollama em execução e o modelo baixado, execute o script:
python3 embeddings.py
O terminal deverá exibir algo semelhante a:

text
Texto: Obrigada, professor Thiago Medeiros Barros.

Modelo: nomic-embed-text

Tamanho do vetor: 768 dimensões
Primeiros 10 valores: [0.0308..., 0.0558..., -0.1055..., ...]
Últimos 5 valores: [0.0098..., 0.0054..., 0.0027..., ...]
A presença do tamanho do vetor (768 dimensões) e dos valores numéricos comprova que o Ollama gerou os embeddings com sucesso.

Estrutura do Projeto
text
IFRN_ollama-embeddings/
├── embeddings.py   # Script Python que gera os embeddings
└── README.md       # Este arquivo com instruções de reprodução

Explicação do Código
O script embeddings.py realiza as seguintes etapas:
Importa a biblioteca ollama.
Define o texto de entrada e o modelo a ser utilizado.
Chama a API ollama.embed() passando o modelo e o texto.
Extrai o vetor de embeddings da resposta.
Exibe no console o tamanho do vetor e amostras dos valores (iniciais e finais).
