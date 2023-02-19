import telegram                             
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,Location
from telegram.ext import Updater, MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
import os.path
import logging
import json
import threading
import time
import pandas as pd

TOKEN = "1816509295:AAH0OIUDdQT-Lwr81Y_1yGPO8Sy5Ukt6dDA"                                            # Token del Bot Wobet Calculadora
modo = 0
operacion = ""

MENU = [['¿Qué es Wobet?  \U0001F525', '¿Prueba gratis?   \U0001F525'],['Rentabilidad \U0001F525', '¿Principiante?  \U0001F525'],['Comisión por recarga \U0001F525']]
MENU1 = [['¿Cómo funciona?   \U0001F525', '¿Porque elegirnos?  \U0001F525'],['No he encontrado la respuesta \U0001F525', '¡Síguenos! \U0001F525'],['Atrás  \U00002B05']]
MENU2 = [['¿Planes Wobet?  \U0001F525', 'Cómo se paga la suscripción?  \U0001F525'],['¿Es prematch y live?  \U0001F525', 'Ya pagué, ¿ahora qué hago?   \U0001F525'],['Atrás  \U00002B05']]
MENU3 = [['Promedio de ganancia por señal  \U0001F525', 'Mayor capital, mayor ganacia  \U0001F525'],['¿Cuantas casas? \U0001F525', 'Atrás  \U00002B05']]
MENU4 = [['¿Cómo gano?   \U0001F525', '¿Cómo calculo las operaciones?  \U0001F525'],['¿Cuál es la base de datos?  \U0001F525', '¿Con cuanto debo empezar?  \U0001F525'],['Atrás  \U00002B05']]
MENU5 = [['¿Cómo funciona?    \U0001F525', '¿Menos limitaciones?  \U0001F525'],['¿Cuántas recargas diarias?  \U0001F525', 'Ejemplo  \U0001F525'],['Atrás  \U00002B05']]

usuarios = {}
nuevosUsuarios = []

def start(update, context):
    idChat = update.message.chat_id
    if idChat in usuarios.keys():
        # El usuario ya se encuentra registrado en el sistema 
        x = usuarios[idChat]
        if x[0] == 0:
            context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
            context.bot.send_message(chat_id=idChat, text="Hola soy Luck, ¡Estoy aquí para resolver tus dudas! 🐦 ")
            menuBotones = telegram.ReplyKeyboardMarkup(MENU)
            context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
        elif x[0] == 1:
            context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
            context.bot.send_message(chat_id=idChat, text="Hola soy Luck, ¡Estoy aquí para resolver tus dudas! 🐦 ")
            menuBotones = telegram.ReplyKeyboardMarkup(MENU)
            context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
        elif x[0] == 2:
            x[0] = 1
            usuarios[idChat] = x
            #guardando diccionario en archivo.txt
            contenido = json.dumps(usuarios)
            archivo = open("registro.txt", "w")  
            archivo.write(contenido)
            archivo.close()
            context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
            context.bot.send_message(chat_id=idChat, text="Hola soy Luck, ¡Estoy aquí para resolver tus dudas! 🐦 ")
            menuBotones = telegram.ReplyKeyboardMarkup(MENU)
            context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
          
    else:
        # El usuario va a registrarse
        context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=idChat, text="Hola soy Luck, ¡Estoy aquí para resolver tus dudas! 🐦 ")
        menuBotones = telegram.ReplyKeyboardMarkup(MENU)
        context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
       #Guardando diccionario en archivo.txt
        usuarios[idChat] = [1]
        contenido = json.dumps(usuarios)
        archivo = open("registro.txt", "w")  
        archivo.write(contenido)
        archivo.close()
           

