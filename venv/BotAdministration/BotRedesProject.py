#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
from telegram.ext import*
from email.mime.text import MIMEText
from smtplib import SMTP

import client

def help(bot, update):
    update.message.reply_text("Lista de comandos implementados: \n\n/start - Comando de inicio\n\n/help - Consulta la lista de comandos implementados y la descripcion de estos\n\n/commands - Consulta de forma rapida la lista de comandos implementados\n\n"
                              "/hello - manda un saludo con el nombre del usuario que solicito el comando\n\n/sendEmail -  le enviara u correo al WEON "
                              "de rudy por ahora xD")

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

def ls(bot, update, args):
    if update.message.chat_id == ID :
        if len(args) == 1:
            _ls = llamadaSistema("ls " + args[0])
        else:
            _ls = llamadaSistema("ls")
        update.message.reply_text(_ls)

def ssh_estado(bot, update):
    if update.message.chat_id == ID :
        respuesta = llamadaSistema("/etc/init.d/ssh status")
        update.message.reply_text(respuesta)

def ip(bot, update):
    if update.message.chat_id == ID :
        ip = llamadaSistema("hostname -I")
        ip = ip[:-1]
        update.message.reply_text(ip)

def sendEmail(bot, update, args):
    if len(args) == 1:
        from_address = "botproyectoredes.2017@gmail.com"
        to_address = args[0]
        message = "Hello, world!"

        mime_message = MIMEText(message, "plain")
        mime_message["From"] = from_address
        mime_message["To"] = to_address
        mime_message["Subject"] = "Correo de prueba"

        if("gmail.com" in args[0]):
            smtp = SMTP("smtp.gmail.com", 587)
        elif("@hotmail.com" in args[0]):
            smtp = SMTP("smtp.live.com", 587)
        else:
            update.message.reply_text("No se reconce el correo electronico")

        smtp.ehlo()
        smtp.starttls()

        smtp.login(from_address, "#RyS$$Lc0nexi0n")

        smtp.sendmail(from_address, to_address, mime_message.as_string())
        update.message.reply_text('Correo enviado')
        smtp.close()
        smtp.quit()

        update.message.reply_text("Correo enviado")
    else:
        update.message.reply_text("Necesita debe especificar la direccion email a la que desea enviar el correo.")

def main():
    # Create the Updater and pass it your bot's token.
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
    updater.dispatcher.add_handler(CommandHandler("ssh_estado", ssh_estado))
    #updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
