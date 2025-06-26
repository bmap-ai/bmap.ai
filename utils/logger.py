"""
Logging Configuration
"""

import logging
import sys
from datetime import datetime

def setup_logger(name, level=logging.INFO):
    """Setup logger with formatting"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    # Add handler
    logger.addHandler(console_handler)
    
    return logger

# Create default logger
logger = setup_logger('bmap.ai')