def mensajes(update, context):
    global operacion, modo, operacion
    idChat = update.message.chat_id
    mensaje = update.message.text
    if idChat in usuarios.keys():
        x = usuarios[idChat]                                                                       # lee la lista cuyo primer elemento es el estado de la conversacion (0- espera codigo, 1- espera nombre, 2- usuario registrado)
        if x[0] == 1:
            x.append(mensaje)
            x[0] = 2
            
            if '¿Qué es Wobet?' in mensaje:
                context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                context.bot.send_message(chat_id=idChat, text="🔥 Somos un servicio de inversión segura que se preocupa por su comunidad y por eso ha generado esta gran oportunidad para cualquier tipo de público mayor de edad. Realizamos arbitraje deportivo dándole a nuestros usuarios las herramientas necesarias para operar correctamente y siempre ganar sin importar el resultado en cada operación")
                menuBotones = telegram.ReplyKeyboardMarkup(MENU1)
                context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                operacion = "1" 
            elif '¿Prueba gratis? ' in mensaje:
                context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                context.bot.send_message(chat_id=idChat, text="🔥 En Wobet primero esta nuestra comunidad, por eso nuestro plan gratis está abierto totalmente al público sin un tiempo definido de expiración, pero ten cuidado, ¡las ganancias no son nada a cuando ingresas y ganas en grande!")
                context.bot.send_message(chat_id=idChat, text="🔥 Este es el link del canal gratis https://t.me/WobetAcademy")
                menuBotones = telegram.ReplyKeyboardMarkup(MENU2)
                context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                operacion = "2"
            elif 'Rentabilidad' in mensaje:
                context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                context.bot.send_message(chat_id=idChat, text="🔥 La rentabilidad depende mucho de cada país o grupo al que vayas a ingresar, sin embargo, un promedio mensual es de por lo menos el 40% del capital que operas, un ejemplo muy sencillo es que si operas una señal que mueva todo tu capital con un porcentaje tan bajo como el 2% eso generaría un retorno de ganancia del 60% de tu capital en 30 días.")
                menuBotones = telegram.ReplyKeyboardMarkup(MENU3)
                context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                operacion = "3"
            elif '¿Principiante?'in mensaje:
                context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                context.bot.send_message(chat_id=idChat, text="🔥 Los pasos que debes seguir son muy sencillos, elige el plan que quieras tomar. En el momento de ingresar a nuestra comunidad un asesor se pondrá en contacto contigo donde se te hará entrega de todas las herramientas, ingreso al curso, al escáner y al grupo premium para que operes correctamente con explicación personalizada, y listo, ¡opera y gana!")
                menuBotones = telegram.ReplyKeyboardMarkup(MENU4)
                context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                operacion = "4"
            elif 'Comisión por recarga'in mensaje:
                context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                context.bot.send_message(chat_id=idChat, text="🔥 Esos son los porcentajes de comisión por cada casa de apuestas para usuarios Wobet, pero betplay únicamente aplica para los departamentos de Meta, Caldas, Boyacá y Amazonas, todas las demás casas de apuestas no tienen ninguna restricción y aplica para todo el territorio nacional, rushbet y betplay son clones ✅")
                with open('productos.jpg', 'rb') as photo_file:
                        context.bot.sendPhoto(chat_id=idChat, photo=photo_file)
                menuBotones = telegram.ReplyKeyboardMarkup(MENU5)
                context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                operacion = "5"

        elif x[0]==2:
            x[0] = 2
            
            if operacion == "1":
                if '¿Cómo funciona?' in mensaje:
                   
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Lo que nosotros hacemos es operar surebets que son apuestas seguras cubriendo todos los posibles resultados, proyectamos el mejor escáner del mercado el cual es betburguer las 24 horas todos los días, con diversidad de apuestas que nosotros hemos verificado que coincidan sus cuotas para operar correctamente. Guiamos a todos nuestros usuarios mediante un curso descriptivo, videos, herramientas propias y únicas de Wobet y del mercado, 3 instructores que estarán atentos de resolver todas tus dudas en cualquier momento, señales enviadas en un grupo Premium por cada país para que no dediques tanto tiempo diario y muchos más beneficios adicionales, así cada mes tienes un excelente servicio y una gran ganancia.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU1)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Porque elegirnos?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Una de las principales razones es la calidad-precio en Wobet te educamos y tienes asesoría constante, evitamos que pagues softwares costosos, cometas errores que salen en los mismos escáneres o casas de apuestas, y dediques horas largas de búsqueda con herramientas poco efectivas, te generamos libertad de tiempo y excelencia en el servicio a un precio menor.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU1)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'No he encontrado la respuesta' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Estos son los contactos de nuestro servicio al cliente en telegram ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @WobetFinanciero ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @Maicol_agudelo  ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @WilliamFuquene  ")
                    context.bot.send_message(chat_id=idChat, text="🔥 Si no encontraste tu respuesta aquí, puedes dirigirte con nuestro servicio al cliente en todas nuestras redes o enviar un correo a clientes@wobetacademy.com y resolveremos todas tus dudas.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU1)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¡Síguenos!' in mensaje:
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="https://beacons.page/wobetacademy")
                    with open('siguenos.jpg', 'rb') as photo_file:
                        context.bot.sendPhoto(chat_id=idChat, photo=photo_file)
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU1)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Atrás'in mensaje:
                    x[0] = 1
                    usuarios[idChat] = x
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
            
            if operacion == "2":
                if '¿Planes Wobet?' in mensaje:
                   
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Actualmente manejamos 2 planes en Wobet el básico y el estándar. En Standard te damos, la calculadora para Windows como programa, las 3 calculadoras en Excel para que puedas operar desde cualquier dispositivo, una base de datos automatizada solo escribes algunos datos y te va registrando todas tus operaciones, acceso a la transmisión del escáner prematch las 24 horas, curso descriptivo y videos, grupo premium donde enviamos las señales detallando como encontrarla en las casas de apuestas (2 p.m. a 10 p.m.) enviamos todo lo que nos muestre el escáner, para que los usuarios no tengan que dedicar tanto tiempo diariamente, 3 instructores prestos para ayudarte a solucionar todas tus dudas e inquietudes, y la comisión por recargas. ¡Y eso no es todo! Actualmente estamos dando la calculadora bot que ayuda a calcular tus operaciones en menos de 10 segundos, junto con la tabla de cuotas, dentro del plan Standard. En el plan básico tienes acceso al escáner, calculadora en Excel y el curso descriptivo.⭐️")
                    with open('planes.jpg', 'rb') as photo_file:
                        context.bot.sendPhoto(chat_id=idChat, photo=photo_file)
                    context.bot.send_message(chat_id=idChat, text="🔥 Luego de la primera compra, en sus renovaciones tendrán el 20% de descuento. Eso quiere decir que en las próximas renovaciones como ya tienes todas las herramientas y el curso, los planes te quedan fijos con un 20% menos, ya sea que quieras el plan básico o el estándar ✅")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU2)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Cómo se paga la suscripción?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Estos son nuestros métodos de pagos, es muy sencillo, solo escoges el de tu preferencia nacional o internacional y envías una captura a nuestra atención al cliente.")
                    with open('metodos.jpg', 'rb') as photo_file:
                        context.bot.sendPhoto(chat_id=idChat, photo=photo_file)
                    context.bot.send_message(chat_id=idChat, text="🔥 Estos son los contactos de nuestro servicio al cliente en telegram ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @WobetFinanciero ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @Maicol_agudelo  ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @WilliamFuquene  ")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU2)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Es prematch y live?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 A partir de mayo suspendimos live debido a que no está generando ningún tipo de resultados en todo el día, hay muy poco mercado y si sale alguna señal dura alrededor de 20 segundos máximo lo que hace que la mayoría de usuarios no operen y si operan cometan errores, así que no tiene sentido para nosotros vender un servicio que no está generando buenos resultados. Esperamos que todo se restablezca nuevamente y podamos volver a activar live para todos los países, por ahora seguimos trabajando con prematch que nos sigue produciendo excelentes retornos y ganancias diarias")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU2)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Ya pagué, ¿ahora qué hago?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Envíanos a servicio al cliente una captura de tu pago  realizado y te generaremos acceso inmediato.")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @WobetFinanciero ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @Maicol_agudelo  ")
                    context.bot.send_message(chat_id=idChat, text="\U00002733 @WilliamFuquene  ")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU2)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Atrás'in mensaje:
                    x[0] = 1
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)       

            if operacion == "3":
                if 'Promedio de ganancia por señal' in mensaje:
                   
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Muchos usuarios se interesan en la cantidad de señales que sale cada día, pero cuando ingresan a Wobet entienden que no es la cantidad sino el porcentaje y la liquidez de la apuesta, con una o dos señales diarias puede alcanzar incluso el 8% o 10% dependiendo de cómo se mueva el mercado. Sin embargo, si te sigue interesando la cantidad de señales diariamente, aunque no es recomendado operar tantas, cada día pueden salir 4, 5, 6 incluso más u otras veces menos, dependiendo mucho de cada país que es independiente por el movimiento.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU3)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Mayor capital, mayor ganacia' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Tal cual, tenemos usuarios que operan cifras bastante grandes por cada movimiento, como te puedes imaginar así mismo son las ganancias.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU3)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Cuantas casas?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Actualmente en Wobet contamos con diversidad de grupos, puedes optar por las casas de apuestas que mejor te parezcan, aunque después de realizar tu pago pide un asesoramiento, algunas casas de apuestas las evitamos.")
                    context.bot.send_message(chat_id=idChat, text="\U00002714 Grupo 1: Rivalo, Wplay, Codere, Betplay. ")
                    context.bot.send_message(chat_id=idChat, text="\U00002714 Grupo 2: Betsson, Inkabet, Apuestatotal, Doradobet, Solbet  ")
                    context.bot.send_message(chat_id=idChat, text="\U00002714 Grupo 3: Wplay, Betplay, Codere, Rivalo, Pinnacle, Bwin, Betfair.")
                    context.bot.send_message(chat_id=idChat, text="\U00002714 Grupo 4: Caliente, Playdoit, Bet365, Netbet, Ganabet, Codere. ")
                    context.bot.send_message(chat_id=idChat, text="\U00002714 Grupo 5: Bet365, Betsson, BetinAsia, Betfair, Titanbet. ")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU3)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Atrás'in mensaje:

                    x[0] = 1
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones) 
            
            if operacion == "4":
                if '¿Cómo gano?' in mensaje:
                   
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Es muy sencillo ganar con Wobet, simplemente tienes que registrarte en las diferentes casas de apuestas que utilizamos, fondearlas y operar correctamente como te lo indica nuestro equipo.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU4)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Cómo calculo las operaciones?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Cuando ingresas a hacer parte de Wobet, nuestro equipo te hará entrega de diferentes herramientas entre ellas la calculadora para Windows, Excel y nuestro bot que ayuda a calcular todo en menos de 10 segundos. Esta nos servirá para escribir las cuotas de las casas de apuestas y el capital que queremos invertir en cada operación y nos mostrará nuestro retorno de inversión y el porcentaje.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU4)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Cuál es la base de datos?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 La base de datos que te ofrecemos en Wobet es para que lleves el reporte mensual de cada operación que haces y controles tus finanzas de forma automatizada, solo pones algunos valores y te arroja automáticamente todo tu balance.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU4)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Con cuanto debo empezar?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 La respuesta a esta pregunta es relativa dada la singularidad de la persona, sin embargo, es mejor cuando tienes un capital grande para operar diariamente, pero también puedes empezar con montos muy bajos como incluso 10 dólares, tomar confianza y luego invertir más. ")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU4)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Atrás'in mensaje:
                    x[0] = 1
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                    
            if operacion == "5":
                if '¿Cómo funciona?' in mensaje:
                   
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Lo que buscamos es evitar aún más las limitaciones, debido a que operamos únicamente señales con ligas reconocidas o muy líquidas, siguiendo el instructivo del curso descriptivo más las recargas con Wobet. Ya no tienes que hacer tantas operaciones diariamente, teniendo un ingreso adicional e incluso puedes operar unos días a la semana como lo hacen muchos usuarios para tener ese ingreso constante a fin de mes.")
                    context.bot.send_message(chat_id=idChat, text="🔥 Es muy sencillo, tu nos envías a nequi, daviplata o bancolombia el saldo que vas a recargar, nosotros te hacemos la recarga y en ese mismo momento te enviamos el adicional según la comisión correspondiente, no es un bono sino una recarga como cualquiera, tu puedes operar y apostar sin ningún término o condición, se realiza para usuarios Wobet y lo tienen cada vez que deseen recargar sus cuentas, el monto mínimo a recargar son $50.000")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU5)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Menos limitaciones? ' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Consiste en evitar las limitaciones y seguir ganando, lo ideal es operar únicamente las señales que sean líquidas, como por ejemplo ligas reconocidas NBA, Champions League, Liga Italiana, España, Alemania, NHL entre otras que aprenderás en el curso descriptivo. Cuando una señal es más baja se reduce el riesgo de limitación y a su vez que anulen una apuesta o que no permita realizarla.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU5)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif '¿Cuántas recargas diarias?' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    context.bot.send_message(chat_id=idChat, text="🔥 Puedes recargar con nosotros varias veces en el día sin ningún problema, como recomendación las casas de apuestas no te permitirán varios retiros al día, entonces lo ideal es que si retiras de una casa de apuestas, recargues a otra cuenta que tengas a nombre de otra persona, además esto permite dejar descansar las cuentas. Las recargas por comisión ayudan mucho para operar debido a que ya no tienes que esperar una señal líquida alta sino por ejemplo tomas una de la NBA al 2% y con las comisiones recibes otro 2% ya hiciste una operación del 4% diariamente, lo cual representaría un excelente promedio sin lidiar con las limitaciones seguido.")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU5)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Ejemplo' in mensaje:
                    
                    context.bot.send_chat_action(chat_id= idChat, action=telegram.ChatAction.TYPING)
                    with open('rushbet.jpg', 'rb') as photo_file:
                        context.bot.sendPhoto(chat_id=idChat, photo=photo_file)
                    with open('wplay.jpg', 'rb') as photo_file:
                        context.bot.sendPhoto(chat_id=idChat, photo=photo_file)
                    context.bot.send_message(chat_id=idChat, text="Ganando Wplay - Rushbet ✅")
                    context.bot.send_message(chat_id=idChat, text="Recargamos con Wobet $500.000 en wplay y $500.000 en rushbet.")
                    context.bot.send_message(chat_id=idChat, text="Con nuestra comisión de recargas ganamos adicional $11.500 en wplay y otros $10.000 en Rushbet.")
                    context.bot.send_message(chat_id=idChat, text="La surebet nos dejó de ganancia $13.000 completamente seguro hasta el final ✅")
                    context.bot.send_message(chat_id=idChat, text="Luego retiramos $500.000 en wplay y volvemos a recargar con Wobet lo que nos deja $10.000 más.")
                    context.bot.send_message(chat_id=idChat, text="Total ganado: $44.500 en un operación 🔥")
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU5)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                elif 'Atrás'in mensaje:
                    x[0] = 1
                    menuBotones = telegram.ReplyKeyboardMarkup(MENU)
                    context.bot.sendMessage(chat_id= idChat, text="\U0001F530 Elige una opción ", reply_markup=menuBotones)
                            
        usuarios[idChat] = x
        #guardando diccionario en archivo.txt
        contenido = json.dumps(usuarios)
        archivo = open("registro.txt", "w")  
        archivo.write(contenido)
        archivo.close()    

