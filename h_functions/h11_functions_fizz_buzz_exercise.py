"""
write a program that prints the numbers from 1 to 100
but for multiples of 3 it prints Fizz.
So it prints a string of fizz instead of the number
and for the multiples of five it prints Buzz
for the numbers which are multiples of both 5 and 3
then you're going to print out fizz buzz
For extra credit
I want you to be able to pass in an arbitrary max of value
_Function  _Looping _Conditionals _Math operators
"""
# Improved by counting the number of multiples and enumerating them

def fizz_buzz(min_num, max_num):
    three_five_mult = 0
    three_mult = 0
    five_mult = 0
    list_thr_fv = []
    list_thr = []
    list_fv = []

    for num in range(min_num, max_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            three_five_mult += 1
            list_thr_fv.append(num)
            print('fizz_buzz')
        elif num % 5 == 0:
            five_mult += 1
            list_fv.append(num)
            print('buzz')
        elif num % 3 == 0:
            three_mult += 1
            list_thr.append(num)
            print('fizz')
        else:
            print(num)

    print(f'{three_five_mult} multiples of 3 and 5 between {min_num} and {max_num} --> {list_thr_fv}')
    print(f'{three_mult} multiples of 3 between {min_num} and {max_num} -->  {list_thr}')
    print(f'{five_mult} multiples of 5 between {min_num} and {max_num} --> {list_fv}')

fizz_buzz(10, 55)


# Another solution
# print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')