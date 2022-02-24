from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import (StaleElementReferenceException,
                                        WebDriverException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configurações Selenium
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--ignore-certificate-errors")
options.headless = False


class EscolhaFilme:
    filmes = []
    
    # Inicializando Selenium
    def __init__(self, data, cidade):
        try:
            self.driver = webdriver.Chrome(options=options)
            self.data = data  
            self.cidade = cidade
        except WebDriverException:
            raise Exception("Erro com o ChromeDriver")
    
    # Acessando Pagina
    def pagina(self):
        # Configurando Url
        url = f"https://www.ingresso.com/filmes?city={self.cidade}&partnership=home&target=em-breve"
        self.driver.get(url)

    def titulo(self):
        titulos = self.driver.find_elements_by_xpath('//ul [@class="movie-list-small"]/li/article/a[2]/div/h1')
        for titulo in titulos:
            titulo = titulo.text
            self.filmes.append({"titulo":titulo})
    
    def sair(self):
        self.driver.close()

