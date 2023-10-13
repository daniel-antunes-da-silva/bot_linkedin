from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice
from funcoes import *

pesquisa = 'farmacêutico'

print('Entrando no site')
# Entrando no site
wait, driver = iniciar_driver(headless=False)  # Aceita argumento: headless=True
driver.get('https://www.linkedin.com/feed/')
espera_aleatoria()

print('Pesquisando')
# Pesquisando
campo_pesquisar = wait.until(expected_conditions.visibility_of_element_located((
    By.XPATH, '//input[@type="text"]')))
espera_aleatoria()
campo_pesquisar.click()
espera_aleatoria(0.5, 1.5)
digitar_devagar(campo_pesquisar, pesquisa)
campo_pesquisar.send_keys(Keys.ENTER)
espera_aleatoria()

print('Clicando no botão pessoas')
# Clicando no botão pessoas
botao_pessoas = wait.until(expected_conditions.visibility_of_all_elements_located((
    By.XPATH, '//button[text()="Pessoas"]')))
espera_aleatoria()
botao_pessoas[0].click()
espera_aleatoria()
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
espera_aleatoria(0.5, 1.0)
botao_avancar = driver.find_element(By.XPATH, '//button//span[text()="Avançar"]')
espera_aleatoria(0.5, 1.0)
driver.execute_script('window.scrollTo(0, 0)')

while True:
    espera_aleatoria()
    while True:
        print('Verificando botões conectar')
        try:
            botoes_conectar = wait.until(expected_conditions.visibility_of_all_elements_located((
                By.XPATH, '//button//span[text()="Conectar"]')))
        except:
            botoes_conectar = False
        if not botoes_conectar:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            espera_aleatoria()
            botao_avancar = driver.find_element(By.XPATH, '//button//span[text()="Avançar"]')
            espera_aleatoria()
            driver.execute_script('arguments[0].click()', botao_avancar)
        else:
            break
        if not botao_avancar:
            break

    # Quando não tiver mais o botão avançar, interrompe o break
    if not botao_avancar:
        print('Interrompendo o loop por não haver botão avançar 2')
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
        mensagens = [f'Olá, gostaria de adicionar você à minha rede de contatos no LinkedIn.',
                     f'Oi, estou interessado em expandir minha rede profissional e acredito que poderíamos '
                     f'beneficiar um ao outro com nossa conexão no LinkedIn.']
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
