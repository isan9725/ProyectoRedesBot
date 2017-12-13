#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
from telegram.ext import*
from email.mime.text import MIMEText
from smtplib import SMTP

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

def sendEmail(bot, update, args):
    if len(args) == 1:
        from_address = "isan.09725@gmail.com"
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

        smtp.login(from_address, "CanutoyCornamenta")

        smtp.sendmail(from_address, to_address, mime_message.as_string())
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
    updater.dispatcher.add_handler(CommandHandler('sendEmail', sendEmail, pass_args= True))
    #updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
