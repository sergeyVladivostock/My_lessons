from encodings.utf_7 import encode

def send_email (message,recipient,*,sender = "university.help@gmail.com"):
    a = (".com",".ru",".net")
    b = False
    c = False
    if "@" not in recipient or "@" not in sender:
        print("Невозможно отправить письмо с адреса", sender, " на адрес", recipient)
    for i in range(0,len(a)):
        if a[i] in recipient:
            b = True
            break
    for i in range(0,len(a)):
        if a[i] in sender:
            c = True
            break
    if c == False or b == False:
        print("Невозможно отправить письмо с адреса",sender,"на адрес",recipient)
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса",sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print("========================")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print("========================")
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print("========================")
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')