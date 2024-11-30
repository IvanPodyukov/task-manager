from datetime import datetime
from typing import List

from tabulate import tabulate

from task import Task


def print_menu(size: int) -> None:
    """
    Выводит меню управления задачами в зависимости от их количества.

    :param size: Количество задач для отображения в меню.
    """
    print(f'\nМенеджер задач. Всего задач: {size}')
    if size > 0:
        print('1. Просмотр всех задач')
        print('2. Просмотр задач по категориям')
        print('3. Добавить задачу')
        print('4. Изменить задачу')
        print('5. Удалить задачу')
        print('6. Поиск задач')
        print('7. Сохранить задачи')
        print('8. Выход')
    else:
        print('1. Добавить задачу')
        print('2. Выход')


def print_tasks(tasks: List[Task]) -> None:
    """
    Выводит список задач в табличном формате.

    :param tasks: Список задач для отображения.
    """
    table = [[
        task.id,
        task.title,
        task.description,
        task.category,
        task.due_date,
        task.priority,
        task.status
    ] for task in tasks]
    headers = ['ID', 'Название', 'Описание', 'Категория',
               'Срок выполнения', 'Приоритет', 'Статус']
    print(tabulate(table, headers=headers, tablefmt='grid'))


def print_categories(categories: List[str]) -> None:
    """
    Выводит список категорий задач.

    :param categories: Список категорий для отображения.
    """
    i = 1
    print('\nКатегория задач')
    for category in categories:
        print(f'{i}. {category}')
        i += 1


def print_edit_menu(task: Task) -> None:
    """
    Выводит меню редактирования задачи.

    :param task: Задача, которую необходимо отредактировать.
    """
    print('\nЗадача')
    print_tasks([task])
    print('1. Изменить название')
    print('2. Изменить описание')
    print('3. Изменить категорию')
    print('4. Изменить срок выполнения')
    print('5. Изменить приоритет')
    print('6. Изменить статус')
    print('7. Завершить редактирование задачи')


def print_search_menu() -> None:
    """
    Выводит меню поиска задач по различным параметрам.
    """
    print('\nПоиск задач')
    print('1. Поиск по ключевым словам')
    print('2. Поиск по категории')
    print('3. Поиск по статусу')


def input_str(prompt: str) -> str:
    """
    Запрашивает строковый ввод от пользователя,
    проверяя, чтобы ввод не был пустым.

    :param prompt: Текст запроса.
    :return: Строковый ввод пользователя.
    """
    while True:
        s = input(prompt)
        if s:
            return s
        print('\nВы ввели пустую строку. Пожалуйста, повторите ввод')


def input_date(prompt: str) -> str:
    """
    Запрашивает строковый ввод от пользователя,
    проверяя, чтобы ввод не был пустым.

    :param prompt: Текст запроса.
    :return: Строковый ввод пользователя.
    """
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print('\nНекорректная дата. Пожалуйста, '
                  'введите дату в формате ГГГГ-ММ-ДД')


def input_priority(prompt: str) -> str:
    """
    Запрашивает у пользователя выбор приоритета задачи
    и проверяет корректность ввода.

    :param prompt: Текст запроса.
    :return: Приоритет задачи ('Низкий', 'Средний', 'Высокий').
    """
    while True:
        priority_str = input(prompt)
        match priority_str:
            case '1':
                return 'Низкий'
            case '2':
                return 'Средний'
            case '3':
                return 'Высокий'
            case _:
                print('\nНекорректный ввод. Введите число от 1 до 3')


def input_status(prompt: str) -> str:
    """
    Запрашивает у пользователя выбор статуса задачи
    и проверяет корректность ввода.

    :param prompt: Текст запроса.
    :return: Статус задачи ('Не выполнена' или 'Выполнена').
    """
    while True:
        status_str = input(prompt)
        match status_str:
            case '1':
                return 'Не выполнена'
            case '2':
                return 'Выполнена'
            case _:
                print('\nНекорректный ввод. Введите число от 1 до 2')


def input_task(prompt: str, tasks: List[Task]) -> Task:
    """
    Запрашивает у пользователя ввод ID задачи
    и возвращает соответствующую задачу.

    :param prompt: Текст запроса.
    :param tasks: Список задач для поиска.
    :return: Задача с введенным ID.
    """
    while True:
        task_str = input(prompt)
        try:
            task_id = int(task_str)
            for task in tasks:
                if task.id == task_id:
                    return task
            raise ValueError
        except ValueError:
            print('\nНекорректный ввод')


def input_category(prompt: str, categories: List[str],
                   can_create: bool = True) -> str:
    """
    Запрашивает у пользователя выбор категории задачи
    с возможностью создания новой категории.

    :param prompt: Текст запроса.
    :param categories: Список доступных категорий.
    :param can_create: Флаг, разрешающий создание новой категории.
    :return: Выбранная категория.
    """
    while True:
        print_categories(categories)
        i = len(categories) + 1
        if can_create:
            print(f'{i}. Создать новую')
        category_str = input(prompt)
        try:
            category_int = int(category_str)
            if can_create and category_int == i:
                return input_str('\nВведите название категории: ')
            else:
                return categories[category_int - 1]
        except (ValueError, IndexError):
            print('\nНекорректный ввод. Пожалуйста, повторите')
