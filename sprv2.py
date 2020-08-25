import random
while True :
    print("what is your choice?")
    choice  = input()
    print("my choice is ", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)

    print("Computer choice is", computer_choice)

    choice_dictionary = {'rock': 0, 'paper' : 1, 'scissors' : 2}
    choice_index = choice_dictionary.get(choice, 3)
    computer_index = choice_dictionary.get(computer_choice)

    print("computer index" , computer_index)

    matrix = [[0,2,1],
              [1,0,2],
              [2,1,0],
              [3,3,3]]

    resultindex = matrix[choice_index][computer_index]

    messageofresult = ['you win' , 'you loose' , 'it was a tie' , 'invalid command']
    print(messageofresult[resultindex])
    if input('Do You Want To Continue?press*y* to continue ') != 'y':
        break
        