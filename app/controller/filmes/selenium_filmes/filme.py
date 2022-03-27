# Orientar tudo ao objeto do selenium



import base64
from datetime import datetime
from random import choice, randint
from urllib import request

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
options.add_argument('--disable-dev-shm-usage') 
options.headless = True

class EscolhaFilme:
    filme = []
    
    def __init__(self, data, cidade):
        try:
            self.driver = webdriver.Chrome(options=options)  
            self.data = datetime.strptime(data, "%d%m%Y")
            self.cidade = cidade
        
        except WebDriverException:
            raise Exception("Erro com o ChromeDriver")
    
    def pagina(self):
        # Configurando Url
        url = f"https://www.ingresso.com/filmes?city={self.cidade}&partnership=home&target=em-breve"
        self.driver.get(url)
    
    def btn_embreve(self):
        # Acessando Aba Em Breve
        self.driver.find_element_by_xpath('//*[@id="tab-coming-soon"]').click()
    
    def fechar_publicidade(self):
        try:
            btn_anucio = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="midia-presite"]/header/div/a'))
            )
            btn_anucio.click()
        except:
            pass
    
    def get_data_estreia(self, filme):
        filme_texto = filme.text
        filme_texto = filme_texto.split("\n")
        filme_data = filme_texto[0]
        return filme_data

    def filtro_data(self, data_estreia):
        try:
            data_estreia = datetime.strptime(data_estreia, "%d/%m/%Y")
            if data_estreia >= self.data:
                return True
            else:
                return False
        except:
            return False
        
    def get_filme_sorteado(self, filmes):
        qtd_filmes = len(filmes)
        filme_escolhido = randint(0, qtd_filmes - 1)
        filme_escolhido = filmes[filme_escolhido]
        return filme_escolhido
    
    def get_titulo_filme(self, filme):
        filme = filme.text
        filme = filme.split("\n")
        filme_titulo = filme[1]
        return filme_titulo
    
    def get_elemento_filme(self, filme):
        return filme
    
    def filmes_sorteio(self):
        filmes = self.driver.find_elements_by_xpath('//*[@id="coming-soon"]/ul/li')
        for filme in filmes:
            filme_data = self.get_data_estreia(filme)
            filtro_data = self.filtro_data(filme_data)
            if not filtro_data:
                filme_fora_da_data = filmes.index(filme)
                filmes.pop(filme_fora_da_data)
        
        return filmes
        
    def filme_selecionado(self):
        filmes = self.filmes_sorteio()
        filme_ecolhido = self.get_filme_sorteado(filmes)
        titulo = self.get_titulo_filme(filme_ecolhido)
        data = self.get_data_estreia(filme_ecolhido)
        elemento = self.get_elemento_filme(filme_ecolhido)
        self.filme = {"titulo":titulo,"data":data, "elemento":elemento} 
    
    def filme_pagina(self):
        filme = self.filme["elemento"]
        self.filme.pop("elemento")
        filme.click()
    
    def sinopse(self):
        # Obtendo sinopse e adicionando ao Json
        sinopse = self.driver.find_element_by_xpath('//div [@class="no-result-details"]/ul/p')
        sinopse = sinopse.text
        self.filme["sinopse"] = sinopse
    
    def diretor(self):
        # Obtendo diretor e adicionando ao Json
        # diretor = self.driver.find_element_by_xpath('//div [@class="no-result-details"]/ul/li/span[@itemprop="director"]')
        diretor = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div [@class="no-result-details"]/ul/li/span[@itemprop="director"]'))
        )
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
    
    def capa(self):
        capa = self.driver.find_element_by_xpath('//img [@class="pb-avatar-image akamai-img-manager"]')
        # Obtendo Url da imagem
        capa_url = capa.get_property("src")
        # Definindo local para imagem
        local = 'app/static/images/capa.png'
        # Download da imagem
        request.urlretrieve(capa_url, local)
        
        # Convetendo imagem em Base64
        with open(local, "rb") as imagem: 
            capa_base64 = base64.b64encode(imagem.read())
        # Adicionando ao Json
        self.filme["capa"] = str(capa_base64)
    
    def filme_dados(self):
        # Retornando filme sorteado
        return self.filme
    
    def sair(self):
        self.driver.close()
