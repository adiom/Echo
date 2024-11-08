# script.rpy
# -*- coding: utf-8 -*-

# Определение персонажей

define k = Character("Кейтер", color="#5DADE2", who_font="fonts/DejaVuSans.ttf")
define n = Character("Найда", color="#AF7AC5", who_font="fonts/DejaVuSans.ttf")
define l = Character("Лена", color="#F7DC6F", who_font="fonts/DejaVuSans.ttf")
define ap = Character("Алексей Петрович", color="#52BE80", who_font="fonts/DejaVuSans.ttf")
define kty = Character("Катя", color="#F5B041", who_font="fonts/DejaVuSans.ttf")
define shadow = Character("Омуть", color="#566573", who_font="fonts/DejaVuSans.ttf", what_font="fonts/Shadow.ttf", what_outlines=[ (1, "#000000") ])

# Определение изображений

# Фоны
image bg city_street_day = "images/backgrounds/city_street_day.jpg"
image bg apartment_hallway = "images/backgrounds/apartment_hallway.jpg"
image bg nadezhda_apartment = "images/backgrounds/nadezhda_apartment.jpg"
image bg city_park_day = "images/backgrounds/city_park_day.jpg"
image bg kayter_apartment = "images/backgrounds/kayter_apartment.jpg"
image bg dream_world = "images/backgrounds/dream_world.jpg"

# Персонажи
image kayter normal = "images/characters/kayter_normal.png"
image kayter happy = "images/characters/kayter_happy.png"
image kayter sad = "images/characters/kayter_sad.png"

image nadezhda normal = "images/characters/nadezhda_normal.png"
image nadezhda smile = "images/characters/nadezhda_smile.png"
image nadezhda sad = "images/characters/nadezhda_sad.png"

image lena normal = "images/characters/lena_normal.png"
image lena mysterious = "images/characters/lena_mysterious.png"

image shadow = "images/characters/shadow.png"

# Начало игры

label start:

    scene black

    show text "Эхо Потерянных Миров" at truecenter with dissolve

    pause 2

    hide text with dissolve

    show text "Кто ты?" at truecenter with dissolve

    menu:

        "Кейтер":

            jump kayter_route

        "Найда":

            jump nadezhda_route

# Сюжетная линия Кейтер

label kayter_route:

    scene bg city_street_day

    show kayter normal at center

    k "Город встретил меня серым небом и нескончаемым потоком людей."

    k "Я переехал сюда, надеясь найти ответы на вопросы, которые давно не дают мне покоя."

    k "Но вместо этого чувствую себя ещё более потерянным."

    hide kayter

    k "Может, стоит начать с малого — познакомиться с соседями или просто прогуляться по городу."

    menu:

        "Постучать в дверь соседки":

            jump kayter_knock_neighbor

        "Прогуляться по городу":

            jump kayter_explore_city

# Вариант: Постучать в дверь соседки

label kayter_knock_neighbor:

    scene bg apartment_hallway

    show kayter normal at left

    k "Я подошёл к двери соседней квартиры и нерешительно постучал."

    pause

    show nadezhda normal at right with dissolve

    n "Да? Кто там?"

    k "Здравствуйте, я ваш новый сосед, Кейтер. Решил представиться."

    n "О, приятно познакомиться. Я Найда."

    k "Взаимно."

    n "Как вам город?"

    k "Пока сложно сказать. Всё кажется таким... незнакомым."

    n "Понимаю. Я тоже недавно переехала."

    n "Может, зайдёте на чашку чая? Обсудим наши впечатления."

    menu:

        "Согласиться зайти":

            jump kayter_visit_nadezhda

        "Отказаться":

            jump kayter_refuse_nadezhda

label kayter_visit_nadezhda:

    scene bg nadezhda_apartment

    with dissolve

    show nadezhda smile at right

    n "Проходите, чувствуйте себя как дома."

    show kayter normal at left

    k "Спасибо. У вас очень уютно."

    n "Чай с сахаром или без?"

    k "Без сахара, спасибо."

    n "Отлично."

    n "Расскажите, что привело вас в наш город?"

    k "Это долгая история... Я ищу ответы на некоторые вопросы. Возможно, здесь я смогу их найти."

    n "Интересно. Я тоже в поисках. Кажется, у нас больше общего, чем мы думали."

    # Встреча с Леной

    "Вдруг раздался звонок в дверь."

    n "Извините, это, наверное, Лена."

    n "Она моя подруга, немного странная, но вы привыкнете."

    show lena mysterious at center with dissolve

    l "Привет, Найда!"

    n "Лена, познакомься, это Кейтер, мой сосед."

    l "Привет, Кейтер."

    k "Здравствуйте."

    l "Ты выглядишь... особенным."

    k "(удивлённо) В каком смысле?"

    l "Твоя аура... Но об этом позже."

    n "Лена увлекается необычными вещами."

    l "Альтернативные реальности, сны, грани между мирами — это моя стихия."

    k "Звучит захватывающе."

    l "Если хочешь, могу рассказать больше."

    menu:

        "Попросить Лену рассказать об альтернативных реальностях":

            jump kayter_ask_lena

        "Сменить тему разговора":

            jump kayter_change_topic

