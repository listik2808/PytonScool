variant = (".com",".ru",".net")
is_change = True

def character_search(text) :
    for i in text :
        if i == "@" :
            return  True
    return False

def checking_sender_recipient(recipient,sender):
    if character_search(recipient) == True and character_search(sender) == True :
        if sender.endswith(variant) == False or recipient.endswith(variant) == False :
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            return False
        else:
             return True
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return False

def send_email(message,recipient,*,sender ="university.help@gmail.com") :
    is_change = checking_sender_recipient(recipient,sender)
    if is_change == True :
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')