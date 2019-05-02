#1. Создайте класс Word.
#2. Добавьте свойства text и part of speech.
#3. Добавьте возможность создавать объект слово со значениями в скобках.
#4. Создайте класс Sentence
#5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
#6. Добавьте метод show, составляющий предложение.
#7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.



class word:
    text=''
    part_of_speech=''
    def __init__(self,text,part_of_speech):
        self.text=text
        self.part_of_speech=part_of_speech


class sentence:
    content=[]
    def show(self):
        elements=''
        for element in self.content:
            elements+=element.text
            elements+=' '
        return elements

    def show_parts(self):
        sent=self.show()
        print("В предложении", sent )
        for element in self.content:
            print("Слово ", element.text, '-', element.part_of_speech)

    def __init__(self,*args):
        self.content=args



word1=word('Это','Частица')
word2=word('тестовое','Прилагательное')
word3=word('предложение','Существительное')


sen1=sentence(word1,word2,word3)
print(sen1.show())
sen1.show_parts()






