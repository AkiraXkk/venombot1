import time
import random
import json
import telebot
from datetime import datetime

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import venomix

api_key = '6859787649:AAGpJjyp4Zs0e5AxQEkpV7WMJbu6X30hHVk'  # Substitua pelo seu próprio token
chat_id = '2043458007'  # Substitua pelo ID do seu canal

bot = telebot.TeleBot(token=api_key)

def calcular_chance(minas):
    if minas == 2:
        return random.randint(92, 100)
    elif minas == 3:
        return random.randint(80, 100)
    elif minas == 4:
        return random.randint(70, 100)

# Função atualizada para distribuir 2, 3 ou 4 diamantes aleatoriamente na matriz
def escolher_padrao_aleatorio():
    padrao_vazio = ['💣'] * 25
    
    # Escolhemos aleatoriamente a quantidade de diamantes (2, 3 ou 4)
    quantidade_diamantes = random.choice([2, 3, 4])
    
    # Adicionamos a quantidade escolhida de diamantes 💎 aleatoriamente nos espaços vazios ⬛
    for _ in range(quantidade_diamantes):
        posicao = random.randint(0, 24)
        while padrao_vazio[posicao] == '💎':
            posicao = random.randint(0, 24)
        padrao_vazio[posicao] = '💎'
    return padrao_vazio

# Função para criar um botão em suas mensagens
def button_link():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="CLIQUE AQUI NO JOGO 💣", url="https://betbrj.com/ymt0gx6fz"))
    return markup

niveis = {
    3: "🟡 Médio risco: Médio Lucro💵",
    4: "🔴 Grande risco: Alto Lucro 💰"
}

# Adicione um atraso de 10 segundos antes de entrar no loop principal
time.sleep(10)

while True:
    h = datetime.now().hour
    m = datetime.now().minute + 2
    s = datetime.now().second
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')
    
    minas = random.choice([3, 4])
    padrao_escolhido = escolher_padrao_aleatorio()
    
    message_text = f'''
🟢🟢 SINAL CONFIRMADO 🟢🟢

 Venom do Mines 💣

💣 Aposte com: {minas} Minas
🕛 Válido até: {h}:{m}
🔁 Nº de tentativas: 2

{' '.join(padrao_escolhido[:5])}
{' '.join(padrao_escolhido[5:10])}
{' '.join(padrao_escolhido[10:15])}
{' '.join(padrao_escolhido[15:20])}
{' '.join(padrao_escolhido[20:])}

{niveis[minas]}
'''

    dados = bot.send_message(chat_id=chat_id, text=message_text, reply_markup=button_link())
    
    # Registre o momento em que a mensagem foi enviada
    mensagem_enviada_em = datetime.now()

    # Verifique o tempo decorrido e aguarde o tempo restante
    tempo_decorrido = (datetime.now() - mensagem_enviada_em).total_seconds()
    if tempo_decorrido < 120:
        tempo_restante = 120 - tempo_decorrido
        time.sleep(tempo_restante)
    
    # Após 2 minutos, enviar a mensagem
    if (datetime.now() - mensagem_enviada_em).total_seconds() >= 120:
        bot.send_message(chat_id=chat_id, text="                                                             ㅤ  🟢🟢 +1 GRENN 🟢🟢                                                ")

    time.sleep(15)
    
    