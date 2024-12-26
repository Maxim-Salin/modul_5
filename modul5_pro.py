from time import sleep


class User():

    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = password #hash(password)
        self.age = age
# nickname
# password
# age

class Video():
    #pass
    def __init__(self, title ,duration,time_now = 0,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
# title
# duration
# time_now
# adult_mode

class UrTube():
    # def __init__(self, users, videos, current_user):
    #     self.users = users
    #     self.videos = videos
    #     self.current_user = current_user
    videos = []
    users = []
    userList = []
    current_user = User("",'',0)

    tmp = Video("","",0,False)
    tmp2 = Video("", "", 0, False)

    def log_in(self, nickname, password ):
        self.nickname = nickname
        self.password = password
        mrFind = False
        #current_user_i = User("", '', 0)
        for i in self.userList:
            if i.nickname == self.nickname and hash(i.password) == hash(self.password) :
                self.current_user = i

                # print(f"Добро пожаловать {i.nickname}")
                # print(f"возраст {i.age}")
                # print(f"возраст current_user {self.current_user.age}")
                mrFind = True
                break
        if mrFind == False:
            print("Логин или пароль не действителен")

    def register(self, nickname, password, age):

        self.nickname = nickname
        self.password = password
        self.age = age
        newUser = User(nickname, password, age)
        self.current_user = newUser
        self.userList.append(User(nickname, password, age))
        #self.userList.append(User(self.nickname,self.password, self.age))
    def log_out(self):
        current_user = None #User("",'',0)

    def add(self, *other):
        for i in other:
           tmp = i
           mark1 = False
           if len(self.videos) > 0:
               for j in self.videos:
                    tmp2 = j
                    if tmp.title == tmp2.title:
                        mark1 = True #self.videos.append(tmp)
               if mark1 == False :
                    self.videos.append(tmp)
           else:
               self.videos.append(tmp)


    def get_videos(self, text):
        list_vid = []
        self.text = text
        for i in self.videos:
            text1 = self.text.lower()
            self.text2 = i.title.lower()
            if self.text2.find(text1) != -1:
                list_vid.append(i.title)
        print(list_vid)

    def watch_video(self, nameVideo):
        self.nameVideo = nameVideo
        timeTik = 0
        playV = False
        if  (self.current_user != 0):
            for i in self.videos:
                if (i.title == self.nameVideo) :
                    if  (i.adult_mode == False  or
                    (i.adult_mode == True and self.current_user.age > 18)):
                        timeTik = i.duration
                        playV = True
                        while timeTik:
                            sleep(1)
                            timeTik -= 1
                            print(timeTik,end=" ")
                    else:
                        print("Вам нет 18")
                        playV = True
        print("")
        if playV == False:
            print("такого видео нет")
    def __str__(self):
        return(str(self.current_user.nickname +" "+ str(self.current_user.age)))



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video(' язык программирования 2024 года', 150)
v4 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v5 = Video('Для чего девушкам парень ?', 15, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
ur.add(v3, v4)
ur.add(v5)
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(ur.current_user.nickname)
ur.get_videos("парень") # поиск ключевого слова
ur.watch_video('Для чего девушкам парень программист?')     # это воспроизвести
ur.watch_video('Для Ачепятка;-) парень программист?')    # поиск не существующего
print(str(ur))
ur.log_in('vasya_pupkin', 'lolkekcheburek') # вход под именем Вася
print(str(ur))
ur.log_in('vasya_pupkin', 'BAG-kekcheburek') # проверка на не верный пароль
ur.watch_video('Для чего девушкам парень программист?') #проверка на возраст
k = input()
