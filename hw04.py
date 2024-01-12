def donut_costs(num_donuts, member):
    '''
    Purpose:
        Find the total cost of a donut order
    Parameters:
        num_donuts: the number of donuts being ordered
        member: determine if customer is a member or not, which will apply a discount if they are
    Return Value:
        Total cost of donuts
    '''
    if num_donuts == 1:
        cost = 90
    elif num_donuts >= 10:
        cost = 70
    else:
        cost = 80
    if member == True:
        cost = int(cost) - 5
    else:
        cost = cost
    total = int(num_donuts) * cost
    return total

if __name__ == '__main__':
    print(donut_costs(6, True)) # Should output 450
    print(donut_costs(10, False)) # Should output 700
    print(donut_costs(10, True)) # Should output 650
    print(donut_costs(2, True)) # Should output 150
    print(donut_costs(2, False)) # Should output 160
    print(donut_costs(1, False)) # Should output 90
    print(donut_costs(1, True)) # Should output 85
    print(donut_costs(15, False)) # Should output 1050
    print(donut_costs(17, True)) # Should output 1105
    print(donut_costs(7, False)) # Should output 560
    print(donut_costs(9, False)) # Should output 720
    print(donut_costs(9, True)) # Should output 675

def choose_three(text, optionA, optionB, optionC):
    '''
    Purpose:
        A function that has three options to choose from
    Parameters:
        text: the task/qustion imposed to the user
        optionA: option A, something the user can input to choose
        optionB: option B, something the user can input to choose
        optionC: option C, something the user can input to choose
    Return Value:
        The selected option the user inputed
    '''
    state = 0

    print(text)
    print()
    print(optionA)
    print(optionB)
    print(optionC)

    while state != 3:
        if state == 0:
            choice = input('Choose A, B, or C: ')
            if choice in ['A', 'B', 'C',]:
                return choice
            else:
                print('Invalid option, try again.')

def adventure():
    '''
    Purpose:
        Create an exciting and fun adventure story depicting a summer day
    Parameters:
        None
    Return Value:
        The outcome of the story, either True or False depending on the decisions made
    '''
    state = 0
    while state != 12:
        start = choose_three('It is a warm summer day, you just woke up and need something to do.', 'A. You decide to call your friends and see what their up to', 'B. It is too early so you roll over and go back to sleep', 'C. Its time to start your morning routine')
        if start in ['A']:
            decision1 = choose_three('Your friends pick up, what should the plan be?', 'A. Lake day', 'B. Golfing', 'C. Lets hangout at someones house')
            if decision1 in ['A', 'B']:
                print('You all enjoy an amazing day outside and end it with a bonfire.')
                return True
            else:
                decision3 = choose_three('Well you have to find a house to hangout at and its never a guys house so you call up the girls and see if their free and they are!', 'A. Ask them to meet up later and everyone brings food and drinks', 'B. Mention something one of the guys said', 'C. Poke fun at the girls')
                if decision3 in ['A']:
                    print('Everyone gets together to enjoy the day and spend the night partying')
                    return True
                else:
                    print('You struck a nerve and now the girls arent talking to you and the vibe is ruined')
                    return False
        elif start in ['C']:
            decision2 = choose_three('After making an amazing breakfast, showering, and making your bed you decide to run over to your friends house and see what their up to. You ring the doorbell and ask them what their up to','A. You strike up conversation and accidentilly mention their ex', 'B. An idea to get everyone together for the day pops into your head and the two of you start calling everyone up ', 'C. They say their headed to the river to do some fishing, so you ask to tag along' )
            if decision2 in ['A']:
                print('Wrong move, you piss them off and they slam the door in your face')
                return False
            elif decision2 in ['C']:
                print('They say of coure you can come, so the two of you spend the day out fishing and manage to catch enough to bring home and cook up')
                return True
            else:
                decision3 = choose_three('Well you have to find a house to hangout at and its never a guys house so you call up the girls and see if their free and they are!', 'A. Ask them to meet up later and everyone brings food and drinks', 'B. Mention something one of the guys said', 'C. Poke fun at the girls')
                if decision3 in ['A']:
                    print('Everyone gets together to enjoy the day and spend the night partying')
                    return True
                else:
                    print('You struck a nerve and now the girls arent talking to you and the vibe is ruined')
                    return False
        else:
            print('You end up waking up later in the afternoon, with a splitting headache and all of your friends are off doing other things')
            return False