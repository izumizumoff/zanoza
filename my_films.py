'''
Модуль посвящен моим любимым филмам и сериалам.
Постоянно обновляемый список фильмов.
JSON файл 'films' содержит информацию о фильмах:
	1. Название
	2. Режиссер
	3. Год
	4. Рейтинг
	 
Мой личный рейтинг:
	 
  5: Ничего особенного, обычный
  6: Любопытно было посмотреть
  7: Хороший и интересный, рекомендую
  8: Крутой фильм! Обязательно к просмотру!
  9: Один из лучших фильмов, который я видел
  10: Моё кинопотрясение
  
 Что может:
 	1. Добавлять новые фильмы и сохранять их в JSON файле
 	2. Искать фильмы по имени режиссера: образует список фильмов снятые этим режиссером
 	3. Искать фильмы по году: образует список фильмов снятые в этом году
 	4. Искать фильмы по первой букве: образует список по первой букве
 	5. Список всех режиссеров
 	6. Список всех фильмов 
'''
class MyFilms:
	
    def __init__(self):
        import json
          
        with open('films.json', 'r') as file:
            films_bin = json.load(file)
        self.films = films_bin.copy()

    def new(self, film, director, year, rate=0):
        # добавляет новый фильм с его основными атрибутами
        # название, режиссер, год, рейтинг 
        # выводит на дисплей инфу об этом

        if film in list(self.films):
            print('Такой фильм: "%s" УЖЕ ЕСТЬ!!!' % film)
        else:
            self.films[film] = {
                'dir': director,
                'year': year,
                'rate': rate,
                }

            print(
                'Добавлен фильм "%s"' % film,
                '\nрежиссер: %s' % director,
                '\n%d года' % year,
                '\nмой рейтинг: %d' % rate)

    def director_search(self, nameOfDir):
        # метод поиска по режиссеру
        # выводит словарь из названия и года

        directorDict = {}
        for x in self.films:
            if self.films[x].get('dir') == nameOfDir:
                directorDict[x] = self.films[x]['year']
        return directorDict

    def year_search(self, intYear):
        # метод поиска по году
        # выводит словарь {фильм: режиссер}

        yearDict = {}
        for x in self.films:
            if self.films[x].get('year') == intYear:
                yearDict[x] = self.films[x]['dir']
        return yearDict

    def sortLetter(self, letter):
        # метод поиска по первой букве
        # выводит список фильмов, 
        # название которых начинается с буквы поиска

        listLetter = []
        for x in self.films:
            if x[0].lower() == letter.lower():
                listLetter.append(x)
        listLetter.sort()
        return listLetter

    def allFilms(self):
        # метод возвращающий полный список
        # названий фильмов по алфавиту

        filmList = list(self.films)
        filmList.sort()
        return filmList

    def allDirectors(self):
        # метод возвращающий полный список 
        # режиссеров по алфавиту

        directorsList = []
        for x in self.films:
            if self.films[x]['dir'] in directorsList:
                continue
            else:
                directorsList.append(self.films[x]['dir'])
        for x in directorsList:
            if type(x) == type([]):
                for y in x:
                    directorsList.append(y)
                directorsList.remove(x)

        filterList = []
        for x in directorsList:
            xList = []
            xList = x.split(' ')
            if len(xList) == 2:
                xList.reverse()
            word = ' '.join(xList)
            filterList.append(word)
        filterList.sort()

        finalList = []
        for x in filterList:
            xList = []
            xList = x.split(' ')
            if len(xList) == 2:
                xList.reverse()
            word = ' '.join(xList)
            finalList.append(word)
        return finalList

    def printDirectors(self):
        # метод выводящий на экран
        # пронумерованный список всех режиссеров

        for index, item in enumerate(self.allDirectors()):
            print('%d. %s' % (index + 1, item))

    def printFilms(self):
        # метод выводящий на экран
        # пронумерованный список всех нпзваний фильмов

        for index, item in enumerate(self.allFilms()):
            print('%d. %s' % (index + 1, item))

    def dateTime(self):
        # формирует дату для
        # названия JSON архива файлов с фильмами

        import datetime

        datePrint = datetime.datetime.today()
        dateList = str(datePrint).split(' ')

        dateF = dateList[0]
        timeF = dateList[1][0:8].replace(':', '-')
        return '%s-%s' % (dateF, timeF)

    def save(self):
        # важный метод
        # сохраняющий все данные в файле
        # а также копию в папке с архивом

        import json
        
        name = 'file_bin_dir/' + self.dateTime() + '.json'
        with open(name, 'w') as file:
            json.dump(self.films, file, ensure_ascii=False)
        with open('films.json', 'w') as file_bot:
            json.dump(self.films, file_bot, ensure_ascii=False)
        with open('films.json', 'r') as file:
            films_bin = json.load(file)
        self.films = films_bin.copy()
        print('__________________')
        print('СПИСОК ОБНОВЛЕН')
