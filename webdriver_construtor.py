"""Modulo com classe que instacia objeto Webdriver"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverManager:
    """Classe Pai que tem metodos básicos na execução do Webdriver"""
    def __init__(self, site: str, name_document: str):
        """
        :site: Link do site
        :name_document: Nome do arquivo que vai ser baixado
        :return: Driver e diretorio
        """
        self.driver = None
        self.diretorio = os.getcwd()
        self.site = site
        self.name_document = name_document
        

    def start_driver(self):
        """Inicia webdriver com todas as preferencias definidas"""
        if not self.driver:
            options = ChromeOptions()
            options.page_load_strategy = 'normal'  # Carrega a página por inteiro
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])  # Evita logs de Erro
            pref = {
                "download.default_directory": rf"{os.getcwd()}",  # Muda o local Default do Download
                "download.directory_upgrade": True,
                "download.prompt_for_download": False, }
            options.add_experimental_option(
                "prefs", pref)  # Adiciona as preferencias

            # Verifica e instala o webdriver (Pode ser um caminho do driver)
            # service = Service(executable_path='chromedriver.exe')
            service = Service(ChromeDriverManager().install())
            # Inicia o Webdriver com os parametros definidos
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get(self.site)  # Entra no site

    def get_driver(self):
        """Metodo get"""
        return self.driver

    def close_driver(self):
        """Fecha o driver caso de algo errado"""
        if self.driver:
            self.driver.quit()
            self.driver = None
            