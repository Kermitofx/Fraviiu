#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("833645402:AAE2k_0zF-VZhsb8D1tCBLWCLDnlZFrKnyk")

@bot.message_handler(commands=["/paciencia"])
def paciencia(m):
	if m.text == '/paciencia' or m.text == '/paciencia@SrKingBot ' or m.text == 'paciÃªncia' :
		list = ["ðŸ˜‘ | PaciÃªncia" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "Minha*{}* tÃ¡ *{}*% Hojeâœ¨".format(resposta, valor), parse_mode='Markdown')
		
		
		##Medo 
	
@bot.message_handler(commands=["/medo"])
def medo(m):
	if m.text == '/medo' or m.text == '/medo@SrKingBot ' or m.text == 'medo' :
		list = ["ðŸ˜• | Medo" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "eu to*{}%* de  *{}*Hojeâœ¨".format(valor, resposta), parse_mode='Markdown')
		
		
		##raiva
@bot.message_handler(commands=["/raiva"])
def frase_command(m):
	if m.text == '/raiva' or m.text == '/raiva@SrKingBot ' or m.text == 'raiva' :
		list = ["ðŸ˜  | Raiva" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "Hoje Eu TÃ´ *{}%* De *{}* Hojeâœ¨".format(valor, resposta), parse_mode='Markdown')
		
  	###start
  
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.reply_to(m, "Oie\n\n Olha Meus Commands DisponÃ­veis :) âœŒ\n `/PaciÃªncia` = `*Medidor De PaciÃªncia* ðŸ˜‘ \n `/medo` = *Medidor de Medo* ðŸ˜¢ \n `/raiva` = *Medidor de Raiva* ðŸ˜ ")
  
		
		
  
bot.polling( )
