#1. Создайте классы Noun и Verb.
#2. Настройте наследование от Word.
#3. Добавьте защищенное свойство «Грамматические характеристики».
#4. Перестройте работу метода show класса Sentence.
#5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.





class Word:

    def __init__(self,text,part_of_speech):
        self.text=text
        self.part_of_speech=part_of_speech

class Sentence:
    content=[]
    def __init__(self, *args):
        self.content = args

    def show(self):
        elements=''
        for element in self.content:
            elements+=element.text+' '
        return elements

    def show_parts(self):
        sent=self.show()
        print("В предложении", sent )
        for element in self.content:
            print("Слово ", element.text, '-', element.part_of_speech, '-', element.get_property())




class Noun(Word):
#    __property_noun=''
    def __init__(self, text, part_of_speech,property):
        self.text = text
        self.part_of_speech = part_of_speech
        self.__property_noun=property

    def get_property(self):
        return self.__property_noun



class Verb(Word):
#    __property_gr=''
    def __init__(self, text, part_of_speech,property):
        self.text = text
        self.part_of_speech = part_of_speech
        self.__property_verb=property
    def get_property(self):
        return self.__property_verb


word1=Noun('Кот','Существительное','грамматические характеристики существительного')
word4=Verb('работать','Глагол','грамматические характеристики глагола')

sen1=Sentence(word1, word4)
print(sen1.show())
sen1.show_parts()
