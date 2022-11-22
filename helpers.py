from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField, IntegerField
class FormularioVeiculo(FlaskForm):
    chassi = StringField('chassi', [validators.DataRequired(), validators.Length(min=0,max=17)])
    modelo = StringField('modelo', [validators.DataRequired(), validators.Length(min=0,max=50)])
    ano = IntegerField('ano do veiculo', [validators.DataRequired(), validators.Length(min=0,max=4)])
    placa = StringField('placa', [validators.DataRequired(), validators.Length(min=0,max=7)])
    nome = StringField('nome', [validators.DataRequired(), validators.Length(min=0,max=20)])
    cpfcnpj = StringField('cpf ou cnpj', [validators.DataRequired(), validators.Length(min=0,max=20)])
    telefone = StringField('telefone', [validators.DataRequired(), validators.Length(min=0,max=11)])
    cep = StringField('cep', [validators.DataRequired(), validators.Length(min=0,max=10)])
    salvar = SubmitField('Salvar')
class FormularioUsuario(FlaskForm):
    nome = StringField('nome', [validators.DataRequired(), validators.Length(min=1,max=50)])
    nickname = StringField('nickname', [validators.DataRequired(), validators.Length(min=1,max=15)])
    senha = PasswordField('senha', [validators.DataRequired(), validators.Length(min=1,max=100)])
    categoria = StringField('categoria', [validators.DataRequired(), validators.Length(min=1,max=6)])
    salvar = SubmitField('Salvar')
class FormularioCliente(FlaskForm):
    nome = StringField('nome', [validators.DataRequired(), validators.Length(min=1,max=20)])
    chassi = StringField('chassi', [validators.DataRequired(), validators.Length(min=1,max=17)])
    cpfcnpj = StringField('cpf ou cnpj', [validators.DataRequired(), validators.Length(min=1,max=20)])
    telefone = StringField('telefone', [validators.DataRequired(), validators.Length(min=0,max=11)])
    cep = StringField('cep', [validators.DataRequired(), validators.Length(min=0,max=10)])
    salvar = SubmitField('Salvar')
class FormularioOrdemDeServico():
    kilometragem = IntegerField('kilometragem', [validators.DataRequired(), validators.Length(min=1,max=7)])
    chassi = StringField('chassi', [validators.DataRequired(), validators.Length(min=1,max=17)])
    descricao = StringField('descricao', [validators.DataRequired(), validators.Length(min=0,max=500)])
    salvar = SubmitField('Salvar')