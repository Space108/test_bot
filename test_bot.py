import logging
from telebot import TeleBot, types
import random

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger('quiz_bot')

bot = TeleBot('Вставьте_свой_токен')
questions = [
    {
        #"id": 1,
        "question": "Что такое Авторизация?",
        "options": [
            "Процесс подтверждения личности пользователя",
            "Процесс предоставления прав доступа пользователю",
            "Процесс регистрации нового пользователя",
            "Процесс восстановления пароля пользователя"
        ],
        "correct_option_id": 1,
        "explanation": {
            "correct": "Авторизация — это процесс предоставления прав доступа пользователю после подтверждения его личности.",
            "incorrect": "Неправильно. Авторизация связана с предоставлением прав доступа после подтверждения личности."
        }
    },
    {
        #"id": 2,
        "question": "Что такое Аутентификация?",
        "options": [
            "Процесс подтверждения личности пользователя",
            "Процесс автоматического обновления системы",
            "Метод хранения данных в облаке",
            "Способ шифрования информации"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Верно! Аутентификация подтверждает личность через проверку введённых данных.",
            "incorrect": "Неправильно. Это процесс подтверждения личности, а не просто шифрование или обновление."
        }
    },
    {
        #"id": 3,
        "question": "Что такое идентификация?",
        "options": [
            "Процесс подтверждения личности пользователя",
            "Процесс регистрации нового пользователя",
            "Процесс определения и распознавания личности пользователя",
            "Процесс восстановления пароля пользователя"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Верно! Идентификация — процесс распознавания пользователя для доступа.",
            "incorrect": "Неправильно. Идентификация — это распознавание, а не подтверждение информации."
        }
    },
    {
        #"id": 4,
        "question": "Что такое клиент-серверная архитектура в контексте программного обеспечения?",
        "options": [
            "Модель вычислений, основанная на взаимодействии клиента и сервера для повышения производительности",
            "Метод разработки ПО без использования сети",
            "Структура ПО, где все задачи выполняются на одном устройстве",
            "Стиль кодирования для улучшения читаемости кода"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Клиент-сервер — модель, где сервер дает ресурсы, клиент их запрашивает.",
            "incorrect": "Неправильно. В клиент-сервере сервер дает услуги, клиент их запрашивает."
        }
    },
    {
        #"id": 5,
        "question": "Для чего используются REST и SOAP, и в чем их основные отличия?",
        "options": [
            "Для хранения данных; REST использует XML, SOAP – JSON",
            "Для обмена сообщениями между системами; REST требует строгого формата, SOAP более гибкий",
            "Для создания веб-сервисов; REST легкий на HTTP, SOAP сложный, использует HTTP и SMTP",
            "Для обслуживания баз данных; REST и SOAP идентичны по функциональности"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Правильно! REST легкий, чаще на HTTP. SOAP сложнее, поддерживает HTTP, SMTP.",
            "incorrect": "Неправильно. REST легкий, на HTTP. SOAP сложный,подходит для HTTP и SMTP."
        }
    },
    {
        #"id": 6,
        "question": "Какие существуют виды тестовой документации?",
        "options": [
            "Тест-план, тест-кейсы, отчет о тестировании",
            "Только тест-план и тест-кейсы",
            "Только отчет о тестировании и список ошибок",
            "Тест-кейсы и пользовательская документация"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Документация: тест-план, кейсы и отчеты, а также другие документы.",
            "incorrect": "Неправильно. Документы: план, кейсы, отчеты и другие составляющие тестирования."
        }
    },
    {
        #"id": 7,
        "question": "Какие требования должны быть соблюдены при создании тестовой документации?",
        "options": [
            "Полнота, ясность, актуальность",
            "Краткость, сложность, общие формулировки",
            "Только актуальность и краткость",
            "Только полнота и сложность"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Документация должна быть полной, ясной и актуальной для поддержки тестирования.",
            "incorrect": "Неправильно. Документация должна быть актуальной, краткой, но также полной и ясной."
        }
    },
    {
       # "id": 8,
        "question": "В чем разница между серьезностью (severity) и приоритетом (priority) дефекта?",
        "options": [
            "Серьезность определяет влияние дефекта на систему, а приоритет — порядок исправления.",
            "Приоритет определяет влияние дефекта на систему, а серьезность — порядок исправления.",
            "Нет разницы, это синонимы.",
            "Серьезность связана только с кодом, а приоритет с функциональностью."
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Серьезность — влияние дефекта на систему, приоритет — порядок его исправления.",
            "incorrect": "Неправильно. Серьезность — влияние дефекта на систему, приоритет — срочность его исправления."
        }
    },
    {
        #"id": 9,
       "question": "Какой код указывает на ошибку сервера, а не клиентскую ошибку?",
       "options": [
            "200: Успех",
            "403: Доступ запрещен",
            "500: Внутренняя ошибка сервера",
            "301: Перемещено навсегда"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Верно! Код 500 означает внутреннюю ошибку сервера.",
            "incorrect": "Неправильно. Код 500 обозначает ошибку сервера, в отличие от клиентской ошибки 403."
        }
    },
    {
       # "id": 10,
        "question": "Каковы типы данных в XML и JSON, и в чем заключаются основные отличия между JSON и XML?",
        "options": [
            "Оба используют только строки; JSON сложнее в синтаксисе",
            "JSON поддерживает строки, числа, массивы, объекты, null типы; XML более гибок в представлении данных",
            "XML поддерживает только числа и строки; JSON поддерживает XML типы данных",
            "JSON и XML имеют одинаковый набор типов данных и функциональность"
        ],
        "correct_option_id": 1,
        "explanation": {
            "correct": "Правильно! JSON поддерживает типы данных, XML гибче с пользовательскими тегами.",
            "incorrect": "Неправильно. JSON прост, XML гибкий для сложных структур."
        }
    },
    {
        #"id": 11,
        "question": "Что такое CRUD в контексте работы с базами данных и приложениями?",
        "options": [
            "Набор инструкций для управления памятью в программировании",
            "Сетевой протокол для передачи данных между серверами",
            "Операции для работы с данными, включающие создание, чтение, обновление и удаление",
            "Метод шифрования данных для обеспечения безопасности в интернете"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Правильно! CRUD — операции создания, чтения, обновления и удаления в базах данных.",
            "incorrect": "Неправильно. CRUD — это создание, чтение, обновление и удаление данных в базе."
        }
    },
    {
        #"id": 12,
        "question": "Что из перечисленного выражает основную концепцию архитектурного стиля REST?",
        "options": [
            "Реализация сложных процедурных алгоритмов на сервере",
            "Обмен данными через состояния между клиентом и сервером",
            "Обеспечение гибких и сложных интерфейсов для взаимодействия с пользователем",
            "Использование стандартизованных методов HTTP для взаимодействия с ресурсами"
        ],
        "correct_option_id": 3,
        "explanation": {
            "correct": "REST использует стандартизованные методы HTTP для простоты и масштабируемости.",
            "incorrect": "Неправильно. REST упрощает создание веб-сервисов через стандартизованные методы HTTP."
        }
    },
    {
        #"id": 13,
        "question": "Что такое мок-объекты в тестировании, и как они применяются?",
        "options": [
            "Это реальная версия объекта для интеграционного тестирования",
            "Временный объект, используемый для изоляции тестируемого кода",
            "Набор данных для обеспечения стабильных тестов",
            "Инструмент для автоматизации пользовательского интерфейса"
        ],
        "correct_option_id": 1,
        "explanation": {
            "correct": "Правильно! Мок-объекты используются для изоляции тестируемого кода.",
            "incorrect": "Неправильно. Мок-объекты служат для изоляции и эмуляции зависимостей."

        }
    },
    {
        #"id": 14,
        "question": "Что такое регрессионное тестирование?",
        "options": [
            "Тестирование для проверки, что изменения не сломали существующий функционал",
            "Тестирование новых функций системы на соответствие требованиям",
            "Тестирование системы на ожидаемую нагрузку",
            "Тестирование безопасности системы от внешних угроз"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Регрессионное тестирование проверяет, что изменения не нарушили функционал.",
            "incorrect": "Неправильно. Регрессионное тестирование проверяет, что изменения не сломали функционал."
        }
    },
    {
        #"id": 15,
        "question": "Какая команда выполняет функцию фильтрации текста в файлах по регулярным выражениям?",
        "options": [
            "touch",
            "pwd",
            "cat",
            "grep"
        ],
        "correct_option_id": 3,
        "explanation": {
            "correct": "Правильно! Команда 'grep' используется для поиска и фильтрации текста в файлах.",
            "incorrect": "Неправильно. Правильный ответ — 'grep', которая используется для поиска и фильтрации текста в файлах."
        }
    },
    {
        #"id": 16,
        "question": "Какой командой можно подключиться к серверу для просмотра логов?",
        "options": [
            "FTP",
            "RDP",
            "SSH",
            "HTTP"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Правильно! 'SSH' используется для безопасного подключения к серверу.",
            "incorrect": "Неправильно. Правильный ответ — 'SSH', который используется для подключения к серверу."
        }
    },
    {
        #"id": 17,
        "question": "Какой командой можно скачать файл с сервера на свой компьютер в Linux?",
        "options": [
            "scp",
            "rm",
            "ls",
            "chmod"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Команда scp используется для копирования файлов с сервера.",
            "incorrect": "Неправильно. Правильный ответ — scp, она копирует файлы с сервера."
        }
    },
    {
        #"id": 18,
        "question": "Как называется самый известный аналог Kafka?",
        "options": [
            "RabbitMQ",
            "ActiveMQ",
            "ZeroMQ"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! RabbitMQ часто упоминается как аналог Kafka, хотя они и предназначены для разных задач.",
            "incorrect": "Неправильно. Самый известный аналог Kafka — RabbitMQ, но они применяются для разных задач."
        }
    },
    {
        #"id": 19,
        "question": "Какое основноеотличие между TCP и UDP?",
        "options": [
            "TCP подтверждает доставку, UDP нет",
            "UDP подтверждает доставку, TCP нет",
            "Оба подтверждают доставку",
            "Нет различий"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! TCP подтверждает доставку данных, делая его более надёжным, чем UDP.",
            "incorrect": "Неправильно. TCP подтверждает доставку, в отличие от UDP."
        }
    },
    {
        #"id": 20,
        "question": "Какой из инструментов является сниффером и аналогом Charles?",
        "options": [
            "JMeter",
            "Jenkins",
            "Sentry",
            "Fiddler"
        ],
        "correct_option_id": 3,
        "explanation": {
            "correct": "Правильно! Fiddler используется для анализа HTTP-трафика и является аналогом Charles.",
            "incorrect": "Неправильно. Fiddler — это инструмент для анализа сетевого трафика, похожий на Charles."
        }
    },
    {
        #"id": 21,
        "question": "Какую часть HTTP запроса или ответа можно редактировать с помощью Charles Breakpoints?",
        "options": [
            "Только заголовки",
            "Только тело",
            "Только параметры URL",
            "Любую часть запроса и ответа"
        ],
        "correct_option_id": 3,
        "explanation": {
            "correct": "Правильно! Charles Breakpoints позволяют редактировать любую часть HTTP запроса и ответа.",
            "incorrect": "Неправильно. Через Charles Breakpoints можно изменять любую часть HTTP запроса и ответа."
        }
    },
    {
        #"id": 22,
        "question": "Что такое DOM дерево?",
        "options": [
            "Набор локаторов, используемых на сайте",
            "Набор атрибутов, используемых на сайте",
            "Чек-лист в виде дерева",
            "Представление HTML-документа в виде дерева тегов"
        ],
        "correct_option_id": 3,
        "explanation": {
            "correct": "Правильно! DOM-дерево представляет HTML-документ в виде дерева тегов.",
            "incorrect": "Неправильно. DOM-дерево — это представление HTML-документа в виде дерева тегов."
        }
    },
    {
        #"id": 23,
        "question": "В какой вкладке Devtools можно просмотреть HTML теги и CSS свойства сайта?",
        "options": [
            "Elements",
            "Application",
            "Sources",
            "Console"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Вкладка 'Elements' отображает HTML теги и CSS свойства сайта.",
            "incorrect": "Неправильно. HTML теги и CSS свойства можно просмотреть во вкладке 'Elements'."
        }
    },
    {
        #"id": 24,
        "question": "Что такое CSS?",
        "options": [
            "Скелет сайта, состоящий из тегов",
            "Каскадная таблица стилей для сайта",
            "Скрипты для взаимодействия с бекендом",
            "Counter Strike Source"],
        "correct_option_id": 1,
        "explanation": {
            "correct": "Правильно! CSS — это каскадная таблица стилей, используемая для оформления веб-страниц.",
            "incorrect": "Неправильно. CSS — это каскадная таблица стилей, предназначенная для оформления веб-страниц."
        }
    },
    {
        #"id": 25,
        "question": "В каком формате хранятся данные в MongoDB?",
        "options": [
            "Квери",
            "REST",
            "JSON",
            "XML"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Правильно! В MongoDB данные хранятся в формате BSON, который очень схож с JSON.",
            "incorrect": "Неправильно. В MongoDB данные фактически хранятся в формате BSON, который очень схож с JSON."
        }
    },
    {
        #"id": 26,
        "question": "Какой инструмент позволяет просматривать логи?",
        "options": [
            "Grafana",
            "Splunk","Kibana",
            "Prometheus"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Правильно! Kibana — это инструмент, который позволяет просматривать и анализировать логи.",
            "incorrect": "Неправильно. Правильный ответ — Kibana, инструмент для просмотра и анализа логов."
        }
    },
    {
        #"id": 27,
        "question": "Какой изначально статус присваивается баг-репорту?",
        "options": [
            "Backlog",
            "To Do",
            "In Progress",
            "Ready for test"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! Изначально баг-репорту присваивается статус 'Backlog'.",
            "incorrect": "Неправильно. Ответом является 'Backlog', так как это начальный статус баг-репорта."
        }
    },
    {
        #"id": 28,
        "question": "В чем основное отличие между функциональным и нефункциональным тестированием?",
        "options": [
            "Цель — удобство использования",
            "Проверка производительности системы",
            "Акцент на отказоустойчивости",
            "Охватывает только безопасность"
        ],
        "correct_option_id": 1,
        "explanation": {
        "correct": "Правильно! Нефункциональное тестирование включает проверку производительности.",
        "incorrect": "Неправильно. Нефункциональное тестирование охватывает аспекты, не связанные с функциональностью."

        }
        
    },
    {
        #"id": 29,
        "question": "Что такое чит-лист?",
        "options": [
            "Применение artmoney для тестирования граничных значений",
            "Список универсальных однотипных проверок",
            "Использование QA-инструментов, без покупки лицензии",
            "То же самое, что и чек-лист"
        ],
        "correct_option_id": 1,
        "explanation": {
            "correct": "Правильно! Чит-лист — это список универсальных однотипных проверок.",
            "incorrect": "Неправильно. Чит-лист — это список универсальных однотипных проверок."
        }
    },
    {
        #"id": 30,
        "question": "Что такое класс эквивалентности?",
        "options": [
            "Множество значений на границах",
            "Значения, эквивалентные corner case",
            "Значения, дающие одинаковый результат",
            "Тестирование взаимодействия микросервисов"
        ],
        "correct_option_id": 2,
        "explanation": {
            "correct": "Правильно! Класс эквивалентности — это значения, дающие одинаковый результат.",
            "incorrect": "Неправильно. Класс эквивалентности — это значения, дающие одинаковый результат."
        }
    },
    {
        #"id": 31,
        "question": "Какой командой можно читать логи на сервере в реальном времени?",
        "options": [
            "tail -f",
            "grep",
            "cat",
            "nano"
        ],
        "correct_option_id": 0,
        "explanation": {
            "correct": "Правильно! tail -f позволяет следить за логами в реальном времени.",
            "incorrect": "Неправильно. tail -f используется для чтения логов в реальном времени."
        }
    }
]

