# Iterators-Generators

This repo contains scripts (my own implementations) that provide solutions to various iterators and generators challenges from the Udemy course "The Modern Python 3 Bootcamp".

__<ins>Specifics</ins>__

1) The script `custom_for_loop_with_function.py` defines a custom <em>for loop</em> where we can also pass in a function to be applied to the iterable provided.

2) In the file `custom_iterator.py` we define our own iterator, essentially our own <em>range class</em> (without a step option) that we call Counter.

3) In the `day_generator.py` file we define a function that returns a generator that yields each day of the week, starting with Monday. After Sunday the generator is exhausted and does not start over.

4) The script `binary_answer.py` provides a function which returns a generator that first yields 'yes', then 'no', then 'yes' and so on.

5) The `infinite_generator.py` python file builds an __infinite generator__ that each time yields a number from 1,2,3,4 (we start counting from 1 and increment by 1 every time).

6) With the file `beverage_song.py` we write a function that takes a count and a beverage and returns a generator that yields verses (their number is determined by the count) from a popular song about the beverage. In each verse the number of the beverages decreases by 1 until no beverages remain. The default count and beverage are 99 and 'soda' respectively.

7) In the file `multiples.py` we define a function which accepts a number and a count and returns a generator that yields the first 'count' non-negative multiples of the number. The default number and count are 1 and 10 respectively.

8) In the script `unlimited_multiples.py` we define a function that accepts a number and returns a generator that yields an unlimited number of non-negative multiples of that number. The default number is 1.

9) The script `Fibonacci_sequence.py` builds a function that accepts an integer number and returns the <em>Fibonacci sequence</em> with a number of elements equal to that number, and then a __generator function__ for the same purpose.

10) Finally the file `gen_expr_vs_list_comp_speed_test.py` provides code useful for comparing the time required for a __generator expression__ and a __list comprehension__ to produce results.
