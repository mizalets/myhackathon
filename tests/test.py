from  mypackage import recursion, sorting
def sum_array(array):
    """
    make sure sum_array works correctly
    """

    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert recursion.sum_array([10, 1, 12]) == 23, 'incorrect'
    assert recursion.sum_array([1, 2, 3, 4, 5, 6]) == 21, 'incorrect'


def fibonacci(n):
    """
    returns nth term in fibonacci sequence
    """

    assert recursion.fibonacci(2) == 1, 'incorrect'
    assert recursion.fibonacci(5) == 5 , 'incorrect'
    assert recursion.fibonacci(10) == 55, 'incorrect'



def factorial(n):
    """
    retruns n!
    """

    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(11) ==39916800 , 'incorrect'
    assert recursion.factorial(7) == 5040, 'incorrect'



def reverse(word):
    """
    returns word in reverse
    """

    assert recursion.reverse(nakedi) == idekan, 'incorrect'
    assert recursion.reverse(evol) ==love, 'incorrect'
    assert recursion.factorial(madam) == madam, 'incorrect'
