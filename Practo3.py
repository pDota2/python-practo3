import time
import os
import keyboard
import csv
import json

indexchoice = 1
person1 = "Гопник"
person2 = "Полицейский"
person3 = "Блатной Зек"
box1 = ['-Вечером вы направились в магазин за молоком.' , '-По пути до вас докопалась гопота.' , f'[{person1}] -Мобила или глаз?' , '\n[1]Отдать телефон.\n[2]Принять вызов и начать драку.']
box1choice1 = ['-Вы отдали телефон.' , f'[{person1}] -Ты что терпила?' , '-Вас начали избивать, но к счастью мимо проезжала полицейская машина.' , '-Всех задержали до выяснения обстоятельств.']
box1choice2 = ['-Вы начали драку.' , '-Получилось уложить двух терпил.' , '-Но третий гопник ударил вас бутылкой по голове.']
box2 = ['-Вы оказались за решеткой.' , f'[{person2}] -Готов помочь тебе выбраться отсюда чистым.' , f'[{person2}] -Если откажешься, скорее всего суд признает тебя виновным...' , f'[{person2}] -У упырей с которыми ты связал свой вечер, очень влиятельные отцы.' , '\n[1]Что мне нужно сделать?\n[2]Отказаться от помощи.']
box2choice1 = [f'[{person2}] -Тебе необходимо будет не нанимать адвоката и проиграть суд.' , f'[{person2}] -После того как тебе вынесут приговор, я дам тебе некий порошок...' , f'[{person2}] -Его необходимо будет пронести на зону и передать одному человеку.' , f'[{person2}] -Я все организую, тебя примут там за своего и никто не тронет.' , f'[{person2}] -Через год после отсидки, я вытащу тебя по УДО.' , '\n[1]Согласиться\n[2]Отказаться и попытаться выиграть суд.']
box2choice2 = [f'[{person2}] -Зря ты отказался от моей помощи...' , f'[{person2}] -Я с радостью припишу тебе пару дел, будешь мотать срок в два раза больше!']
box3 = ['-Вы оказались на зоне.' , '-Вас определили в камеру.' , '-При входе у вас интересуются.' , f'[{person3}] -Что сьешь - мыло со стола или хлеб с параши?' , '[1]Стол не мыльница, параша не хлебница.\n[2]Кто я такой чтобы есть хлеб с параши?']
boxend3choice1 = [f'[{person3}] -Правильный ответ.' , f'[{person3}] -Заходи в хату и выбирай шконку.' , '-Далее ваша жизнь в тюрьме проходила спокойно.' , '-Спустя 5 лет отсидки вы умерли от лихорадки...']
boxend3choice2 = [f'[{person3}] -Ответ неверный.' , '-Вас задушили подушкой...']
boxend1 = ['-Вы проиграли суд.' , '-Успешно пронесли и передали порошок.' , '-Через пару дней к вам подошел зек, которому вы передали порошок.' , f'[{person3}] -ЭТО ПАЛЕНЫЙ ТОВАР! ТРЕБУЮ ВЕРНУТЬ МНЕ ДЕНЬГИ! У ТЕБЯ СУТКИ!' , '-Конечно же, вы не знали, что товар, который зек купил у мента, окажется паленым.' , '-Вы не смогли найти необходимую сумму денег.' , 'Следующей ночью вам перерезали горло зубной щеткой, заточенной об стену...']
mainbox = []

def delete_saved_files():
    try:
        os.remove('game_data.json')
        os.remove('game_data.csv')
        print("Сохраненные файлы удалены.")
    except FileNotFoundError:
        print("Файлы сохранения не найдены.")

def delete_menu():
    os.system('cls')
    print("Меню удаления сохраненных файлов.")
    print("[1] Удалить сохраненные файлы")
    print("[2] Назад")
    choice = input("Выберите действие: ")
    if choice == '1':
        delete_saved_files()
    elif choice == '2':
        return
    else:
        print("Некорректный выбор.")
        input("Нажмите Enter, чтобы продолжить...")
        delete_menu()

