#Форматирование текста.
import re
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
    formated_text = formated_text + sentenses[l]  + ' ' + '\n'
  return str(formated_text)
  

#Отладка
#text = 'Привет, я, к несчастью, упал. Такая себе.'
text = input()
print(format_text(text))
print(str(int(100*(1- len(format_text(text))/len(text))))+ '%')
