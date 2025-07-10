"""
Event Bus for pub/sub
"""

from typing import Dict, List, Callable
from collections import defaultdict

class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)
        
    def subscribe(self, event_type: str, handler: Callable):
        """Subscribe to an event"""
        self.subscribers[event_type].append(handler)
        
    def unsubscribe(self, event_type: str, handler: Callable):
        """Unsubscribe from an event"""
        if handler in self.subscribers[event_type]:
            self.subscribers[event_type].remove(handler)
            
    def publish(self, event_type: str, data: any):
        """Publish an event"""
        for handler in self.subscribers[event_type]:
            try:
                handler(data)
            except Exception as e:
                print(f"Error in event handler: {e}")
                
    def clear(self, event_type: str = None):
        """Clear subscribers"""
        if event_type:
            self.subscribers[event_type] = []
        else:
            self.subscribers.clear()

# Global event bus
event_bus = EventBus()