def startgame():
    os.system('cls')
    print('Добро пожаловать в игру!')
    player_name = input("Введите ваше имя: ")

    while True:
        os.system('cls')
        print(f"Добро пожаловать, {player_name}!")
        print("[1] Начать новую игру")
        print("[2] Меню удаления сохраненных файлов")
        print("[3] Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            game_data = {
                "Player Name": player_name,
            }
            with open('game_data.json', 'a', newline='') as json_file:
                json.dump(game_data, json_file)
            mainbox.insert(0, [f"Player Name: {player_name}"])
            save_to_csv(mainbox)
            save_to_json(mainbox)
            messagebox(mainbox=box1, indexchoice=indexchoice, indexbox=False, end=False)
        elif choice == '2':
            delete_menu()
        elif choice == '3':
            exit("До новых встреч!")
        else:
            print("Некорректный выбор.")
            input("Нажмите Enter, чтобы продолжить...")

def endgame(mainbox=mainbox):
    for message in mainbox:
        print("".join(message))
        time.sleep(1.5)
    exit(print('Спасибо за игру!'))
    
def messagebox(mainbox, indexchoice, indexbox, end):
    os.system('cls')
    for message in mainbox:
        print("".join(message))
        time.sleep(1.5)
    choicechecker(indexchoice=indexchoice, indexbox=indexbox, end=end)

def save_to_json(data):
    with open('game_data.json', 'w', newline='') as json_file:
        json.dump(data, json_file)

def save_to_csv(data):
    with open('game_data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([])
        for row in data:
            writer.writerow(row)

def endgame(mainbox=mainbox):
    for message in mainbox:
        print("".join(message))
        time.sleep(1.5)
    save_to_json(mainbox)
    save_to_csv(mainbox)
    exit(print('Спасибо за игру!'))

def choicechecker(indexchoice, indexbox, end):
    if indexchoice == 2 and indexbox == True:
        print('Для продолжения нажмите [Space]...')
        keyboard.wait('Space')
        messagebox(mainbox=box2, indexchoice=indexchoice, indexbox=False, end=False)
    if indexchoice == 3 and indexbox == True:
        print('Для продолжения нажмите [Space]...')
        keyboard.wait('Space')
        messagebox(mainbox=box3, indexchoice=4, indexbox=False, end=False)
    if end == True:
        endgame(mainbox=mainbox)
    choice(indexchoice)

def choice(indexchoice):
    print('Ваше действие: ')
    time.sleep(0.25)
    if indexchoice == 1:
        while True:
            key = keyboard.read_key()
            match key:
                case '1':
                    return messagebox(mainbox=box1choice1, indexchoice=2, indexbox=True, end=False)
                case '2':
                    return messagebox(mainbox=box1choice2, indexchoice=2, indexbox=True, end=False)          
    if indexchoice == 2:
        while True:
            key = keyboard.read_key()
            match key:
                case '1':
                    return messagebox(mainbox=box2choice1, indexchoice=3, indexbox=False, end=False)
                case '2':
                    return messagebox(mainbox=box2choice2, indexchoice=3, indexbox=True, end=False)
    if indexchoice == 3:
        while True:
            key = keyboard.read_key()
            match key:
                case '1':
                    return messagebox(mainbox=boxend1, indexchoice=3, indexbox=False, end=True)
                case '2':
                    return messagebox(mainbox=box2choice2, indexchoice=3, indexbox=True, end=False)
    if indexchoice == 4:
        while True:
            key = keyboard.read_key()
            match key:
                case '1':
                    return messagebox(mainbox=boxend3choice1, indexchoice=indexchoice, indexbox=False, end=True)
                case '2':
                    return messagebox(mainbox=boxend3choice2, indexchoice=indexchoice, indexbox=False, end=True)

startgame()
