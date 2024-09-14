def send_email (message,recipient,*,sender = "university.help@gmail.com"):
    a = (".com",".ru",".net")

    if "@" not in recipient or "@" not in sender:
        print("Невозможно отправить письмо с адреса", sender, " на адрес", recipient)

    for i in range(0,3):
        if a[i] in recipient and a[i] in sender:
            break
        if a[i] in recipient:
            for j in range(0,3):
                if a[j] in sender:
                    break
                else:
                    continue
        else:
            for j in range(0, 3):
                if a[j] in sender:
                    break
                else:
                    continue

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")

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