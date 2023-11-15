"""Modulo com classe filha de WebDriverManager e
com metodo que contém passos de interação"""
import os
import time
from selenium.webdriver.common.by import By
from webdriver_construtor import WebDriverManager


class Drive(WebDriverManager):
    """
    Classe filha do WebDriverManager
    """
    def __init__(self, site: str, name_document: str):
        super().__init__(site, name_document)

    def exec_rda(self):
        """
        Acessa a uma página web e executa os passos
        """
        self.start_driver()  # Inicio o driver
        driver = self.get_driver()  # Salva o objeto na variavel
        elementos = {
            'buttons':{
                'download':'/html/body/div[3]/div[4]/div/div[3]/div[2]/div[2]/div[3]'
            }
        }

        arquivo = f'{self.diretorio}\\{self.name_document}'  # Atributo 1
        if os.path.isfile(arquivo):  # Verifica se o arquivo existe
            os.remove(arquivo)  # Exclui o arquivo

        time.sleep(5)
        driver.find_element(By.XPATH,elementos['buttons']['download']).click()  # Encontra e clica no elemento
        time.sleep(10)
        driver.quit()  # Fecha o driver
