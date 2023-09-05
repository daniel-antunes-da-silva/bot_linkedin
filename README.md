# Bot de postagem no LinkedIn - versão 1.0 

Nessa versão:
# O usuário vai precisar passar todo o caminho onde a mídia está. Ex: C:\Users\[nome_do_usuario]\Pictures\image.png
# O windows abrirá a caixa de diálogo para inserir a mídia e ficará aberto até o final da execução, já que não precisaremos dela diretamente.
# Isso não é um problema, e com o uso do argumento --headless, que permite a execução em segundo plano, a caixa de diálogo não é exibida.
# Caso não tivesse essa opção, poderia ser utilizado o pyautogui para fechá-la.

Nas próximas versões:
# O usuário poderá utilizar um caminho padrão, mudando apenas o nome do arquivo de acordo com o que vai publicar. Sendo assim, recomenda-se que o usuário sempre crie uma pasta para manter os arquivos a serem publicados.
# Ou poderá também ser exibido a caixa de diálogo do windows para selecionar as imagens no início do programa. Testarei as possibilidades.
# O usuário poderá escolher se quer agendar ou não uma postagem