from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Preencher com os dados do computador local utilizado
USER = ""
PASSWORD = ""
HOST = ""
PORT = ""
DATABASE_URL = f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/Banco_Universidade"

engine = create_engine(DATABASE_URL) # Cria a conexão entre com o banco a partir da URL 
Session = sessionmaker(bind= engine) # Por meio da session podemos fazer queries no nosso banco
