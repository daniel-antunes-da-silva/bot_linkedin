from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from funcoes import iniciar_driver, digitar_devagar, espera_aleatoria

texto = str(input('Cole aqui o texto a ser publicado: ')).strip()
print('Especifique o caminho da mídia com o nome do arquivo, ou', end=' ')
diretorio = str(input('deixe em branco para publicar apenas texto: ')).strip()

wait, driver = iniciar_driver()
driver.get('https://www.linkedin.com/')
espera_aleatoria(4, 9.0)

# Escrevendo o texto
iniciar_publicacao = wait.until(expected_conditions.element_to_be_clickable((
    By.XPATH, '//button[@class="artdeco-button artdeco-button--muted artdeco-button--4 '
              'artdeco-button--tertiary ember-view share-box-feed-entry__trigger"]')))
espera_aleatoria()
iniciar_publicacao.click()
espera_aleatoria()
campo_texto = wait.until(expected_conditions.visibility_of_element_located((
    By.XPATH, '//div[@aria-label="Editor de texto para criação de conteúdo"]')))
espera_aleatoria()
digitar_devagar(campo_texto, texto)
espera_aleatoria()

# Adicionando mídia
if diretorio != '':
    botao_midia = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH, '//button[@aria-label="Adicionar mídia"]')))
    botao_midia.click()
    enviar_midia = driver.find_element(By.ID, 'media-editor-file-selector__file-input')
    espera_aleatoria()
    enviar_midia.send_keys(diretorio)
    espera_aleatoria()
    sleep(1)
    botao_avancar = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH, '//button[@class="share-box-footer__primary-btn artdeco-button'
                  ' artdeco-button--2 artdeco-button--primary ember-view"]')))
    espera_aleatoria()
    botao_avancar.click()
    espera_aleatoria()

# Publicando o post
botao_publicar = wait.until(expected_conditions.element_to_be_clickable((
    By.XPATH, '//button[@class="share-actions__primary-action artdeco-button '
              'artdeco-button--2 artdeco-button--primary ember-view"]')))
espera_aleatoria()
botao_publicar.click()
espera_aleatoria()

driver.close()
