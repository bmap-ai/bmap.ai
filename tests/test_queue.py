"""
Test Queue Manager
"""

import sys
sys.path.append('..')
from core.queue_manager import QueueManager

def test_queue():
    manager = QueueManager()
    
    # Test regular queue
    manager.add_task("task1", {"data": "test1"})
    manager.add_task("task2", {"data": "test2"})
    
    task_id, task_data = manager.get_task()
    assert task_id == "task1"
    
    # Test priority queue
    manager.add_priority_task(2, "low", {"priority": "low"})
    manager.add_priority_task(1, "high", {"priority": "high"})
    
    task_id, task_data = manager.get_task()
    assert task_id == "high"
    
    # Test results
    manager.store_result("task1", {"result": "success"})
    result = manager.get_result("task1")
    assert result["result"] == "success"
    
    print("Queue test passed!")

if __name__ == "__main__":
    test_queue()