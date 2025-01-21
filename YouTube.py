from time import sleep

class User:
    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

class Video:
    def __init__(self,title,duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now =0
        self.adult_mode = adult_mode

    def __contains__(self, item):
        if isinstance(item,Video):
            return item.title in self.title

    def __eq__(self, other):
        if str(self.title).lower().count(str(other).lower()):
            return self.title

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def register(self,nickname,password,age):
        if len(self.users) == 0:
            user = User(nickname,password,age)
            self.add_user(user)
            self.set_user_curent(user)
        else:
            count =0
            for user in self.users:
                if nickname == user.nickname:
                    print(f"Пользователь {nickname} уже существует")
                    break
                else:
                    count += 1
                    if count == len(self.users):
                        user = User(nickname, password, age)
                        self.add_user(user)
                        self.set_user_curent(user)
                        break

    def add_user(self,user):
        user = User(user.nickname, user.password, user.age)
        self.users.append(user)

    def set_user_curent(self,user):
        self.current_user = user


    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                hash1 = hash(str(password))
                hash2 = hash(str(user.password))
                if hash1 == hash2:
                    self.current_user = user
                    break

    def log_out(self):
        self.current_user = None

    def add(self,*Video):
        for video in Video:
            if len(self.videos) == 0:
                self.videos.append(video)
                continue
            for video_save in self.videos:
                if video.__contains__(video_save) == False:
                    self.videos.append(video)
                    print("Добавили видео")

    def get_videos(self,text):
        list_title = []
        for name in self.videos:
            if isinstance(name,Video):
                textname = name.__eq__(text)
                if textname !=None:
                    list_title.append(textname)

        return list_title

    def watch_video(self,video_name):
        if self.current_user != None:
            for name in self.videos:
                if isinstance(name,Video):
                    if name.title == video_name:
                        self.check_age(name)
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

    def check_age(self,Video):
        if Video.adult_mode == True:
            if isinstance(self.current_user, User):
                if self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    self.viewing_time_display(Video)
        else:
            self.viewing_time_display(Video)

    def viewing_time_display(self,Video):
        while Video.time_now != Video.duration:
            Video.time_now += 1
            print(Video.time_now)
            sleep(1)
            if Video.time_now == Video.duration:
                print("Конец видео")
                Video.time_now = 0
                break

ur = UrTube()
ur.register("Jon",123,13)
ur.register("Joneton",123213,32)
print(ur.current_user)
ur.log_in("Jon",123)
print(ur.current_user)
ur.log_out()
print(ur.current_user)
v1 = Video("Буратино",10)
v2 = Video("Буратино",10)
v3 = Video("Рат2",4,True)
ur.add(v1,v2,v3)
print(ur.get_videos("Бу"))
print(ur.get_videos("рат"))
ur.log_in("Jon",123)
print(ur.current_user)
ur.log_in("Joneton",123213)
print(ur.current_user)
ur.watch_video("Рат2")
