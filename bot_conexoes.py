from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
from random import choice
from funcoes import *

# Passo a passo
# entrar linkedin
# encontrar campo pesquisar
# digitar no campo pesquisar e apertar enter
# encontrar campo pessoas
# clicar no campo pessoas
# encontrar elementos de conectar
# clicar em cada um deles
# em seguida, encontrar o elemento de adicionar nota e clicar
# Pegar o [nome] do usuário para criar mensagem personalizada
# Escrever a nota com o nome do usuário armazenado.
# Clicar no botão enviar
# Repetir esse processo para todos disponíveis
# Avançar página e repetir

# Definindo conteúdo da pesquisa
pesquisa = 'nutricionista'


# Entrando no site
wait, driver = iniciar_driver()  # Aceita argumento: headless=True
driver.get('https://www.linkedin.com/feed/')
# chain = ActionChains(driver)
espera_aleatoria()

# Pesquisando
campo_pesquisar = wait.until(expected_conditions.visibility_of_element_located((
    By.XPATH, '//input[@type="text"]')))
espera_aleatoria()
campo_pesquisar.click()
espera_aleatoria(0.5, 1.5)
digitar_devagar(campo_pesquisar, pesquisa)
campo_pesquisar.send_keys(Keys.ENTER)
espera_aleatoria()

# Clicando no botão pessoas
botao_pessoas = wait.until(expected_conditions.visibility_of_all_elements_located((
    By.XPATH, '//button[text()="Pessoas"]')))
espera_aleatoria()
botao_pessoas[0].click()

# Verificar se existe o botão conectar, e se não existir, rolar até o fim e avançar a página enquanto não existir.

# Encontrando botões conectar
espera_aleatoria()
botoes_conectar = wait.until(expected_conditions.visibility_of_all_elements_located((
    By.XPATH, '//button//span[text()="Conectar"]')))


# Adicionando notas em cada pessoa com botão disponível
for botao in botoes_conectar:
    botao.click()
    espera_aleatoria()
    botao_add_nota = wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//button[@aria-label="Adicionar nota"]')))
    espera_aleatoria()
    botao_add_nota.click()
    espera_aleatoria()
    texto_com_nome = wait.until(expected_conditions.visibility_of_element_located((
        By.ID, 'send-invite-modal')))
    texto = texto_com_nome.text
    texto = texto.split()
    nome = texto[1]
    mensagens = [f'Olá {nome}, gostaria de adicionar você à minha rede de contatos no LinkedIn. Estou sempre em busca '
                 f'de ampliar minha rede profissional e acredito que podemos trocar conhecimentos e experiências. '
                 f'Aguardo sua conexão!',
                 f'Oi {nome}, estou interessado em expandir minha rede profissional e acredito que poderíamos '
                 f'beneficiar um ao outro com nossa conexão no LinkedIn. Vamos nos conectar e compartilhar '
                 f'conhecimentos e experiências? Fico aguardando sua aceitação!']
    campo_notas = wait.until(expected_conditions.visibility_of_element_located((
        By.ID, 'custom-message')))
    campo_notas.send_keys(choice(mensagens))
    # digitar_devagar(campo_notas, choice(mensagens))
    enviar_conexao = wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//button[@aria-label="Enviar agora"]')))
    espera_aleatoria()
    enviar_conexao.click()
    espera_aleatoria()
    driver.execute_script('window.scrollTo(0, 200)')
    espera_aleatoria()
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# Encontrar botão de avançar e verificar se ele existe para poder fazer as ações.
# Quando não houver mais botãod e conectar, vai avançar a página.
input('Aperte ENTER para encerrar.')
driver.close()
