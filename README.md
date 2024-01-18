# BUSCADOR DE ID
[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA)
[![GitHub Repo stars](https://img.shields.io/badge/CURSO%20DE-TELEGRAM%20BOT-03A9F4?logo=github)](https://github.com/VILHALVA/CURSO-DE-TELEGRAM-BOT)

<img src="https://smartbotsland.com/bots/wp-content/uploads/2022/07/Subscription-Bot.png" align="center" width="280"> <br>

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

## COMO USAR?
1. **Coloque o Token:**
   - Antes de executar o programa, é necessário substituir o token do seu bot na linha `4`, o qual pode ser obtido por meio do [@BotFather](https://t.me/BotFather). Certifique-se também de que todas as dependências estejam instaladas em sua máquina. Se você não estiver familiarizado com esses passos, confira nosso [curso completo sobre a criação de bots no Telegram](https://github.com/VILHALVA/CURSO-DE-TELEGRAM-BOT) para obter orientações detalhadas.

2. **Inicie o Bot:**
   - Inicie o bot enviando o comando `/start`. Receba uma mensagem de boas-vindas e instruções.

3. **Encaminhar Mensagem:**
   - Encaminhe uma mensagem de um grupo ou canal para o bot.
   - O bot identifica o ID do chat da mensagem original e responde enviando uma mensagem com esse ID.

Este bot fornece uma maneira rápida e simples de obter o ID do chat de mensagens encaminhadas, o que pode ser útil em diversos contextos, especialmente para administradores de grupos ou canais no Telegram.