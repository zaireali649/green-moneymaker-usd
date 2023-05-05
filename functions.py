import random
import datetime
from dateutil.tz import tzutc
from typing import List

def sum(a: int, b: int) -> int:
    """
    Function to add two integers and return the sum.
    
    Args:
    a: An integer to be added.
    b: An integer to be added.
    
    Returns:
    The sum of a and b as an integer.
    """
    return a + b

def get_bucket_name_from_response(data: dict) -> List[str]:
    """
    Function to extract the name of buckets from a dictionary and return a list of strings.
    
    Args:
    data: A dictionary containing information about AWS S3 buckets.
    
    Returns:
    A list of strings containing the names of the buckets in the given dictionary.
    """
    names = []
    buckets = data['Buckets']
    for bucket in buckets:
        names.append(bucket['Name'])
        
    return names
    
if __name__ == '__main__':
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = sum(a, b)  # Add two random integers
    print(a, b, c)  # Print the random integers and their sum
