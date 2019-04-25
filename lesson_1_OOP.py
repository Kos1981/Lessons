import re
#1. Получите текст из файла.
#2. Разбейте текст на предложения.
#3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
#4. Отберите все ссылки.
#5. Ссылки на страницы какого домена встречаются чаще всего?
#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».



def the_most_freqent(words):
    freq = {}

    for word in words:
        freq[word] = words.count(word)
    print("Наиболее встречающиеся слова:")
    maximum=max(freq.values())
    for x, y in freq.items():
        if y == maximum:
            print("Слово: ", x, y, "раз(а)")

#1. Получите текст из файла.
f = open('new.txt', "r")
text=f.read()
print('Задание 1:')
print(text)

#2. Разбейте текст на предложения.
sentences=re.split('\.[ \n]',text)
print('Задание 2:')
print(sentences)

#3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
words=re.findall('[а-яА-ЯёЁ]{4,}',text.lower())
print('Задание 3:')
the_most_freqent(words)

#4. Отберите все ссылки.
links=re.findall('(?:\w+\.){1,2}ru(?:/\w+){0,1}',text)
print('Задание 4:')
print(links)

#5. Ссылки на страницы какого домена встречаются чаще всего?
domainlinks=re.findall('\w+\.ru',text.lower())
print('Задание 5:')
print(domainlinks)
the_most_freqent(domainlinks)

#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

newtext=re.sub('(?:\w+\.){1,2}ru(?:/\w+){0,1}','Ссылка отобразится после регистрации',text)
print('Задание 6:')
print(newtext)




