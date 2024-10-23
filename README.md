<h2>Телеграмм бот для проведения викторины по тестированию.</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
Бот обрабатывает результаты ответов и отправляет следующее в зависимости от того, верно ли ответил пользователь.


## 🖼 Скриншоты

Стартовое меню:

![image](https://raw.githubusercontent.com/Space108/test_bot/refs/heads/master/Greeting.png)

После выбора запуск:

![image](https://raw.githubusercontent.com/Space108/test_bot/refs/heads/master/Launch.png)


## 💻 Технологии

1. Python - основной язык программирования для написания бота.
2. pyTelegramBotAPI - библиотека Python для работы с API Telegram, используемая для создания и управления ботом.
3. Random - стандартный модуль Python, используемый для перемешивания вопросов и опций.
##     Функции 
   Вопросы отправляются пользователю, варианты ответов перемешиваются, и определяется правильный ответ.
   Бот обрабатывает результаты ответов и отправляет следующее сообщение в зависимости от того, верно ли ответил пользователь.
   
## ⏬ Развертывание на сервере
1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.


``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
import logging
from telebot import TeleBot, types
import random
```
5. Настраиваем логирование
``` markdown
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger('quiz_bot')
```

5. Запускаем
``` markdown
python3 test_bot.py
```

## Автор

Михаил Колядин ([@SpaceKM](https://t.me/SpaceKM))
