import pytest
from task import Task


def test_task_initialization():
    task = Task(1, 'Test Task', 'Description', 'Work', '2024-12-01', 'Высокий')
    assert task.id == 1
    assert task.title == 'Test Task'
    assert task.description == 'Description'
    assert task.category == 'Work'
    assert task.due_date == '2024-12-01'
    assert task.priority == 'Высокий'
    assert task.status == 'Не выполнена'


def test_title_setter():
    task = Task(2, 'Title', 'Desc', 'Category', '2024-12-01', 'Средний')
    task.title = 'New Title'
    assert task.title == 'New Title'
    with pytest.raises(ValueError):
        task.title = ''


def test_description_setter():
    task = Task(3, 'Title', 'Desc', 'Category', '2024-12-01', 'Низкий')
    task.description = 'New Description'
    assert task.description == 'New Description'
    with pytest.raises(ValueError):
        task.description = ''


def test_category_setter():
    task = Task(4, 'Title', 'Desc', 'Category', '2024-12-01', 'Средний')
    task.category = 'New Category'
    assert task.category == 'New Category'
    with pytest.raises(ValueError):
        task.category = ''


def test_due_date_setter():
    task = Task(5, 'Title', 'Desc', 'Category', '2024-12-01', 'Низкий')
    task.due_date = '2025-01-01'
    assert task.due_date == '2025-01-01'
    with pytest.raises(ValueError):
        task.due_date = '01-01-2025'


def test_priority_setter():
    task = Task(6, 'Title', 'Desc', 'Category', '2024-12-01', 'Средний')
    task.priority = 'Низкий'
    assert task.priority == 'Низкий'
    with pytest.raises(ValueError):
        task.priority = 'Unknown'


def test_status_setter():
    task = Task(7, 'Title', 'Desc', 'Category', '2024-12-01', 'Высокий')
    task.status = 'Выполнена'
    assert task.status == 'Выполнена'
    with pytest.raises(ValueError):
        task.status = 'In Progress'


def test_to_dict():
    task = Task(8, 'Dict Task', 'Desc', 'Category', '2024-12-01', 'Высокий')
    expected_dict = {
        'id': 8,
        'title': 'Dict Task',
        'description': 'Desc',
        'category': 'Category',
        'due_date': '2024-12-01',
        'priority': 'Высокий',
        'status': 'Не выполнена'
    }
    assert task.to_dict() == expected_dict


def test_from_dict():
    data = {
        'id': 9,
        'title': 'From Dict Task',
        'description': 'Desc',
        'category': 'Category',
        'due_date': '2024-12-01',
        'priority': 'Низкий',
        'status': 'Выполнена'
    }
    task = Task.from_dict(data)
    assert task.id == 9
    assert task.title == 'From Dict Task'
    assert task.description == 'Desc'
    assert task.category == 'Category'
    assert task.due_date == '2024-12-01'
    assert task.priority == 'Низкий'
    assert task.status == 'Выполнена'
