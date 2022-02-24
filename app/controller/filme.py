from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

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
        url = f"https://www.ingresso.com/filmes?city={self.cidade}&partnership=home&target=em-cartaz"
        self.driver.get(url)

    def filtro_data(self):
        # Obtendo e Filtrando lista de filmes pelas datas
        datas = self.driver.find_elements_by_xpath('//span [@class="tag tag-genre m-b-05"]')
        for data in datas:
            data = data.text
            data = datetime.strptime(data, "%d/%m/%Y")
            
            if self.data >= data:
                print(data)
            
    def sair(self):
        self.driver.close()
