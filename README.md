# Leia com atenção esta parte

Foi retirado a funcionalidade de mensagem personalizada com o nome da pessoa.

Além disso, é POSSÍVEL que o programa esteja DESATUALIZADO atualmente, então leve isso em consideração caso queira fazer um Fork, mas de qualquer forma, o código presente foi a base que utilizei para que o programa funcionasse da forma desejada.

# Bots de LinkedIn - versão 2.0 

O repositório foi atualizado, trazendo duas funções e interface gráfica com PySimpleGUI.

Resumo do que foi utilizado:
- Python
- PySimpleGUI
- Selenium
- Threads (threading)
- Tkinter (filedialog para selecionar arquivos no bot de postagem)
- Random
- os
- Funções e modularização

# Como usar?

Primeiramente, você precisa ter o python instalado no seu computador. Caso não tenha, faça download no site oficial:

[Download Python](https://www.python.org/downloads/)


Com o Python instalado, faça download ou clone esse repositório (precisa ter o git configurado) em algum local do seu computador com o seguinte comando no terminal:

```
git clone https://github.com/daniel-antunes-da-silva/bot_linkedin.git
```

Abra o projeto no seu editor de código, e instale as dependências necessárias, que estão no arquivo requirements.txt.

Sugiro criar um ambiente virtual para o projeto, embora não seja obrigatório. Para isso, é necessário abrir o terminal dentro do projeto. Veja como criar um ambiente virtual no Windows (rode uma linha de código por vez):

```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

Instalando as dependências:

```
pip install -r requirements.txt
```

Pronto, agora que já tem o projeto e as dependências na sua máquina, você pode executar o programa rodando o arquivo _**"janelas.py"**_.

# Como funciona?

Ao rodar o programa, você verá a seguinte tela.


# Tela principal

Nessa tela, o usuário escolhe a automação (bot) a ser executada.

![tela_principal](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/ab114cbe-29b3-48f4-8c3c-c070a533408c)

Após a escolha, o bot iniciará as ações automáticas no computador, e isso inclui abrir o navegador **Google Chrome** e executar ações dentro dele.


# Bot de postagens

Assim que aparecer a tela, você precisa clicar em iniciar. Com isso, o programa vai pedir para que você selecione arquivos. O arquivo .txt é obrigatório, sendo que o de mídia você pode fechar a janela caso não queira.


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

**Caso não queira incluir nenhuma mensagem, ele funcionará apenas enviando as conexões.**

Nesse bot, também é exibido um histórico do que está acontecendo.

![historico_bot_conexoes](https://github.com/daniel-antunes-da-silva/bot_linkedin/assets/132831685/0beb528f-6a9a-4bd9-83a7-9a08f64624b4)


**_Importante:_**

O bot muda de página quando não houver mais botões de "conectar" disponíveis, sendo assim, o bot executará quase que infinitamente (até que o número de páginas acabem), sendo necessário ser encerrado pelo usuário.

  # Observações:
  * O post e a mídia escolhida serão publicados no LinkedIn, no perfil previamente logado no google chrome.
  * É necessário que o google chrome não esteja sendo executado durante o uso da automação. Feche-o antes de executar a automação.
  * Por ser uma automação web baseada no código fonte do site e utilizando XPATHs, pode ser que em algum momento a automação pare de funcionar caso o site mude.
  * Evite rodar por muito tempo a automação de conexões e com as mesmas mensagens, para evitar possíveis bloqueios.
  * Mesmo fazendo o passo acima, não posso garantir que o bot nunca será detectado pelo Linkedin. O bot foi construído com pausas entre as ações para evitar que se pareça com um robô, e parecer mais com um humano. Além disso, as pausas são aleatórias, para          evitar padronização. No entanto, redes sociais são sites sensívies, que podem identificar atividade suspeita em algum momento, por isso, o uso é de sua total responsabilidade e risco.
  * O intuito da criação do bot foi apenas para colocar em prática conhecimentos adquiridos, como forma de automatizar tarefas repetitivas.
