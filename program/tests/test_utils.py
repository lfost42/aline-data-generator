'''Unit tests for utils.py methods.'''

from program.utils import random_num, get_header, random_user_id, \
    random_user_info, random_username

def test_random_num_generator_number():
    """
    GIVEN a number
    WHEN a positive integer is passed in
    THEN check that it returns a number of the correct length.
    """
    result_num = random_num(3)
    assert isinstance(result_num, int)
    assert len(str(result_num)) == 3

def test_get_header_successful():
    """
    GIVEN a user admin
    WHEN a valid username and password
    THEN check that it returns a dictionary that is not empty.
    """
    result = get_header()
    assert isinstance(result, dict)
    assert get_header()

def test_random_user_creates_data():
    """
    GIVEN an invokation
    WHEN the method runs
    THEN check that all elements return a non-empty string
    """
    user = random_user_id()
    assert all(user) is True

def test_random_user_info_creates_data():
    """
    GIVEN an invokation
    WHEN the method runs
    THEN check that all elements return a non-empty string
    """
    user = random_user_info()
    assert all(user) is True

def test_random_username_creates_string():
    """
    GIVEN a user admin
    WHEN the method is invoked
    THEN check that it returns a string.
    """
    result = random_username()
    assert isinstance(result, str)
    assert len(result) > 1