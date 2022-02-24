from flask import Flask

# Instancia Flask
app = Flask(__name__)

# Configurações Flask
app.config.from_object("config")