user_states = {}

def count_characters(text):
    return len(text)

def send_question(chat_id, question_data):
    # Подсчитываем количество символов в каждом варианте ответа
    option_lengths = [count_characters(option) for option in question_data['options']]

    # Логируем информацию о вопросе и длинах опций
    logger.info(f"Отправка вопроса: {question_data['question']}")
    logger.info(f"Длины опций: {option_lengths}")

    # Отправляем вопрос пользователю
    bot.send_poll(
        chat_id,
        question_data['question'],
        question_data['options'],
        is_anonymous=False,
        type='quiz',
        correct_option_id=question_data['correct_option_id']
    )

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в викторину по тестированию!👨‍💻")
    
    # Перемешиваем список вопросов при старте викторины
    user_states[message.chat.id] = {
        'answered_questions': set(),
        'questions_order': random.sample(range(len(questions)), len(questions))  # Генерируем новый порядок вопросов
    }
    
    send_next_question(message.chat.id)

@bot.message_handler(commands=['count'])
def handle_count_command(message):
    text = message.text.partition(' ')[2]
    if text:
        count = count_characters(text)
        bot.send_message(message.chat.id, f"Количество символов: {count}")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введите текст после команды /count.")

@bot.poll_answer_handler()
def handle_poll_answer(poll_answer):
    chat_id = poll_answer.user.id
    current_state = user_states.get(chat_id)

    if current_state is None:
        return

    current_question_index = len(current_state['answered_questions'])
    question_data = questions[current_state['questions_order'][current_question_index]]  # Используем новый порядок
    correct_answer = question_data['correct_option_id'] == poll_answer.option_ids[0]

    explanation = question_data['explanation']['correct'] if correct_answer else question_data['explanation']['incorrect']
    bot.send_message(chat_id, explanation)
    current_state['answered_questions'].add(current_question_index)
    send_next_question(chat_id)

def send_next_question(chat_id):
    current_state = user_states.get(chat_id)
    if not current_state:
        return

    unanswered_questions = [i for i in range(len(questions)) if i not in current_state['answered_questions']]

    if unanswered_questions:
        next_question_index = unanswered_questions[0]
        send_question(chat_id, questions[current_state['questions_order'][next_question_index]])  # Используем новый порядок
    else:
        finish_quiz(chat_id)

def finish_quiz(chat_id):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Начать заново", callback_data="restart_quiz")
    markup.add(button)
    bot.send_message(chat_id, "Поздравляем! Вы завершили викторину. 🏆✨", reply_markup=markup)
    del user_states[chat_id]

@bot.callback_query_handler(func=lambda call: call.data == "restart_quiz")
def restart_quiz(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Начинаем викторину заново!")
    
    # Перемешиваем список вопросов заново
    user_states[chat_id] = {
        'answered_questions': set(),
        'questions_order': random.sample(range(len(questions)), len(questions))  # Генерируем новый порядок вопросов
    }
    
    send_next_question(chat_id)

bot.polling()

# Разработано Space 108
