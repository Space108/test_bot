<h2>Телеграмм бот для проведения викторины по тестированию.</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи

Телеграмм-бот предназначен для проведения викторины с пользователями. Он отправляет вопросы в виде опросов и проверяет правильность ответов,
давая разъяснения в зависимости от правильности ответа. Бот также может считать количество символов в тексте, который пользователь отправляет командой.
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
   Отправляет вопросы в виде опросов через бот. Вопросы и варианты ответа перемешиваются,
   и отправляется соответствующий правильный ответ.

   
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
