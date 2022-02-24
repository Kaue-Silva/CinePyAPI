from datetime import datetime
from random import choice
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
        # Pegando o titulo de todos os filmes
        # e Adicionando a uma lista como objeto
        titulos = self.driver.find_elements_by_xpath('//ul [@class="movie-list-small"]/li/article/a[2]/div/h1')
        for titulo in titulos:
            titulo = titulo.text
            self.filmes.append({"titulo":titulo})
    
    def data_estreia(self):
        # Pegando a data de todos os filmes
        # e Adicionando a uma lista como objeto
        datas_estreia = self.driver.find_elements_by_xpath('//ul [@class="movie-list-small"]/li/article/a/div[2]/div/span')
        for i, data_estreia in enumerate(datas_estreia):
            data_estreia = data_estreia.text
            data_estreia_date = datetime.strptime(data_estreia, "%d/%m/%Y")
            if data_estreia_date >= self.data:
                self.filmes[i]["data_estreia"] = data_estreia
    
    def filtrar_filmes(self):
        filmes = []
        # Filtrando filmes por data
        for filme in self.filmes:
            if "data_estreia" in filme:
                filmes.append(filme)
        
        # Sorteando filme aleatorio
        self.filme = choice(filmes)
    
    # Entrando na pagina do filme sorteado
    def filme_pagina(self):
        filme_sorteado = self.filme['titulo']
        filme = self.driver.find_element_by_xpath(f'//h1 [text()="{filme_sorteado}"]')
        filme.click()
    
    def sinopse(self):
        # Obtendo sinopse e adicionando ao Json
        sinopse = self.driver.find_element_by_xpath('//div [@class="no-result-details"]/ul/p')
        sinopse = sinopse.text
        self.filme["sinopse"] = sinopse
    
    def diretor(self):
        # Obtendo diretor e adicionando ao Json
        diretor = self.driver.find_element_by_xpath('//div [@class="no-result-details"]/ul/li/span[@itemprop="director"]')
        diretor = diretor.text
        self.filme["diretor"] = diretor

    def genero(self):
        # Variavel acumuladora
        generos_text = ""
        # Generos do Filme
        generos = self.driver.find_elements_by_xpath('//div [@class="synopsis-tags hidden-sm-down stags-1"]')
        for genero in generos:
            # Obtendo genero em texto
            genero = genero.text
            # Concatenando generos
            generos_text += genero
        
        self.filme["generos"] = generos_text.title()
    
    def filme_dados(self):
        # Retornando filme sorteado
        return self.filme
    
    
    def sair(self):
        self.driver.close()

