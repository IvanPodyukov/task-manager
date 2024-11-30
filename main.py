from task_io import (print_tasks, input_category, input_date,
                     input_str, input_priority, input_task, input_status,
                     print_menu, print_edit_menu, print_search_menu)
from task_manager import TaskManager


def handle_view_tasks(task_manager: TaskManager) -> None:
    """
    Отображает список всех задач.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    tasks = task_manager.get_tasks(category=None)
    print_tasks(tasks)


def handle_view_tasks_group_by_categories(task_manager: TaskManager) -> None:
    """
    Отображает задачи, сгруппированные по категориям.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    categories = task_manager.get_categories()
    tasks = task_manager.get_tasks(category=None)
    for i, category in enumerate(categories):
        print(f'\n{i + 1}. {category}')
        print_tasks([task for task in tasks if task.category == category])


def handle_add_task(task_manager: TaskManager) -> None:
    """
    Добавляет новую задачу в TaskManager.

    Запрашивает у пользователя данные: название, описание, категорию,
    срок выполнения и приоритет задачи.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    title = input_str('\nВведите название: ')
    description = input_str('\nВведите описание: ')
    categories = task_manager.get_categories()
    category = input_category('\nВведите категорию: ', categories)
    due_date = input_date('\nВведите срок выполнения (в формате ГГГГ-ММ-ДД): ')
    priority = input_priority('\nВведите приоритет (1 - низкий, '
                              '2 - средний, 3 - высокий): ')
    task_manager.add_task(title, description, category, due_date, priority)


def handle_edit_task(task_manager: TaskManager) -> None:
    """
    Позволяет редактировать существующую задачу.

    Пользователь выбирает задачу по ID, затем может изменять её атрибуты:
    название, описание, категорию, срок выполнения, приоритет и статус.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    tasks = task_manager.get_tasks(category=None)
    print_tasks(tasks)
    task = input_task('\nВведите id задачи, которую вы хотите изменить: ',
                      tasks)
    while True:
        print_edit_menu(task)
        edit_choice = input('\nВыберите действие: ')
        match edit_choice:
            case '1':
                title = input_str('Введите название: ')
                task.title = title
            case '2':
                description = input_str('\nВведите описание: ')
                task.description = description
            case '3':
                categories = task_manager.get_categories()
                category = input_category('\nВведите категорию: ', categories)
                task.category = category
            case '4':
                due_date = input_date('\nВведите срок выполнения '
                                      '(в формате ГГГГ-ММ-ДД): ')
                task.due_date = due_date
            case '5':
                priority = input_priority('\nВведите приоритет (1 - низкий, '
                                          '2 - средний, 3 - высокий): ')
                task.priority = priority
            case '6':
                status = input_status('\nВведите статус (1 - "не выполнена",'
                                      ' 2 - "выполнена"): ')
                task.status = status
            case '7':
                print('\nРедактирование задачи завершено')
                break
            case _:
                print('\nНекорректный ввод')


def handle_delete_task(task_manager: TaskManager) -> None:
    """
    Удаляет задачу по ID или все задачи указанной категории.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    tasks = task_manager.get_tasks(category=None)
    print_tasks(tasks)
    while True:
        delete_str = input('\nВведите тип удаления (1 - по id задачи, '
                           '2 - по категории задачи): ')
        match delete_str:
            case '1':
                task = input_task('\nВведите id задачи, '
                                  'которую вы хотите удалить: ',
                                  tasks)
                task_manager.delete_task(task)
                print(f'\nЗадача с id = {task.id} успешно удалена')
                break
            case '2':
                categories = task_manager.get_categories()
                category = input_category('\nВведите категорию: ',
                                          categories, can_create=False)
                task_manager.delete_task(category)
                print(f'\nЗадачи категории {category} успешно удалены')
                break
            case _:
                print('\nНекорректный ввод')


def handle_search_task(task_manager: TaskManager) -> None:
    """
    Осуществляет поиск задач по ключевому слову, категории или статусу.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    print_search_menu()
    while True:
        search_str = input('\nВведите действие: ')
        match search_str:
            case '1':
                keyword = input_str('\nВведите ключевое слово: ')
                tasks = task_manager.get_tasks_by_keyword(keyword=keyword)
                print_tasks(tasks)
            case '2':
                categories = task_manager.get_categories()
                category = input_category('\nВведите категорию: ',
                                          categories, can_create=False)
                tasks = task_manager.get_tasks(category=category)
                print_tasks(tasks)
            case '3':
                status = input_status('\nВведите статус (1 - "не выполнена",'
                                      ' 2 - "выполнена"): ')
                tasks = task_manager.get_tasks_by_status(status=status)
                print_tasks(tasks)
            case _:
                print('\nНекорректный ввод')


def handle_save_tasks(task_manager: TaskManager) -> None:
    """
    Сохраняет список задач в указанный файл.

    :param task_manager: Экземпляр класса TaskManager, управляющий задачами.
    """
    file_name = input_str('\nВведите название файла, куда '
                          'вы хотите сохранить задачи: ')
    task_manager.save_tasks(file_name)


def main():
    """
    Основная функция программы.

    Управляет взаимодействием с пользователем через текстовый интерфейс.
    Обрабатывает действия пользователя через соответствующие обработчики.

    """
    storage_file = input('\nВведите название файла с '
                         'задачами (или оставьте пустым): ')
    task_manager = TaskManager(storage_file)
    while True:
        print_menu(task_manager.size)
        choice = input('\nВыберите действие: ')
        if task_manager.size > 0:
            match choice:
                case '1':
                    handle_view_tasks(task_manager)
                case '2':
                    handle_view_tasks_group_by_categories(task_manager)
                case '3':
                    handle_add_task(task_manager)
                case '4':
                    handle_edit_task(task_manager)
                case '5':
                    handle_delete_task(task_manager)
                case '6':
                    handle_search_task(task_manager)
                case '7':
                    handle_save_tasks(task_manager)
                case '8':
                    exit()
                case _:
                    print('\nНекорректный ввод.')
        else:
            match choice:
                case '1':
                    handle_add_task(task_manager)
                case '2':
                    exit()
                case _:
                    print('\nНекорректный ввод.')


if __name__ == '__main__':
    main()
