'''
The module is dedicated to my favorite films and TV shows.
Constantly updated list of films.
JSON file 'films' contains information about films:
	1. Title
	2. Director
	3. Year
	4. Rating

My personal rating:
	5: Nothing special, normal
	6: It was interesting to see
	7: Nice and interesting, I recommend
	8: Cool movie! Must-see!
	9: One of the Best Movies I've Seen
	10: My Movie Shake

What can:
 	1. Add new movies and save them in JSON file
	2. Search for films by director's name: generates a list of films made by this director
	3. Search for films by year: generates a list of films made this year
	4. Search movies by first letter: makes a list by first letter
	5. List of all directors
	6. List of all films
'''
class MyFilms:
	
    def __init__(self):
        import json
          
        with open('films.json', 'r', encoding='UTF-8') as file:
            films_bin = json.load(file)
        self.films = films_bin.copy()

        with open('serials.json', 'r', encoding='UTF-8') as file:
            serials_bin = json.load(file)
        self.allSerials = serials_bin.copy()
        self.allSerials.sort()
        

    def newFilm(self, film, director, year, rate=0):
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

    def newSerial(self, serial):
        # добавляет новый сериал в список
        # название, режиссер, год, рейтинг 
        # выводит на дисплей инфу об этом

        if serial in list(self.serials):
            print('Такой сериал: "%s" УЖЕ ЕСТЬ!!!' % serial)
        else:
            self.serials.append(serial)
            self.serials.sort()

            print(
                'Добавлен сериал "%s"' % serial)

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

    def saveFilm(self):
        # важный метод
        # 
        # сохраняющий все данные в файле
        # а также копию в папке с архивом

        import json
        # сохранение фильмов
        name = 'file_bin_dir/' + self.dateTime() + '.json'
        with open(name, 'w', encoding='UTF-8') as file:
            json.dump(self.films, file, ensure_ascii=False)
        with open('films.json', 'w', encoding='UTF-8') as file_bot:
            json.dump(self.films, file_bot, ensure_ascii=False)
        with open('films.json', 'r', encoding='UTF-8') as file:
            films_bin = json.load(file)
        self.films = films_bin.copy()

        # сохранение сериалов

        print('Фильм добавлен!')
        print('__________________')
        print('СПИСОК ОБНОВЛЕН')
