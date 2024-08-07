# BUSCADOR DE ID
🧑‍💻ENCONTRE O ID DO SEU GRUPO OU CANAL DO TELEGRAM COM ESSE SIMPLES BOT EM PYTHON.

<img src="FOTO.png" align="center" width="500"> <br>

## AVISO:
Até a data de lançamento deste bot (18/01/2024), o aplicativo oficial do Telegram não oferece uma função nativa que permita aos usuários descobrir o ID de algum grupo ou canal. Aqueles que conseguem realizar essa tarefa geralmente utilizam clientes personalizados do Telegram que disponibilizam tal recurso ou contam com a assistência de bots especializados. Foi com o intuito de preencher essa lacuna que desenvolvi a minha própria versão simplificada desse recurso. Mesmo que o Telegram venha a incorporar essa funcionalidade em futuras atualizações, manterei este bot ativo aqui no [GITHUB](https://github.com/VILHALVA?tab=repositories&q=+topic:BOT) como uma alternativa prática e acessível.

## DESCRIÇÃO:
Esse bot do Telegram tem duas funcionalidades principais:

1. **Comando /start:**
   - Quando o usuário envia o comando `/start` para o bot, ele responde com uma mensagem de boas-vindas.
   - Também envia instruções de uso, indicando ao usuário que a função principal é exibir o ID do chat de uma mensagem encaminhada.

2. **Mensagens Encaminhadas:**
   - Quando o usuário encaminha uma mensagem (textual, foto, vídeo, áudio, documento, adesivo, voz, etc.) de um grupo ou canal, o bot responde com uma mensagem contendo o ID do chat da mensagem original.
   - O ID do chat é uma identificação única associada ao grupo ou canal de onde a mensagem foi encaminhada.
   - O trecho `<b>` e `</b>` envolve o texto "ID DO CHAT:", tornando-o em negrito, enquanto a tag `<code>` e `</code>` é usada para formatar o ID do chat em um estilo de código (Permitindo que você copie o id para área de transferência apenas clicando nele).

## EXECUTANDO O PROJETO:
1. **Coloque o Token:**
   - Antes de executar, é necessário introduzir o token do seu bot no arquivo `./CODIGO/TOKEN.py`, o qual pode ser obtido por meio do [@BotFather](https://t.me/BotFather). 

2. **Instalando as dependências:**
   - Antes de executar o bot, certifique-se de instalar todas as dependências necessárias. No terminal, execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt` em `CODIGO`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie o Bot:**
   - Execute o bot do Telegram em Python iniciando-o com o seguinte comando:
   ```bash
   python CODIGO.py
   ```

   - Inicie o bot enviando o comando `/start`. Receba uma mensagem de boas-vindas e instruções.

4. **Encaminhar Mensagem:**
   - Encaminhe uma mensagem de um grupo ou canal para o bot.
   - O bot identifica o ID do chat da mensagem original e responde enviando uma mensagem com esse ID.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias relacionadas, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos alguns subsidios:
* [CURSO DE TELEBOT](https://github.com/VILHALVA/CURSO-DE-TELEBOT)
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
