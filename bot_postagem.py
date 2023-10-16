from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from funcoes import iniciar_driver, digitar_devagar, espera_aleatoria, ler_txt, selecionar_arquivo


def bot_postagem():
    try:
        print('Selecionando arquivos...', end=' ')
        diretorio_texto = selecionar_arquivo('Arquivos de texto', '*.txt')
        texto = ler_txt(nome_arquivo=diretorio_texto[0])
        diretorios_midia = selecionar_arquivo()
        print(diretorios_midia, end=' ')
    except:
        print('Ocorreu algum problema na escolha de arquivos.')
    else:
        print('OK')
        try:
            print('Navegando até o site...', end=' ')
            wait, driver = iniciar_driver(headless=False)
            driver.get('https://www.linkedin.com/')
            espera_aleatoria(2.0, 4.5)
        except:
            print('Ocorreu algum problema na navegação até o site.')
        else:
            print('OK')
            try:
                # Iniciando a publicação
                print('Iniciando a publicação...')
                iniciar_publicacao = wait.until(expected_conditions.element_to_be_clickable((
                    By.XPATH, '//button[@class="artdeco-button artdeco-button--muted artdeco-button--4 '
                              'artdeco-button--tertiary ember-view share-box-feed-entry__trigger"]')))
                espera_aleatoria()
                iniciar_publicacao.click()
                espera_aleatoria()
                print('Adicionando mídia(s)...', end=' ')
                # Adicionando mídia
                if diretorios_midia != '':
                    espera_aleatoria()
                    botao_midia = wait.until(expected_conditions.element_to_be_clickable((
                        By.XPATH, '//button[@aria-label="Adicionar mídia"]')))
                    espera_aleatoria()
                    botao_midia.click()
                    qtd_arquivos = len(diretorios_midia)
                    for diretorio in diretorios_midia:
                        enviar_midia = driver.find_element(By.ID, 'media-editor-file-selector__file-input')
                        espera_aleatoria()
                        enviar_midia.send_keys(diretorio)
                        espera_aleatoria()
                        if qtd_arquivos > 1:
                            adicionar_mais = driver.find_elements(
                                By.XPATH, '//div[@class="artdeco-notification-badge ember-view"]//button['
                                          '@aria-describedby]')
                            espera_aleatoria()
                            # O botão de mídia nessa etapa está na posição 5.
                            adicionar_mais[5].click()
                            espera_aleatoria()
                        qtd_arquivos -= 1
                        sleep(1)

                    botao_avancar = wait.until(expected_conditions.element_to_be_clickable((
                        By.XPATH, '//button[@class="share-box-footer__primary-btn artdeco-button'
                                  ' artdeco-button--2 artdeco-button--primary ember-view"]')))
                    espera_aleatoria()
                    botao_avancar.click()
                    espera_aleatoria()
            except:
                print('Ocorreu algum problema ao adicionar mídias...')
            else:
                print('OK')
                try:
                    print('Escrevendo o texto...', end=' ')
                    # Escrevendo o texto
                    campo_texto = wait.until(expected_conditions.visibility_of_element_located((
                        By.XPATH, '//div[@aria-label="Editor de texto para criação de conteúdo"]')))
                    espera_aleatoria()
                    # digitar_devagar(campo_texto, texto)
                    campo_texto.send_keys(texto)
                    espera_aleatoria()
                except:
                    print('Ocorreu algum problema na publicação do texto.')
                else:
                    print('OK')
                    try:
                        print('Publicando o post...', end=' ')
                        # Publicando o post
                        botao_publicar = wait.until(expected_conditions.element_to_be_clickable((
                            By.XPATH, '//button[@class="share-actions__primary-action artdeco-button '
                                      'artdeco-button--2 artdeco-button--primary ember-view"]')))
                        espera_aleatoria()
                        botao_publicar.click()
                        espera_aleatoria()
                        driver.close()
                    except:
                        print('Ocorreu algum problema na publicação do post.')
                    else:
                        print('OK')
                        print('='*35)
                        print('Publicação efetuada com sucesso!')

