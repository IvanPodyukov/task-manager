import pytest
import json
from task_manager import TaskManager


@pytest.fixture
def setup_temp_file(tmp_path):
    file_path = tmp_path / 'tasks.json'
    return str(file_path)


@pytest.fixture
def setup_task_manager(setup_temp_file):
    return TaskManager(setup_temp_file)


def test_initialization_with_empty_file(setup_task_manager):
    manager = setup_task_manager
    assert manager.tasks == []
    assert manager.task_id == 1


def test_size(setup_task_manager):
    manager = setup_task_manager
    assert manager.size == 0
    manager.add_task('Test Task', 'Description', 'Work',
                     '2024-12-01', 'Высокий')
    assert manager.size == 1


def test_add_task(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Test Task', 'Description', 'Work',
                     '2024-12-01', 'Высокий')
    assert len(manager.tasks) == 1
    task = manager.tasks[0]
    assert task.title == 'Test Task'
    assert task.description == 'Description'
    assert task.category == 'Work'
    assert task.due_date == '2024-12-01'
    assert task.priority == 'Высокий'
    assert task.id == 1


def test_delete_task_by_object(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-01', 'Высокий')
    task_to_delete = manager.tasks[0]
    manager.delete_task(task_to_delete)
    assert len(manager.tasks) == 0


def test_delete_task_by_category(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-01', 'Высокий')
    manager.add_task('Task 2', 'Description 2', 'Personal',
                     '2024-12-02', 'Средний')
    manager.delete_task('Work')
    assert len(manager.tasks) == 1
    assert manager.tasks[0].category == 'Personal'


def test_get_categories(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-01', 'Высокий')
    manager.add_task('Task 2', 'Description 2', 'Personal',
                     '2024-12-02', 'Средний')
    categories = manager.get_categories()
    assert sorted(categories) == ['Personal', 'Work']


def test_get_tasks(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-02', 'Высокий')
    manager.add_task('Task 2', 'Description 2', 'Work',
                     '2024-12-01', 'Средний')
    tasks = manager.get_tasks('Work')
    assert len(tasks) == 2
    assert tasks[0].due_date == '2024-12-01'  # Проверка сортировки по дате


def test_get_tasks_by_status(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-01', 'Высокий')
    task = manager.tasks[0]
    task.status = 'Выполнена'
    tasks = manager.get_tasks_by_status('Выполнена')
    assert len(tasks) == 1
    assert tasks[0].status == 'Выполнена'


def test_get_tasks_by_keyword(setup_task_manager):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-01', 'Высокий')
    manager.add_task('Another Task', 'Some description', 'Work',
                     '2024-12-02', 'Средний')
    tasks = manager.get_tasks_by_keyword('another')
    assert len(tasks) == 1
    assert tasks[0].title == 'Another Task'


def test_save_tasks(setup_task_manager, setup_temp_file):
    manager = setup_task_manager
    manager.add_task('Task 1', 'Description 1', 'Work',
                     '2024-12-01', 'Высокий')
    manager.save_tasks(setup_temp_file)
    with open(setup_temp_file, 'r') as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]['title'] == 'Task 1'


def test_load_tasks(setup_temp_file):
    task_data = [
        {
            'id': 1,
            'title': 'Task 1',
            'description': 'Description 1',
            'category': 'Work',
            'due_date': '2024-12-01',
            'priority': 'Высокий',
            'status': 'Не выполнена'
        }
    ]
    with open(setup_temp_file, 'w') as file:
        json.dump(task_data, file)
    manager = TaskManager(setup_temp_file)
    assert len(manager.tasks) == 1
    task = manager.tasks[0]
    assert task.title == 'Task 1'
    assert task.id == 1
