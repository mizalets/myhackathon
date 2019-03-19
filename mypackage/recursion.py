def sum_array(array):

    """Return sum of all items in array
    Args:
        array: list or array-like object containing numerical values.

    Returns:
        sum (int): all the items in the array added together
    Example:
        >>> sum_array([8, 3, 2,])
        13
    """

    """
    docstring goes here
    """
    sum_arr=0    #initialising to a variable
    for i in array:
        sum_arr += i  #increment the sum_arr by i
# return the sum of the array
    return sum_arr




def fibonacci(n):

    """Return nth term in fibonacci sequence
Args:
    n (int): any positive number

Returns:
    nth term (int): nth term in the fibonacci sequesnce
Example:
    >>>fibonacci(9)
    34
    """

    """
    docstring goes here
    """
    if n<0 :
        return("Input must be positive")  #since Fibonacci sequence is positive numbers
        # The first Fibonacci number is 0
    elif n==0:
        return 0
        # The second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def factorial(n):

    """Return n!
    Args:
        n (int): any positive number
    Returns:
    n!(int): factorial of a positive number
    Example:
    >>>factorial(4)
    24"""

    """
    docstring goes here
    """
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num



def reverse(word):

    """Return word in reverse
    Args:
        n (int): any positive number
    Returns:
    n!(int): factorial of a positive number
    Example:
    >>>reverse(nakedi)
    idekan
    """

    """
    docstring goes here
    """

    str = ""
    for i in word:
        str = i + str
    return str
