
# Assistente Virtual de Conversação com GPT-3 e Reconhecimento de Fala

Bem-vindo ao projeto Assistente Virtual de Conversação! Este projeto utiliza tecnologias como GPT-3 da OpenAI, reconhecimento de fala e Python para criar um assistente virtual interativo. O assistente é capaz de converter comandos de voz em texto, gerar respostas inteligentes e contextualizadas com base na entrada do usuário usando GPT-3 e transformar essas respostas de volta em fala.

## Tecnologias Utilizadas

- OpenAI GPT-3: Fornece respostas inteligentes e contextuais.
- SpeechRecognition (sr): Biblioteca para reconhecimento de fala.
- pyttsx3: Converte texto em fala.
- dotenv: Gerencia variáveis de ambiente, incluindo chaves de API.

## Funcionalidades
### Reconhecimento de Fala:
- Captura a fala do usuário via microfone.
- Converte a fala em texto usando o Google Speech Recognition.
### Interação com GPT-3:
- Envia o texto reconhecido para o GPT-3.
- Recebe respostas geradas pelo modelo.
### Conversão Texto para Fala:
- Converte as respostas do GPT-3 de volta em fala usando o pyttsx3.
### Encerramento por Comando de Voz:
- Permite ao usuário encerrar a conversa dizendo "Barney encerrar conversa".

## Utilização
    1. Clone o repositório: git clone https://github.com/seu-usuario/assistente-virtual.git
    2. Instale as dependências: pip install -r requirements.txt
    3. Configure as variáveis de ambiente em um arquivo .env.
    4. Execute o script: python main.py