label kayter_ask_lena:

    l "Отлично! Знаешь, есть теория, что наши сны — это окна в другие миры."

    l "Границы между реальностями тоньше, чем кажется."

    k "Интересно... Иногда мне снятся странные сны."

    l "Может быть, это не просто сны."

    # Омуть начинает проявляться

    "Вдруг свет в комнате начал меркнуть."

    show shadow at center with fade

    shadow "Кейтер..."

    k "(испуганно) Кто это?"

    n "Ты что-то сказал?"

    l "(шёпотом) Похоже, твоя Омуть проявляется."

    k "Омуть?"

    l "Твои страхи и сомнения. Они могут принимать форму."

    shadow "Ты не найдёшь здесь ответов..."

    menu:

        "Противостоять Тени":

            jump kayter_confront_shadow

        "Убежать из квартиры":

            jump kayter_run_away

label kayter_confront_shadow:

    k "Нет! Я не боюсь тебя!"

    shadow "Посмотрим..."

    "Омуть начала приближаться, но Лена встала между вами."

    l "Оставь его!"

    shadow "Ты не можешь защитить его вечно."

    "Омуть растворилась в воздухе."

    k "Что это было?"

    l "Мы должны поговорить. Но не здесь."

    # Продолжение сюжета

    return

label kayter_run_away:

    "Паника охватила вас, и вы выбежали из квартиры."

    scene bg apartment_hallway

    k "(задыхаясь) Что это было?"

    "Вы услышали, как дверь открылась позади."

    n "Кейтер! Подожди!"

    l "Он ещё не готов."

    "Вы решили вернуться к себе домой и обдумать случившееся."

    scene bg kayter_apartment

    k "Может, мне просто показалось..."

    # Сон и встреча с Омутью

    jump kayter_dream

label kayter_change_topic:

    k "Это очень интересно, но, возможно, в другой раз."

    l "Как знаешь."

    n "Может, расскажешь о себе?"

    # Продолжение диалога с Надеждой

    k "Я родом из небольшого городка. Всегда чувствовал, что мне чего-то не хватает."

    n "Я тоже. Возможно, в этом городе мы найдём то, что ищем."

    # Завершение визита

    k "Спасибо за чай и компанию. Мне пора."

    n "Рада была познакомиться. Заходи ещё."

    k "Обязательно."

    # Продолжение сюжета

    return

label kayter_refuse_nadezhda:

    k "Спасибо, но у меня ещё много дел. Возможно, в другой раз."

    n "Понимаю. Если что, я всегда рядом."

    k "До свидания."

    # Продолжение сюжета

    jump kayter_explore_city

# Вариант: Прогуляться по городу

label kayter_explore_city:

    scene bg city_park_day

    show kayter normal at center

    k "Я решил прогуляться по парку, чтобы развеяться."

    "Вдалеке заметил девушку, сосредоточенно смотрящую в ноутбук."

    show lena normal at right

    k "(мысленно) Интересно, чем она так увлечена?"

    l "(не отрывая взгляда) Если хочешь спросить, подойди."

    k "(смущённо) Ой, извините. Я не хотел мешать."

    l "Ничего страшного. Я Лена."

    k "Кейтер."

    l "Ты не местный."

    k "Верно. Только что переехал."

    l "Ищешь что-то?"

    k "Можно и так сказать."

    l "Может, я могу помочь. Я знаю места, которых нет на картах."

    k "Звучит интригующе."

    l "Пойдём, покажу одно из них."

    menu:

        "Пойти с Леной":

            jump kayter_go_with_lena

        "Отказаться и продолжить прогулку":

            jump kayter_decline_lena

label kayter_go_with_lena:

    scene bg city_hidden_place

    with fade

    l "Это место называют 'Точкой Слияния'. Здесь границы между мирами особенно тонки."

    k "Почему ты мне это показываешь?"

    l "Потому что ты особенный. И скоро тебе предстоит сделать выбор."

    k "Какой выбор?"

    l "Между реальностями. Но пока рано об этом говорить."

    # Омуть появляется

    show shadow at center with fade

    shadow "Ты не сможешь избежать своей судьбы."

    k "Опять ты!"

    l "Не слушай его."

    shadow "Она не говорит тебе всей правды."

    menu:

        "Довериться Лене":

            jump kayter_trust_lena

        "Слушать Омуть":

            jump kayter_listen_shadow

label kayter_trust_lena:

    k "Я доверяю Лене."

    l "Хороший выбор."

    shadow "Это ещё не конец..."

    "Омуть исчезла, оставив вас наедине."

    l "У нас мало времени. Я помогу тебе понять свои способности."

    # Обучение от Лены

    return

label kayter_listen_shadow:

    k "Что ты хочешь сказать?"

    shadow "Лена использует тебя для своих целей."

    l "Не слушай его!"

    shadow "Она ведёт тебя по ложному пути."

    menu:

        "Спросить Лену о её намерениях":

            jump kayter_confront_lena

        "Уйти от них обоих":

            jump kayter_leave_both

