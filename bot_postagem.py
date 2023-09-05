from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from random import uniform
from funcoes import iniciar_driver, digitar_devagar

texto = str(input('Cole aqui o texto a ser publicado: ')).strip()
print('Especifique o caminho da mídia com o nome do arquivo, ou', end=' ')
diretorio = str(input('deixe em branco para publicar apenas texto: ')).strip()

wait, driver = iniciar_driver()
driver.get('https://www.linkedin.com/')
sleep(uniform(4.0, 9.0))

# Escrevendo o texto
iniciar_publicacao = wait.until(expected_conditions.element_to_be_clickable((
    By.XPATH, '//button[@class="artdeco-button artdeco-button--muted artdeco-button--4 '
              'artdeco-button--tertiary ember-view share-box-feed-entry__trigger"]')))
sleep(uniform(1.5, 6.5))
iniciar_publicacao.click()
sleep(uniform(1.5, 6.5))
campo_texto = wait.until(expected_conditions.visibility_of_element_located((
    By.XPATH, '//div[@aria-label="Editor de texto para criação de conteúdo"]')))
sleep(uniform(1.5, 6.5))
digitar_devagar(campo_texto, texto)
sleep(uniform(1.5, 6.5))

# Adicionando mídia
if diretorio != '':
    botao_midia = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH, '//button[@aria-label="Adicionar mídia"]')))
    botao_midia.click()
    enviar_midia = driver.find_element(By.ID, 'media-editor-file-selector__file-input')
    sleep(uniform(1.5, 6.5))
    enviar_midia.send_keys(diretorio)
    sleep(uniform(1.5, 6.5))
    sleep(1)
    botao_avancar = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH, '//button[@class="share-box-footer__primary-btn artdeco-button'
                  ' artdeco-button--2 artdeco-button--primary ember-view"]')))
    sleep(uniform(1.5, 6.5))
    botao_avancar.click()
    sleep(uniform(1.5, 6.5))

# Publicando o post
botao_publicar = wait.until(expected_conditions.element_to_be_clickable((
    By.XPATH, '//button[@class="share-actions__primary-action artdeco-button '
              'artdeco-button--2 artdeco-button--primary ember-view"]')))
sleep(uniform(1.5, 6.5))
botao_publicar.click()
sleep(uniform(1.5, 6.5))

driver.close()
