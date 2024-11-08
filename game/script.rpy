### Вы можете расположить сценарий своей игры в этом файле.
##
### Определение персонажей игры.
##define e = Character('Эйлин', color="#c8ffc8")
##
### Вместо использования оператора image можете просто
### складывать все ваши файлы изображений в папку images.
### Например, сцену bg room можно вызвать файлом "bg room.png",
### а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
##
### Игра начинается здесь:
##label start:
##
##    scene bg room
##
##    show eileen happy
##
##    e "Вы создали новую игру Ren'Py."
##
##    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"
##
##    return





### KLIK

define m = Character("Михаил")
define n = Character("Надежда")
define a = Character("Алина")
define ap = Character("Алексей Петрович")
define k = Character("Катя")

label start:

    scene black

    show text "Выберите персонажа, за которого хотите играть:" at truecenter

    menu:
        "Михаил":
            jump mihail_route
        "Надежда":
            jump nadezhda_route
        "Алина":
            jump alina_route
        "Алексей Петрович":
            jump aleksey_route
        "Катя":
            jump katya_route

label mihail_route:

    scene street_day

    m "Город встретил меня серым небом и шумом машин. Я переехал сюда, чтобы найти новый смысл жизни."

    m "Возможно, стоит познакомиться с соседями."

    menu:
        "Постучать в дверь соседки":
            jump knock_neighbor
        "Пройти мимо и заняться своими делами":
            jump ignore_neighbor

label knock_neighbor:

    scene hallway

    m "Я подошёл к двери и нерешительно постучал."

    n "Да? Кто там?"

    m "Привет, я ваш новый сосед. Хотел познакомиться."

    n "..."

    # Продолжение взаимодействия

    return

label ignore_neighbor:

    m "Нет, не сегодня. У меня ещё много дел."

    # Продолжение сюжета

    return


label nadezhda_route:

    scene apartment_night

    n "Снова эта бессонница... Переезд не помог забыть прошлое, но, может быть, здесь всё будет иначе."

    # Продолжайте историю Надежды здесь

    return

label alina_route:

    scene cafe_day

    a "Я стараюсь начать всё сначала, но воспоминания о нём не дают мне покоя."

    # Продолжайте историю Алины здесь

    return

label aleksey_route:

    scene office_day

    ap "Многие молодые люди сейчас потеряны. Может, я смогу помочь им найти свой путь."

    # Продолжайте историю Алексея Петровича здесь

    return

label katya_route:

    scene home_evening

    k "Михаил совсем отдалился. Нужно попытаться восстановить нашу связь."

    # Продолжайте историю Кати здесь

    return
