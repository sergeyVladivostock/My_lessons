class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
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

class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

if __name__ == "__main__":