label kayter_confront_lena:

    k "Лена, это правда? Что ты скрываешь?"

    l "(вздыхая) Хорошо. Возможно, я не всё тебе рассказала."

    l "Но я действительно хочу помочь."

    # Разговор с Леной

    return

label kayter_leave_both:

    k "Мне нужно побыть одному."

    "Вы разворачиваетесь и уходите, оставляя Лену и Омуть позади."

    scene bg city_street_evening

    k "Слишком много всего... Мне нужно всё обдумать."

    # Продолжение сюжета

    return

label kayter_decline_lena:

    k "Спасибо, но, пожалуй, откажусь."

    l "Как хочешь. Но если передумаешь, я буду здесь."

    "Вы продолжаете прогулку по парку."

    # Продолжение сюжета

    return

# Сон и встреча с Омутью

label kayter_dream:

    scene bg dream_world

    with fade

    show kayter normal at center

    k "Где я? Это какой-то сон?"

    show shadow at right with dissolve

    shadow "Это больше, чем сон, Кейтер."

    k "Омуть... Что тебе нужно?"

    shadow "Предупредить тебя. Границы между мирами стираются."

    k "Почему это происходит?"

    shadow "Ты — ключ к равновесию. Твой выбор определит исход."

    k "Какой выбор?"

    shadow "Скоро узнаешь..."

    "Вдруг всё вокруг начинает растворяться."

    scene bg kayter_apartment

    with fade

    k "(просыпаясь) Какой странный сон..."

    # Продолжение сюжета

    return

# Сюжетная линия Надежды

label nadezhda_route:

    scene bg nadezhda_apartment

    show nadezhda sad at center

    n "Снова эта пустота внутри..."

    n "Переезд не помог забыть прошлое. Воспоминания всё ещё преследуют меня."

    n "Может, стоит поговорить с Леной. Она всегда знает, что сказать."

    menu:

        "Позвонить Лене":

            jump nadezhda_call_lena

        "Остаться дома":

            jump nadezhda_stay_home

label nadezhda_call_lena:

    n "Нужно набрать её номер."

    "Вы берёте телефон и звоните."

    l "Привет, Найда."

    n "Привет. Можем встретиться?"

    l "Конечно. Приходи в наше место."

    # Встреча с Леной

    scene bg city_hidden_place

    with fade

    show nadezhda sad at left

    show lena mysterious at right

    n "Мне снова снятся эти сны."

    l "Они становятся ярче?"

    n "Да. И ещё... Я чувствую чьё-то присутствие."

    l "Это Омуть. Она пытается проникнуть в твоё сознание."

    n "Что мне делать?"

    l "Ты должна принять своё прошлое. Только так ты сможешь освободиться."

    # Омуть появляется

    show shadow at center with fade

    shadow "Ты не сможешь убежать от меня."

    n "Оставь меня!"

    l "Найда, сосредоточься!"

    menu:

        "Противостоять Тени":

            jump nadezhda_confront_shadow

        "Сдаться":

            jump nadezhda_give_in

label nadezhda_confront_shadow:

    n "Я не боюсь тебя!"

    shadow "Посмотрим..."

    "Омуть начинает отступать."

    l "Хорошо! Ты справляешься!"

    shadow "Мы ещё встретимся..."

    "Омуть исчезает."

    n "(облегчённо) Спасибо, Лена."

    l "Это только начало. Тебе предстоит ещё многое узнать."

    # Продолжение сюжета

    return

label nadezhda_give_in:

    n "У меня нет сил бороться..."

    shadow "Ха-ха-ха..."

    l "Найда, нет!"

    "Омуть поглощает вас, и всё вокруг меркнет."

    # Плохая концовка

    return

label nadezhda_stay_home:

    n "Нет, не хочу никого видеть."

    "Вы ложитесь на кровать и закрываете глаза."

    # Сон и встреча с Омутью

    jump nadezhda_dream

label nadezhda_dream:

    scene bg dream_world

    with fade

    show nadezhda sad at center

    n "Где я?"

    show shadow at right with dissolve

    shadow "Наконец-то мы одни."

    n "Кто ты?"

    shadow "Я — твои страхи. Твоё прошлое."

    n "Оставь меня в покое!"

    shadow "Ты не сможешь убежать."

    menu:

        "Попытаться убежать":

            jump nadezhda_try_escape

        "Спросить, чего он хочет":

            jump nadezhda_ask_shadow

label nadezhda_try_escape:

    "Вы пытаетесь бежать, но ноги не слушаются."

    shadow "Бесполезно..."

    "Омуть приближается."

    # Плохая концовка

    return

label nadezhda_ask_shadow:

    n "Что тебе нужно?"

    shadow "Прими меня. Только так ты сможешь стать целой."

    n "Принять свои страхи..."

    "Вы протягиваете руку к Тени."

    shadow "Хороший выбор."

    "Омуть сливается с вами, и вы чувствуете облегчение."

    # Хорошая концовка

    return

# Конец игры

label end_game:

    scene black

    show text "Спасибо за игру!" at truecenter with dissolve

    pause 3

    return
