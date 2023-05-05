import unittest
from my_functions import sum, get_bucket_name_from_response

class TestFunctions(unittest.TestCase):

    def test_sum(self):
        # Test the function with positive integers
        self.assertEqual(sum(2, 3), 5)
        # Test the function with negative integers
        self.assertEqual(sum(-2, -3), -5)
        # Test the function with zero
        self.assertEqual(sum(2, 0), 2)
    
    def test_get_bucket_name_from_response(self):
        # Test the function with a dictionary containing one bucket
        data = {'Buckets': [{'Name': 'my-bucket'}]}
        self.assertEqual(get_bucket_name_from_response(data), ['my-bucket'])
        # Test the function with a dictionary containing multiple buckets
        data = {'Buckets': [{'Name': 'my-bucket-1'}, {'Name': 'my-bucket-2'}, {'Name': 'my-bucket-3'}]}
        self.assertEqual(get_bucket_name_from_response(data), ['my-bucket-1', 'my-bucket-2', 'my-bucket-3'])
        # Test the function with an empty dictionary
        data = {}
        self.assertEqual(get_bucket_name_from_response(data), [])
        
if __name__ == '__main__':
    unittest.main()
