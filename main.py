## está sem usuário e senha do IG
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from funcoes import cria_lista_usuarios_unicos
from funcoes import sorteia_usuario
from flask import Flask, render_template, request


app=Flask('SorteioInstagram')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/result')
def result():
  url=request.args.get('url')
  quantidade_vencedores=request.args.get('quantosvencedores')
  print(url)
  print(quantidade_vencedores)

  lista_usuarios=cria_lista_usuarios_unicos(url)
  sorteado=sorteia_usuario(lista_usuarios)
  
  return render_template('result.html',sorteio=sorteado)


app.run(host='0.0.0.0')
