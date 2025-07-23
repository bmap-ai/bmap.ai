"""
Queue Management for async processing
"""

from queue import Queue, PriorityQueue
import threading

class QueueManager:
    def __init__(self):
        self.task_queue = Queue()
        self.priority_queue = PriorityQueue()
        self.results = {}
        self.lock = threading.Lock()
        
    def add_task(self, task_id, task_data):
        """Add task to queue"""
        self.task_queue.put((task_id, task_data))
    
    def add_priority_task(self, priority, task_id, task_data):
        """Add priority task"""
        self.priority_queue.put((priority, task_id, task_data))
    
    def get_task(self):
        """Get next task"""
        if not self.priority_queue.empty():
            return self.priority_queue.get()[1:]
        return self.task_queue.get()
    
    def store_result(self, task_id, result):
        """Store task result"""
        with self.lock:
            self.results[task_id] = result
    
    def get_result(self, task_id):
        """Get task result"""
        with self.lock:
            return self.results.get(task_id)