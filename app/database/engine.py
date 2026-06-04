from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Tem que preencher isso aqui de acordo com o PC que vai ter o banco de dados, ai a gente ve melhor isso
USER = ""
PASSWORD = ""
HOST = ""
PORT = ""
DATABASE_URL = f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/Banco_Universidade"

engine = create_engine(DATABASE_URL) # Cria a conexão entre com o banco a partir da URL 
Session = sessionmaker(bind= engine) # Por meio da session podemos fazer queries no nosso banco
