#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import _mysql_exceptions
import os
import sys
import time
import numbers
import subprocess
import telegram
from telegram.ext import*
from email.mime.text import MIMEText
from smtplib import SMTP

import client

ID = 348072664


##############################

# Funcion para realizar llamadas del sistema (ejecutar comandos Linux)
def llamadaSistema(entrada):
    salida = ""  # Creamos variable vacia
    f = os.popen(entrada)  # Llamada al sistema
    for i in f.readlines():  # Leemos caracter a caracter sobre la linea devuelta por la llamada al sistema
        salida += i  # Insertamos cada uno de los caracteres en nuestra variable
    salida = salida[:-1]  # Truncamos el caracter fin de linea '\n'

    return salida  # Devolvemos la respuesta al comando ejecutado


##############################

def help(bot, update):
    update.message.reply_text("Lista de comandos implementados: \n\n/start - Comando de inicio\n\n/help - Consulta la lista de comandos implementados y la descripcion de estos\n\n/commands - Consulta de forma rapida la lista de comandos implementados\n\n"
                              "/hello - manda un saludo con el nombre del usuario que solicito el comando\n\n/sendEmail -  le enviara un correo a la direccion que ponga como correo electronico\n\n"
                              " ")

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def start(bot, update):
    update.message.reply_text("Este bot se encargara de hacer que pasemos redes :v")

def commands(bot, update):
    update.message.reply_text("Lista de comandos implementados: \n/start\n/help\n/commands\n/hello\n/sendEmail")

def getDataLog(bot, update):
    client
    update.message.reply_text("")

def fecha(bot, update):
    if update.message.chat_id == ID :
        fecha = llamadaSistema("date")
        update.message.reply_text(fecha)


def sendEmail(bot, update, args):
    if len(args) == 1:
        from_address = "botproyectoredes.2017@gmail.com"
        to_address = args[0]
        message = "Hello, world! xD"

        mime_message = MIMEText(message, "plain")
        mime_message["From"] = from_address
        mime_message["To"] = to_address
        mime_message["Subject"] = "Correo de prueba"

        smtp = SMTP("smtp.gmail.com", 587)

        smtp.ehlo()
        smtp.starttls()

        smtp.login(from_address, "#RyS$$Lc0nexi0n")

        smtp.sendmail(from_address, to_address, mime_message.as_string())
        update.message.reply_text('Correo enviado')
        smtp.close()
        smtp.quit()

        #update.message.reply_text("Correo enviado")
    else:
        update.message.reply_text("Necesita debe especificar la direccion email a la que desea enviar el correo.")

