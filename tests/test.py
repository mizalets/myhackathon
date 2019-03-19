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
    assert recursion.reverse(madam) == madam, 'incorrect'



def bubble_sort(items):
    assert sorting.bubble_sort([50,30,40,10,20]) == [10,20,30,40,50], 'incorrect'
    assert sorting.bubble_sort([9,8,7]) == [7,8,9], 'incorrect'
    assert sorting.bubble_sort([10,4,2,0]) == [0,2,4,10], 'incorrect'




def merge_sort(items):
    assert sorting.merge_sort([77,31,45,55,10]) == [10, 31,45,55, 77, 93], 'incorrect'
    assert sorting.merge_sort([3, 1, 2]) == [1,2,3], 'incorrect'
    assert sorting.merge_sort([5,12,78,1,2,6]) == [1,2,5,6,12,78], 'incorrect'




def quick_sort(items):
    assert sorting.quick_sort([77,31,44,55,20]) == [31, 44, 54, 55, 77], 'incorrect'
    assert sorting.quick_sort([31, 21, 23]) == [21,23,31], 'incorrect'
    assert sorting.quick_sort([5,12,78,1]) == [1,5,12,78], 'incorrect'
