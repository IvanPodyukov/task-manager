import json

from task import Task
from typing import List, Optional


class TaskManager:
    """
    Класс для управления задачами, включая добавление,
    удаление, поиск и сохранение задач.

    Позволяет загружать задачи из файла, добавлять новые,
    изменять и удалять существующие,
    фильтровать по статусу и ключевым словам,
    а также сохранять изменения в файл.
    """

    def __init__(self, storage_file: str):
        """
        Инициализирует объект менеджера задач.

        :param storage_file: Путь к файлу, в котором хранятся задачи.
        """
        self.storage_file = storage_file
        self.tasks = self.load_tasks()
        self.task_id = max((task.id for task in self.tasks), default=0) + 1

    @property
    def size(self) -> int:
        """
        Возвращает количество задач в списке.

        :return: Количество задач.
        """
        return len(self.tasks)

    def load_tasks(self) -> List[Task]:
        """
        Загружает задачи из файла.

        Если файл не найден или поврежден, возвращает пустой список.

        :return: Список объектов Task.
        """
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_task(self, title: str, description: str,
                 category: str, due_date: str, priority: str) -> None:
        """
        Добавляет новую задачу в список.

        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи.
        :param due_date: Срок выполнения задачи в формате 'ГГГГ-ММ-ДД'.
        :param priority: Приоритет задачи ('Низкий', 'Средний', 'Высокий').
        """
        task = Task(self.task_id, title, description,
                    category, due_date, priority)
        self.task_id += 1
        self.tasks.append(task)

    def delete_task(self, value: Task | str) -> None:
        """
        Удаляет задачу или все задачи в указанной категории.

        :param value: Задача для удаления или название категории
        для удаления всех задач этой категории.
        """
        if isinstance(value, Task):
            self.tasks.remove(value)
        else:
            category_tasks = [task for task in self.tasks
                              if task.category == value]
            for task in category_tasks:
                self.tasks.remove(task)

    def get_categories(self) -> List[str]:
        """
        Возвращает список всех уникальных категорий задач.

        :return: Список категорий.
        """
        categories = set(task.category for task in self.tasks)
        return list(categories)

    def get_tasks(self, category: Optional[str] = None) -> List[Task]:
        """
        Возвращает список задач, фильтруя по категории (если указана).

        Задачи сортируются по сроку выполнения.

        :param category: Категория для фильтрации задач.
        Если None, возвращаются все задачи.
        :return: Список задач.
        """
        filtered_tasks = sorted((task for task in self.tasks
                                 if category is None
                                 or task.category == category),
                                key=lambda task: task.due_date)
        return filtered_tasks

    def get_tasks_by_status(self, status: str) -> List[Task]:
        """
        Возвращает задачи, фильтруя по статусу.

        Задачи сортируются по сроку выполнения.

        :param status: Статус задач для фильтрации
        ('Не выполнена' или 'Выполнена').
        :return: Список задач.
        """
        filtered_tasks = sorted((task for task in self.tasks
                                 if task.status == status),
                                key=lambda task: task.due_date)
        return filtered_tasks

    def get_tasks_by_keyword(self, keyword: str) -> List[Task]:
        """
        Возвращает задачи, которые содержат
        ключевое слово в названии или описании.

        Задачи сортируются по сроку выполнения.

        :param keyword: Ключевое слово для поиска.
        :return: Список задач.
        """
        keyword = keyword.lower()
        filtered_tasks = sorted(
            (task for task in self.tasks
             if keyword in task.title.lower()
             or keyword in task.description.lower()),
            key=lambda task: task.due_date)
        return filtered_tasks

    def save_tasks(self, file_name: str) -> None:
        """
        Сохраняет все задачи в файл.

        :param file_name: Название файла для сохранения задач.
        :raise json.JSONDecodeError: Если произошла ошибка при сохранении.
        """
        try:
            with open(file_name, 'w') as file:
                tasks_json = [task.to_dict() for task in self.tasks]
                json.dump(tasks_json, file)
        except json.JSONDecodeError:
            print('Сохранить задачи не удалось')
