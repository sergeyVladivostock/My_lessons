class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password =password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f"Имя пользователя: {self.nickname}"

    def __int__(self):
        return self.age

class Video:

    def __init__(self,title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __int__(self):
        return self.duration, self.time_now(0)

    def __bool__(self):
        return self.adult_mode(False)





class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self):

    def register(self):

    def log_out(self):

    def add(self):

    def get_videos(self):

    def watch_video(self):

if __name__ == "__main__":

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
