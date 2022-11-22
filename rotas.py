from flask import render_template,request, redirect, url_for, flash,session
from main import app, db
from models import  Veiculos, Usuario, Cliente
from helpers import FormularioVeiculo, FormularioUsuario, FormularioCliente
from timez import pegar_tempo_atual


@app.route('/')
def inicio():
    lista = Veiculos.query.order_by(Veiculos.chassi)
    horas = pegar_tempo_atual()
    listacliente = Cliente.query.order_by(Cliente.chassi)
    form = FormularioVeiculo()
    return render_template('inicio.html', titulo='OFICINA', veiculos=lista, horas=horas, listacliente=listacliente, form=form)
@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuario.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
        if form.senha.data == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(url_for('cadastrarnovoveiculo'))
        else:
            flash('Usuario não aceito')
            return redirect(url_for('inicio'))
@app.route('/cadastrarveiculo')
def cadastrarnovoveiculo():
    form = FormularioVeiculo()
    form2 = FormularioCliente()
    return render_template('cadastrarVeiculo.html', form=form, form2=form2)
@app.route('/novoveiculo', methods=['POST',])
def novoveiculo():
    form = FormularioVeiculo(request.form)
    if not Veiculos.query.filter_by(chassi=form.chassi.data).first():
        chassi = form.chassi.data
        modelo = form.modelo.data
        placa = form.placa.data
        ano = form.ano.data
        nome = form.nome.data
        cpfcnpj = form.cpfcnpj.data
        telefone = form.telefone.data
        cep = form.cep.data
        novo_usuario = Veiculos(chassi=chassi, modelo=modelo, placa=placa,ano=ano, cpfcnpj=cpfcnpj,telefone=telefone,cep=cep,nome=nome)
        
        db.session.add(novo_usuario)
        
        db.session.commit()
        flash('veículo adcionado com sucesso')
        return redirect(url_for('inicio'))
    else:
        flash('veículo já cadastrado')
        return redirect(url_for('login'))
@app.route('/resultadopesquisa', methods=['POST',])
def resultadopesquisa():
    form = FormularioVeiculo(request.form)
    chassi = form.chassi.data
    placa = form.chassi.data
    cpfcnpj = form.cpfcnpj.data
    nome = form.nome.data
    lista_de_veículos = Veiculos.query.filter_by(chassi=chassi).first()
    if not chassi:
        lista_de_veículos = Veiculos.query.filter_by(placa=placa).first()
        if not placa:
            lista_de_veículos = Veiculos.query.filter_by(cpfcnpj=cpfcnpj).first()
            if not cpfcnpj: 
                lista_de_veículos = Veiculos.query.filter_by(nome=nome).first()
                if not nome:
                    flash('data não encontrada')
                    return redirect(url_for('inicio'))
    if lista_de_veículos == None:
        flash('data não encontrada')
        return redirect(url_for('inicio'))                
    

    return render_template('resultadopesquisa.html', veiculo=lista_de_veículos)