from __future__ import annotations

from datetime import datetime
from typing import Dict


class Task:
    """
    Класс для представления задачи.

    Каждая задача имеет уникальный ID, название, описание, категорию,
    срок выполнения, приоритет и статус.
    """

    def __init__(self, task_id: int, title: str, description: str,
                 category: str, due_date: str, priority: str):
        """
        Инициализирует новый объект задачи.

        :param task_id: Уникальный идентификатор задачи.
        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи.
        :param due_date: Срок выполнения задачи в формате 'ГГГГ-ММ-ДД'.
        :param priority: Приоритет задачи ('Низкий', 'Средний', 'Высокий').
        """
        self._id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = 'Не выполнена'

    @property
    def id(self) -> int:
        """
        Возвращает ID задачи.

        :return: Уникальный идентификатор задачи.
        """
        return self._id

    @property
    def title(self) -> str:
        """
        Возвращает название задачи.

        :return: Название задачи.
        """
        return self._title

    @title.setter
    def title(self, value: str):
        """
        Устанавливает название задачи.

        :param value: Новое название задачи.
        :raise ValueError: Если название пустое.
        """
        if not value:
            raise ValueError('Название задачи не может быть пустым')
        self._title = value

    @property
    def description(self) -> str:
        """
        Возвращает описание задачи.

        :return: Описание задачи.
        """
        return self._description

    @description.setter
    def description(self, value: str):
        """
        Устанавливает описание задачи.

        :param value: Новое описание задачи.
        :raise ValueError: Если описание пустое.
        """
        if not value:
            raise ValueError('Описание задачи не может быть пустым')
        self._description = value

    @property
    def category(self) -> str:
        """
        Возвращает категорию задачи.

        :return: Категория задачи.
        """
        return self._category

    @category.setter
    def category(self, value: str):
        """
        Устанавливает категорию задачи.

        :param value: Новая категория задачи.
        :raise ValueError: Если категория пустая.
        """
        if not value:
            raise ValueError('Категория задачи не может быть пустой')
        self._category = value

    @property
    def due_date(self) -> str:
        """
        Возвращает срок выполнения задачи.

        :return: Срок выполнения задачи в формате 'ГГГГ-ММ-ДД'.
        """
        return self._due_date

    @due_date.setter
    def due_date(self, value: str):
        """
        Устанавливает срок выполнения задачи.

        :param value: Новый срок выполнения задачи в формате 'ГГГГ-ММ-ДД'.
        :raise ValueError: Если срок выполнения не соответствует формату.
        """
        try:
            datetime.strptime(value, '%Y-%m-%d')
            self._due_date = value
        except ValueError:
            raise ValueError('Срок выполнения задачи должен быть '
                             'в формате ГГГГ-ММ-ДД')

    @property
    def priority(self) -> str:
        """
        Возвращает приоритет задачи.

        :return: Приоритет задачи ('Низкий', 'Средний', 'Высокий').
        """
        return self._priority

    @priority.setter
    def priority(self, value: str):
        """
        Устанавливает приоритет задачи.

        :param value: Новый приоритет задачи ('Низкий', 'Средний', 'Высокий').
        :raise ValueError: Если приоритет не соответствует
        допустимым значениям.
        """
        if value not in ('Низкий', 'Средний', 'Высокий'):
            raise ValueError('Приоритет задачи должен '
                             'быть низким, средним или высоким')
        self._priority = value

    @property
    def status(self) -> str:
        """
        Возвращает статус задачи.

        :return: Статус задачи ('Не выполнена', 'Выполнена').
        """
        return self._status

    @status.setter
    def status(self, value: str):
        """
        Устанавливает статус задачи.

        :param value: Новый статус задачи ('Не выполнена', 'Выполнена').
        :raise ValueError: Если статус не соответствует допустимым значениям.
        """
        if value not in ('Не выполнена', 'Выполнена'):
            raise ValueError('Задача должна быть '
                             'выполненной или не выполненной')
        self._status = value

    def to_dict(self) -> Dict:
        """
        Преобразует объект задачи в словарь.

        :return: Словарь, представляющий задачу.
        """
        return {
            'id': self._id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data: Dict) -> Task:
        """
        Создает объект задачи из словаря.

        :param data: Словарь, содержащий данные задачи.
        :return: Новый объект Task.
        """
        task = Task(data['id'], data['title'], data['description'],
                    data['category'], data['due_date'], data['priority'])
        task.status = data['status']
        return task
