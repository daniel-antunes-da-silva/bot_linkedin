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
                 '--user-data-dir=C:\\Users\\Daniel\\AppData\\Local\\Google\\Chrome\\User Data',
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
        10,
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
        sleep(randint(1, 5)/30)
        campo.send_keys(letra)


def espera_aleatoria(inicio=2.5, fim=6.5):
    sleep(uniform(inicio, fim))
