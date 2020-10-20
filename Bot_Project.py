#Импорт бота. Импортировать нашу библиотеку и подключить токен бота:
import telebot;
import re
bot = telebot.TeleBot('1242287800:AAEuM8ZZ-D3TYGO4E_GRIIFryuRJp7r-f7g')
#Метод получения сообщений ботом
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

#Форматирование текста
with open("data_words.txt") as file:
      array = [row.strip() for row in file]
def format_text(text):
  #Форматриуем весь текст: убираем слова в скобках
  text = re.sub(r'\[[0-9]*\]', ' ', text)
  text = re.sub(r'\[a-zA-Zа-яА-ЯёЁ]*\]', ' ', text)
  text = re.sub(r'\s+', ' ', text)
  text = re.sub(r'\([^()]*\)', '', text)
  text = re.sub(r'\([^[]]*\)', '', text)
  sentenses = sent_tokenize(text)
  #print(sentenses)
  for k in range(0, len(sentenses)):
    #Инцилизация переменной
    sent = sentenses[k]
    
    #Приводим к нижнему регистру
    sent = sent.lower()
    
    #Удаляем вводные слова
    for i in range(0, len(array)):
      sent = sent.replace(array[i] + ', ', "")
    #print(sent)
    #Убираем первые k символов до первой буквы
    while len(sent) > 0 and sent[0] not in "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
      sent = sent[1:]
    #print(sent)
    #Переводим первую букву строки в верхний регистр:
    first_letter = sent[0]
    first_letter = first_letter.title()
    sent = sent[1 :]
    #print(sent)
    sent = first_letter + sent
    sentenses[k] = sent
    sent = ''
  formated_text = ''
  #print(sentenses)
  for l in range(0, len(sentenses)):
    formated_text = formated_text + sentenses[l]  + ' '
  return str(formated_text)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/text':
        bot.send_message(message.from_user.id, "Введите, пожалуйста, текст: ");
        bot.register_next_step_handler(message, text_process);
    else:
        bot.send_message(message.from_user.id, 'Нажми => /text');

def text_process(message):
    text = message.text
    #bot.send_message(message.from_user.id, text);
    #Форматируем текст
    text = format_text(text)
    # Токенизация текста
    stopWords = set(stopwords.words("russian")) 
    words = word_tokenize(text) 
    #stopwords.append('')
    # Создаем матрицу для хранения значения слов в тексте.
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1
   
    # Аналогчно для каждого предложения
    sentences = sent_tokenize(text) 
    sentenceValue = dict() 
   
    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq 
   
   
   
    sumValues = 0
    for sentence in sentenceValue: 
        sumValues += sentenceValue[sentence] 
   
# Значение кажого предложения в тексте
   
    average = int(sumValues / len(sentenceValue)) 
   
#Делаем пересказ 
    
    summary = '' 
    for sentence in sentences: 
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.0 * average)): 
            summary += " " + sentence
    answer = summary 
    bot.send_message(message.from_user.id, answer);

    bot.send_message(message.from_user.id, "Процент сжатия(в процентах): ");
    bot.send_message(message.from_user.id, int(100*(1 - (len(answer)/len(text)))));                 
bot.polling(none_stop=True, interval=0)



