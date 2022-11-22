from main import db
class Veiculos(db.Model):
    chassi = db.Column(db.String(17), primary_key=True)
    modelo = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    placa = db.Column(db.String(7))
    nome = db.Column(db.String(20))
    cpfcnpj = db.Column(db.String(20))
    telefone = db.Column(db.String(11))
    cep = db.Column(db.String(10))
    def __repr__(self):
        return '<Name %r>' % self.name

class Cliente(db.Model):
    nome = db.Column(db.String(20), primary_key=True, nullable=False)
    chassi = db.Column(db.String(17), nullable=False,)
    cpfcnpj = db.Column(db.String(20), nullable=False,)
    telefone = db.Column(db.String(11), nullable=False,)
    cep = db.Column(db.String(10), nullable=False,)
    def __repr__(self):
        return '<Name %r>' % self.name   
class OrdemServico(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kilometragem = db.Column(db.Integer, nullable=False,)
    datadeemissão = db.Column(db.String(10), nullable=False,)
    datadefechamento = db.Column(db.String(10), nullable=False,)
    chassi = db.Column(db.String(17), nullable=False,)
    descricao = db.Column(db.String(500), nullable=False,)
    def __repr__(self):
        return '<Name %r>' % self.name 
class Usuario(db.Model):
    nickname = db.Column(db.String(15), nullable=False)
    nome = db.Column(db.String(50), nullable=False, primary_key=True)
    senha = db.Column(db.String(100), nullable=False,)
    categoria = db.Column(db.String(6), nullable=False,)
    def __repr__(self):
        return '<Name %r>' % self.name   
