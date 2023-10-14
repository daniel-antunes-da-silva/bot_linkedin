# Bots de LinkedIn - versão 2.0 

O repositório foi atualizado, trazendo duas funções e interface gráfica com PySimpleGUI.

Resumo do que foi utilizado:
- Python
- PySimpleGUI
- Selenium WebDriver
- Threads (threading)
- Tkinter (filedialog para selecionar arquivos no bot de postagem)
- Random
- os
- Funções e modularização


# Tela principal

Nessa tela, o usuário escolhe a automação (bot) a ser executada.

![tela_principal](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/ab114cbe-29b3-48f4-8c3c-c070a533408c)

Após a escolha, o bot iniciará as ações automáticas no computador, e isso inclui abrir o navegador **Google Chrome** e executar ações automáticas dentro dele.



# Bot de postagens

Postagem automática de textos (carregar arquivo .txt) + mídia no LinkedIn, com pausas estratégicas para melhor carregamento dos elementos e humanização.

Os arquivos são selecionados a partir da caixa de diálogo para inserção de arquivos. Veja só:

![solicitacoes de arquivos](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/f5d16159-3ea6-4dd0-bdf7-ec67883f0d08)

O arquivo de TEXTO precisa ser do tipo .txt.

O programa vai informar ao usuário as etapas que estão aconteecendo, além de informar a etapa que possa acontecer algum erro... Tudo isso é exibido na seção de histórico da interface gráfica:

![historico_bot_postagem](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/abc2d7ce-6613-4635-9c55-d66de1c9f7b8)
Obs: essas acima são as etapas que ocorrem caso o bot funcione corretamente.



# Bot de conexões

Conexões automáticas com outros usuários, de acordo com a profissão escolhida. O bot filtra por pessoas que tenham essa profissão, e começa a se conectar automaticamente.
Caso queira, é possível incluir uma mensagem, e ela deve ser iniciada dessa forma, pulando o cumprimento (o bot vai adicionar automaticamente um Olá {nome_da_pessoa} no início de cada mensagem.

![bot_conexoes](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/130a8bee-7c34-43f6-9038-c99f33775f03)

Caso não queira incluir nenhuma mensagem, ele funcionará apenas enviando as conexões.

Nesse bot, também é exibido um histórico do que está acontecendo.

![historico_bot_conexoes](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/0beb528f-6a9a-4bd9-83a7-9a08f64624b4)


**_Importante:_**
O bot muda de página quando não houver mais botões de "conectar" disponíveis, sendo assim, o bot executará quase que infinitamente (até que o número de páginas acabem), sendo necessário ser encerrado pelo usuário.



# Observações:
* O post e a mídia escolhida serão publicados no LinkedIn, no perfil previamente logado no google chrome.
* É necessário que o google chrome não esteja sendo executado durante o uso da automação. Feche-o antes de executar a automação.
* Por ser uma automação web baseada no código fonte do site e utilizando XPATHs, pode ser que em algum momento a automação pare de funcionar caso o site mude.
