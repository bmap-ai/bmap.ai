"""
Test Data Validation
"""

import sys
sys.path.append('..')
from core.data_validation import DataValidator

def test_validation():
    validator = DataValidator()
    
    # Test address validation
    valid_address = "0x" + "a" * 40
    invalid_address = "0x" + "z" * 40
    
    assert validator.validate_address(valid_address) == True
    assert validator.validate_address(invalid_address) == False
    
    # Test batch validation
    data = [
        {"address": valid_address, "value": 100},
        {"address": invalid_address, "value": 50},
        {"address": valid_address, "value": -10}
    ]
    
    result = validator.validate_batch(data)
    assert result['valid_count'] == 1
    assert result['invalid_count'] == 2
    
    print("Validation test passed!")

if __name__ == "__main__":
    test_validation()