def leerRegistro(archivo):
    reg = {}
    archivo = 'registro.txt'
    try:
        registro = open(archivo,'r')
    except FileNotFoundError:
        print(">>Registro no encontrado!!, generando archivo vacio...")
        registro = open(archivo,'w')                                            # Crea el archivo de registr chat_id/identificacion en caso de no existir
        registro.write('{}')
        registro.close()                                                        # Cierra el modo escritura y...
        registro = open(archivo, 'r')                                           # abre como archivo de lectura
    ids = registro.read()                                                       # Leer el contenido del archivo
    registro.close()
    try:
        reg = json.loads(ids)                                                   # lee los datos del registro para convertirlo en diccionario
    except TypeError:
        print("[[Sin usuarios registrados!!!]]")                                # En el caso de no tener usuarios registrados, 
        reg = {}                                                                # crea un diccionario vacio
    ## los IDs leidos desde el archivo estan en formato string y es necesario cambiarlos a entero para funcionamiento con
    ## los ID de chat que llegan desde la interface de telegram
    temp = {}
    for i in reg:
        j = int(i)
        temp[j] = reg[i]
    return temp

def identificar(update, context):
    idChat = update.message.chat_id

path = os.path.dirname(os.path.realpath(__file__)) + '/'
usuarios = leerRegistro(path)
updater = Updater(TOKEN, use_context=True)

def main():
    print("..... Inicio PQR Wobet ...")
    dp = updater.dispatcher    
    dp.add_handler(telegram.ext.CommandHandler("start", start))
    dp.add_handler(telegram.ext.CommandHandler("myId", identificar))
    dp.add_handler(telegram.ext.MessageHandler(Filters.text, mensajes))    
    #revisaUDP.start()
    updater.start_polling()
    updater.idle()
## -----------------------------------------------------------------------------------------------------------------------------------------
##          Inicio del programa
## -----------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    updater.stop()