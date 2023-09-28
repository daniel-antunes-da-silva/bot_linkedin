from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice
from funcoes import *


def encontrar_botoes_conectar():
    global wait
    try:
        btns_conectar = wait.until(expected_conditions.visibility_of_all_elements_located((
            By.XPATH, '//button//span[text()="Conectar"]')))
    except:
        return False
    else:
        return btns_conectar


def encontrar_botao_avancar():
    global driver
    try:
        btn_avancar = driver.find_element(By.XPATH, '//button//span[text()="Avançar"]')
    except:
        return False
    else:
        return btn_avancar


pesquisa = 'fisioterapeuta'

# Entrando no site
wait, driver = iniciar_driver()  # Aceita argumento: headless=True
driver.get('https://www.linkedin.com/feed/')
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
espera_aleatoria()

botao_avancar = None

while True:
    espera_aleatoria()
    while True:
        botoes_conectar = encontrar_botoes_conectar()

        # Verificando... Caso não tenha botão conectar, desce até o final da página e clica no botão avançar...
        if not botoes_conectar:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            espera_aleatoria()
            botao_avancar = encontrar_botao_avancar()

            # Quando não tiver mais o botão avançar, interrompe o break
            if not botao_avancar:
                break
            espera_aleatoria()
            driver.execute_script('arguments[0].click()', botao_avancar)
            espera_aleatoria()
        else:
            break

    # Quando não tiver mais o botão avançar, interrompe o break
    if not botao_avancar:
        break

    # Adicionando notas em cada pessoa com botão disponível
    for botao in botoes_conectar:
        espera_aleatoria()
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

input('Aperte ENTER para encerrar.')
driver.close()
