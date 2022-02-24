# CinePy
## Descrição
API Construida em Python

Sua intenção e Sortear o filme baseado nas suas preferencias

## Tecnologias Utilizadas
- Flask
- Selenium
- Docker
- Docker Compose

## Como Iniciar API
Necessario Inicializar Docker e Ter o Git
``` bash
    # Clonando Repositorio
    git clone https://github.com/Kaue-Silva/CinemaPyAPI.git
    # Constroi Container
    docker-compose up --build
```

## Como Usar a API
Fazemos um Request do Tipo GET na URL,
Passando Sua Cidade e uma Data 
Lembrando que os Espaços no Nome da Cidade Devem Conter um Traço, Exemplo: rio-de-janeiro e 
a Data Devera ir Sem Barras e no Padrão Brasileiro Exemplo: 20042022,
Só Seram Sorteado os Filmes que Vão Estrear na Mesma Data ou Após
e é Claro só os Que Estarão Disponiveis na Sua Cidade.

### Rotas
- Rodando Localmente
- - Metodo GET
- - http://127.0.0.1:5000/api/cinepy/escolha_filme?cidade=DIGITE SUA CIDADE AQUI &data=SUA DATA AQUI

- Rodando no Servidor
- - Metodo GET
- - http://127.0.0.1:5000/api/cinepy/escolha_filme?cidade=cidade&data=data

### Exemplo de Retorno
``` JSON
{
    "capa": "BASE64 Omtido por Ser Muito Grande",
    "data_estreia": "22/06/2022",
    "diretor": "Baz Luhrmann",
    "generos": "Drama",
    "sinopse": "O filme aborda a vida e a música de Elvis Presley sob o prisma da sua tumultuada relação com seu empresário enigmático, o coronel Tom Parker. A história mergulha na complexa dinâmica entre Presley e Parker, que se estendeu por mais de 20 anos, desde a ascensão de Presley à fama até seu estrelato sem precedentes, tendo como pano de fundo a evolução da paisagem cultural e a perda da inocência na América. No centro dessa jornada está uma das pessoas mais importantes e influentes na vida de Elvis, Priscilla Presley",
    "titulo": "Elvis"
}
```



## Hospedado
- Heroku (Em Breve)

https://www.linkedin.com/in/kaue-silva2004/
