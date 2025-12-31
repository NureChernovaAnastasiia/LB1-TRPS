import pytest
from todo import TodoList


class TestAddTask:
    def test_add_task_success(self):
        todo = TodoList()
        index = todo.add_task("Buy milk")
        assert index == 0
        assert todo.task_count() == 1

    def test_add_multiple_tasks(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        todo.add_task("Task 3")
        assert todo.task_count() == 3

    def test_add_empty_task(self):
        todo = TodoList()
        with pytest.raises(ValueError, match="Task cannot be empty"):
            todo.add_task("")

    def test_add_whitespace_task(self):
        todo = TodoList()
        with pytest.raises(ValueError, match="Task cannot be empty"):
            todo.add_task("   ")


class TestRemoveTask:
    def test_remove_task_success(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        removed = todo.remove_task(0)
        assert removed["task"] == "Task 1"
        assert todo.task_count() == 1

    def test_remove_invalid_index(self):
        todo = TodoList()
        todo.add_task("Task 1")
        with pytest.raises(IndexError, match="Task index out of range"):
            todo.remove_task(5)

    def test_remove_negative_index(self):
        todo = TodoList()
        todo.add_task("Task 1")
        with pytest.raises(IndexError, match="Task index out of range"):
            todo.remove_task(-1)


class TestCompleteTask:
    def test_complete_task_success(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.complete_task(0)
        tasks = todo.get_all_tasks()
        assert tasks[0]["completed"] is True

    def test_uncomplete_task(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.complete_task(0)
        todo.uncomplete_task(0)
        tasks = todo.get_all_tasks()
        assert tasks[0]["completed"] is False

    def test_complete_invalid_index(self):
        todo = TodoList()
        with pytest.raises(IndexError, match="Task index out of range"):
            todo.complete_task(0)


class TestGetTasks:
    def test_get_all_tasks(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        tasks = todo.get_all_tasks()
        assert len(tasks) == 2

    def test_get_completed_tasks(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        todo.add_task("Task 3")
        todo.complete_task(0)
        todo.complete_task(2)
        completed = todo.get_completed_tasks()
        assert len(completed) == 2

    def test_get_pending_tasks(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        todo.add_task("Task 3")
        todo.complete_task(1)
        pending = todo.get_pending_tasks()
        assert len(pending) == 2


class TestClearCompleted:
    def test_clear_completed_tasks(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        todo.add_task("Task 3")
        todo.complete_task(0)
        todo.complete_task(2)
        removed = todo.clear_completed()
        assert removed == 2
        assert todo.task_count() == 1

    def test_clear_no_completed(self):
        todo = TodoList()
        todo.add_task("Task 1")
        removed = todo.clear_completed()
        assert removed == 0


class TestCounts:
    def test_task_count(self):
        todo = TodoList()
        assert todo.task_count() == 0
        todo.add_task("Task 1")
        assert todo.task_count() == 1

    def test_completed_count(self):
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        todo.complete_task(0)
        assert todo.completed_count() == 1
        assert todo.pending_count() == 1
