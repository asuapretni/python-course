# nums = list(range(1, 100))

# while len(nums) > 0:  # sentinel value
#     print(nums.pop())  # we take the last num out of the list (pop) then the lenght is -1 each tine till it ends up being 0

def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '30':
            print('You WIN!!')
            return False
        else:
            print(f'No, {guess} is not, you lose!!')


guessing_game()

# lesson exercise
def loop_using_while():
    dog_house = ['Peter', 'Ace', 'pinky', 'Ray']
    counter = 0
    while counter < len(dog_house):
        print(dog_house[counter])
        counter += 1

    return [dog_house, counter]

loop_using_while()