SECRET_KEY = 'teste'

SQLALCHEMY_DATABASE_URI= \
'{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario ='root',
    senha='Macaviga_2442',
    servidor='localhost',
    database='oficina' 
)
SQLALCHEMY_TRACK_MODIFICATIONS= False