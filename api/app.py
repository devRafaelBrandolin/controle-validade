from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

#Dicionarios
aves = {
    "Frango Inteiro":6181,
    "Asa de Frango":1944,
    "Peito c/ Osso":1948,
    "Coxa Sobre Coxa":1949,
    "Filé de Peito":1947,
}

temps = {
    "Frango Passarinho":2912,
    "Coxinha da Asa":2911,
    "Peito s/ Osso":2908,
    "Filé de Coxa Sobre Coxa":3314,
    "Meio da Asa (Tulipa)":3794,
    "Sobre Coxa":2910,
}

#Funçoes
def localizar_dic(dic, value):
    for chave, valor_atual in dic.items():
        if valor_atual == value:
            return chave
    #se nao encontrado
    return None

#getdata
def getdata():
    data_atual = datetime.now()
    atual = data_atual.strftime("%d/%m/%Y")
    return atual
#criar a 1°pagina do site
#route -> site.com/pagina
#funçao -> oque vai aparecer na pagina
#template

@app.route("/")
def homepage():
    return render_template("homepage.html")
#----------------------------------------------------------------------------------------
#-----------------------menu de lançamento-----------------------------------------------
@app.route("/add")
def pag_add():
    id_item = aves["Frango Inteiro"]
    name_item = localizar_dic(aves, 6181) 
    hoje = getdata() 
    return render_template("add.html", hoje=hoje, id_item=id_item, name_item=name_item)
#----------------------------------------------------------------------------------------
@app.route("/menu-aves")
def pag_menu_aves():
    btn_01 = localizar_dic(aves, 6181)
    btn_02 = localizar_dic(aves, 1944)
    btn_03 = localizar_dic(aves, 1948)
    btn_04 = localizar_dic(aves, 1949)
    btn_05 = localizar_dic(aves, 1947)
    return render_template("menu-aves.html", btn_01=btn_01, btn_02=btn_02, btn_03=btn_03, btn_04=btn_04, btn_05=btn_05)

@app.route("/6181")
def pag_6181():
    id_item = aves["Frango Inteiro"]
    name_item = localizar_dic(aves, 6181) 
    return render_template("aves/6181.html", id_item=id_item, name_item=name_item)

@app.route("/1944")
def pag_1944():
    id_item = aves["Asa de Frango"]
    name_item = localizar_dic(aves, 1944) 
    return render_template("aves/1944.html", id_item=id_item, name_item=name_item)

@app.route("/1948")
def pag_1948():
    id_item = aves["Peito c/ Osso"]
    name_item = localizar_dic(aves, 1948) 
    return render_template("aves/1948.html", id_item=id_item, name_item=name_item)

@app.route("/1949")
def pag_1949():
    id_item = aves["Coxa Sobre Coxa"]
    name_item = localizar_dic(aves, 1949) 
    return render_template("aves/1949.html", id_item=id_item, name_item=name_item)

@app.route("/1947")
def pag_1947():
    id_item = aves["Filé de Peito"]
    name_item = localizar_dic(aves, 1947) 
    return render_template("aves/1947.html", id_item=id_item, name_item=name_item)
#----------------------------------------------------------------------------------------
@app.route("/menu-temperados")
def pag_menu_temperados():
    btn_t01 = localizar_dic(temps, 2912)
    btn_t02 = localizar_dic(temps, 2911)
    btn_t03 = localizar_dic(temps, 2908)
    btn_t04 = localizar_dic(temps, 3314)
    btn_t05 = localizar_dic(temps, 3794)
    btn_t06 = localizar_dic(temps, 2910)
    return render_template("menu-temperados.html", btn_t01=btn_t01, btn_t02=btn_t02, btn_t03=btn_t03, btn_t04=btn_t04, btn_t05=btn_t05, btn_t06=btn_t06)

@app.route("/menu-linguicas")
def pag_menu_linguicas():
    return render_template("menu-linguicas.html")

@app.route("/menu-bovinos")
def pag_menu_bovinos():
    return render_template("menu-bovinos.html")


#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)