from task_report import add_new_entry
import pytest

def test_add_new_entry():
    assert add_new_entry("Fri Feb 23 01:27:40 2024", "Advance", "Tasks Completed") == ("Fri Feb 23 01:27:40 2024 -> SUBJECT: Advance day 1 DESCRIPTION: First Tasks Completed")
    assert add_new_entry("Fri Feb 23 01:27:40 2024", "Advance", "Tasks Completed") == ("Fri Feb 23 01:30:29 2024 -> SUBJECT: Advance day 2 DESCRIPTION: Second Tasks Completed")