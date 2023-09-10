from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
from random import randint, uniform


def iniciar_driver():
    chrome_options = Options()
    # chrome_options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    arguments = ['--lang=pt-BR', 'window-size=1300,1000',
                 '--user-data-dir=C:\\Users\\Daniel\\AppData\\Local\\Google\\Chrome\\User Data'
                 '--headless']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(
        driver,
        20,
        poll_frequency=1,  # frequencia q vai tentar fazer algo
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return wait, driver


def digitar_devagar(campo, msg):
    for letra in msg:
        espera_aleatoria(0.01, 0.5 / 100)
        campo.send_keys(letra)


def espera_aleatoria(inicio=2.5, fim=5.5):
    sleep(uniform(inicio, fim))


def ler_txt(nome_arquivo):
    """
    Essa função serve para ler arquivos de texto, guardando em uma variável e retornando esse texto.
    :param nome_arquivo: Podem ser passados o nome do arquivo ou o diretório e o nome do arquivo, separados por duplas
    barras invertidas. Deve ser passado como uma string, e com o formato .txt no final.
    Exemplo: 'texto_para_ler.txt' ou 'C:\\Users\\[seu_usuario]\\Documents\\texto_para_ler.txt'
    :return: retorna o texto que estava escrito no arquivo.txt
    """
    with open(nome_arquivo, 'r', encoding='UTF-8') as arquivo_texto:
        texto = arquivo_texto.read()
        return texto


if __name__ == '__main__':
    txt = ler_txt(nome_arquivo='texto_a_publicar.txt')
    print(txt)