# Manejador correspondiente al comando /red_conectada
def red_conectada(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        ssidred = llamadaSistema("iwgetid") # Llamada al sistema
        update.message.reply_text(ssidred) # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /ip
def ip(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        ip = llamadaSistema("hostname -I") # Llamada al sistema
        ip = ip[:-1] # Eliminamos el ultimo caracter
        update.message.reply_text(ip) # Respondemos al comando con el mensaje


# Manejador correspondiente al comando /drivers
def drivers(bot, update):
    if update.message.chat_id == ID:  # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _lsmod = llamadaSistema("lsmod")  # Llamada al sistema
        update.message.reply_text(_lsmod)  # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /pwd
def pwd(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _pwd = llamadaSistema("pwd") # Llamada al sistema
        update.message.reply_text(_pwd) # Respondemos al comando con el mensaje


# Manejador correspondiente al comando /cd
def cd(bot, update, args):
    if update.message.chat_id == ID:  # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        if len(args) == 1:  # Comprobar si el comando presenta argumento o no
            directorio = args[0]
            os.chdir(directorio)
            update.message.reply_text("Cambiando al directorio " + directorio)  # Respondemos al comando con el mensaje
        else:
            update.message.reply_text(
                "Se debe especificar el directorio al que acceder.\n\nEjemplo:\n/cd /home/usuario")  # Respondemos al comando con el mensaje
# Manejador correspondiente al comando /ls
def ls(bot, update, args):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        if len(args) == 1: # Comprobar si el comando presenta argumento o no
            _ls = llamadaSistema("ls " + args[0]) # Llamada al sistema
        else:
            _ls = llamadaSistema("ls") # Llamada al sistema
        update.message.reply_text(_ls) # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /montajes
def montajes(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _df = llamadaSistema("df") # Llamada al sistema
        update.message.reply_text(_df) # Respondemos al comando con el mensaje


# Manejador correspondiente al comando /borrar
def borrar(bot, update, args):
    if update.message.chat_id == ID:  # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        if len(args) == 1:  # Comprobar si el comando presenta argumento o no
            archivo = args[0]
            llamadaSistema("rm -rf " + args[0])  # Llamada al sistema
            update.message.reply_text("Archivo " + archivo + " borrado")  # Respondemos al comando con el mensaje
        else:
            update.message.reply_text(
                "Especifica un archivo.\n\nEjemplo:\n/borrar /home/user/archivo.txt")  # Respondemos al comando con el mensaje


# Manejador correspondiente al comando /cat
def cat(bot, update, args):
	if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
		if len(args) == 1: # Comprobar si el comando presenta argumento o no
			_cat = llamadaSistema("cat " + args[0]) # Llamada al sistema
			num_caracteres_fichero = len(_cat) # Determinamos el numero de caracteres que tiene el archivo
			if num_caracteres_fichero < 4096: # Si el numero de caracteres es menor a 4096 se envia un unico mensaje con todo el contenido
				update.message.reply_text(_cat) # Respondemos al comando con el mensaje
			else: # Si el numero de caracteres es superior a 4096, se divide el contenido del archivo en diversos fragmentos de texto que se enviaran en varios mensajes
				num_mensajes = num_caracteres_fichero/float(4095) # Se determina el numero de mensajes a enviar
				if isinstance(num_mensajes, numbers.Integral) != True: # Si no es un numero entero (es decimal)
					num_mensajes = int(num_mensajes) + 1 # Se aumenta el numero de mensajes en 1
				fragmento = 0
				for i in range(0, num_mensajes): # Se van enviando cada fragmento de texto en diversos mensajes
					mensaje = _cat[fragmento:fragmento+4095].decode('utf-8', 'ignore') # Creamos un mensaje correspondiente al fragmento de texto actual
					update.message.reply_text(mensaje) # Respondemos al comando con el mensaje
					fragmento = fragmento + 4095 # Aumentamos el fragmento de texto (cursor de caracteres)
		else:
			update.message.reply_text("Especifica un archivo.\n\nEjemplo:\n/cat /home/user/archivo.txt") # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /ssh_on
def ssh_on(bot, update):
	if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
		llamadaSistema("/etc/init.d/ssh start") # Llamada al sistema
		update.message.reply_text("Iniciando servidor SSH") # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /ssh_off
def ssh_off(bot, update):
	if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
		llamadaSistema("/etc/init.d/ssh stop") # Llamada al sistema
		update.message.reply_text("Deteniendo servidor SSH") # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /ssh_reiniciar
def ssh_reiniciar(bot, update):
	if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
		llamadaSistema("/etc/init.d/ssh restart") # Llamada al sistema
		update.message.reply_text(respuesta) # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /ssh_estado
def ssh_estado(bot, update):
	if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
		respuesta = llamadaSistema("/etc/init.d/ssh status") # Llamada al sistema
		update.message.reply_text(respuesta) # Respondemos al comando con el mensaje

# Manejador correspondiente al comando /buscar
def buscar(bot, update, args):
	if update.message.chat_id == ID: # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
		if len(args) == 2: # Si el comando presenta 2 argumentos
			nombre_archivo = args[0]
			ruta = args[1]
			resultado = llamadaSistema("find " + ruta + " -name '*" + nombre_archivo + "*'") # Llamada al sistema
			update.message.reply_text("Archivos encontrados para el termino de busqueda:\n\n'" + resultado) # Respondemos al comando con el mensaje
		else:
			update.message.reply_text("Se debe especificar el archivo y el directorio desde el que buscar.\n\nEjemplo:\n/buscar .log /") # Respondemos al comando con el mensaje

#Comando correspondiente para free en linux
def free(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _df = llamadaSistema("free") # Llamada al sistema
        update.message.reply_text(_df) # Respondemos al comando con el mensaje

def ipconfig(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _df = llamadaSistema("ipconfig") # Llamada al sistema
        update.message.reply_text(_df) # Respondemos al comando con el mensaje

def last(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _df = llamadaSistema("last") # Llamada al sistema
        update.message.reply_text(_df) # Respondemos al comando con el mensaje

def netstat(bot, update):
    if update.message.chat_id == ID : # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        _df = llamadaSistema("netstat") # Llamada al sistema
        update.message.reply_text(_df) # Respondemos al comando con el mensaje

def sftp(bot, update, args):
    if update.message.chat_id == ID:  # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        if len(args) == 1:  # Comprobar si el comando presenta argumento o no
            dispositivo = args[0]
            llamadaSistema("sftp " + args[0])  # Llamada al sistema
            #update.message.reply_text("Archivo " + dispositivo + " borrado")  # Respondemos al comando con el mensaje
        else:
            update.message.reply_text(
                "Especifica una maquina_remota ip")  # Respondemos al comando con el mensaje

def traceroute(bot, update, args):
    if update.message.chat_id == ID:  # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        if len(args) == 1:  # Comprobar si el comando presenta argumento o no
            nombrehost_ip = args[0]
            llamadaSistema("traceroute " + args[0])  # Llamada al sistema
            update.message.reply_text("traceroute: " + nombrehost_ip )  # Respondemos al comando con el mensaje
        else:
            update.message.reply_text(
                "Especifica una maquina_remota ip")  # Respondemos al comando con el mensaje


def coneccionMySQL(bot, update):
    db_host = 'localhost'
    usuario = 'root'
    contraseña = '12345'
    base_de_datos = 'proyectoredesbot'

    db = MySQLdb.Connect(host = "localhost", user = "root", passwd = "12345", database = "proyectoredesbot")

    cursor = db.cursor()

    #Alta de Inventario
    sql = "INSERT INTO inventariomaquinas VALUES "
    #sql+="(" + "'" + nombre + "'," + "'" + ipmaquina + "'," + "'" + macadress + "'," + "'" + discoduro + "'," + "'" + version + "'," + "'" + ram + "'," + "'" + procesador + "'" + ")"
    sql+="(null,'isra','192.168.228.10','64:27:37:9B:BB:47','120gb','1.2','4gb','intel 3')"

    cursor.execute(sql)

    db.autocommit()

    cursor.close()
    update.message.reply_text("Agregado a la base de datos")




def main():
    # se crea el updateer con el Token especifico de nuestro bot
    updater = Updater("472695035:AAGM2Ws9MGWoqs2d3Xb5CVglJaGoJK2376w")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('commands', commands))
    updater.dispatcher.add_handler(CommandHandler('getdatalog', getDataLog))
    updater.dispatcher.add_handler(CommandHandler('sendEmail', sendEmail, pass_args= True))
    updater.dispatcher.add_handler(CommandHandler("fecha", fecha))
    updater.dispatcher.add_handler(CommandHandler("ip", ip))
    updater.dispatcher.add_handler(CommandHandler("ls", ls, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("red_conectada", red_conectada))
    updater.dispatcher.add_handler(CommandHandler("pwd", pwd))
    updater.dispatcher.add_handler(CommandHandler("drivers", drivers))
    updater.dispatcher.add_handler(CommandHandler("cd", cd, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("montajes", montajes))
    updater.dispatcher.add_handler(CommandHandler("borrar", borrar, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("cat", cat, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("ssh_on", ssh_on))
    updater.dispatcher.add_handler(CommandHandler("ssh_off", ssh_off))
    updater.dispatcher.add_handler(CommandHandler("ssh_reiniciar", ssh_reiniciar))
    updater.dispatcher.add_handler(CommandHandler("ssh_estado", ssh_estado))
    updater.dispatcher.add_handler(CommandHandler("buscar", buscar, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("free", free))
    updater.dispatcher.add_handler(CommandHandler("ipconfig", ipconfig))
    updater.dispatcher.add_handler(CommandHandler("last", last))
    updater.dispatcher.add_handler(CommandHandler("netstat", netstat))
    updater.dispatcher.add_handler(CommandHandler("sftp", sftp, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("traceroute", traceroute, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("coneccionMySQL", coneccionMySQL))
    #updater.dispatcher.add_error_handler(error)

    # Imicio del Bot
    updater.start_polling()

    # El bot se ejecuta hasta que se el archivo se detenga o se preciona CTRL + C
    updater.idle()


if __name__ == '__main__':
    main()
