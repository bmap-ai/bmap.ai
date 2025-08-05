"""
Master Test Suite Runner
"""

import sys
import unittest
import os

sys.path.append('..')

def run_all_tests():
    """Run complete test suite"""
    loader = unittest.TestLoader()
    
    # Load unit tests
    unit_suite = loader.discover('tests', pattern='test_*.py')
    
    # Load integration tests
    integration_suite = loader.discover('tests/integration', pattern='test_*.py')
    
    # Combine suites
    full_suite = unittest.TestSuite([unit_suite, integration_suite])
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(full_suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.1f}%")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)