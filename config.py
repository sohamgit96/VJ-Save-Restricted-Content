import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25727177"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "13e78c472b61a64746fa8c587e09ab45")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sohamgangurde1996:HBEZ24jkoRGhGdUP@cluster0.oqrbp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
