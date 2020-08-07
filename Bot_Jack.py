import turtle

########################################################################################################################
# introducing
########################################################################################################################
print("Jack: Hello. I'm Jack. What is your name?")
print('')
name = input()
print('')
print(f'Jack: Hello, {name}!')


########################################################################################################################
# for those one who likes to break
########################################################################################################################
def lst_num_things_not_valid():
    print("Jack: ...OK... So you don't want to create a shopping list, do you?")
    print('''---Tip: Please enter "yes"(If you don't want to create) or "no"(If you want to create).---''')
    print('')
    asking_to_clarify_list = input()
    print('')
    if asking_to_clarify_list == 'yes':
        want_to_do_smth_else()
        return None
    elif asking_to_clarify_list == 'no':
        print('Jack: OK! So enter a normal number of', type_of_things + '.')
        print('')
        num_of_things = int(input())
        print('')
        return num_of_things
    else:
        print("Jack: What? I don't understand. Let's start from the beginning.")
        print('')
        return None


####################################################################################################################
# dancing
####################################################################################################################
def dancing():
    print("Jack: OK, let's dance with a turtle!")
    print('---Tip: You can exit from "dancing" by clicking on the window with turtle.---')
    print('')
    ############################################################################################################
    # creating a turtle
    ############################################################################################################
    wn = turtle.Screen()

    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    dk = turtle.Turtle()

    wn.bgcolor('lightgreen')
    dk.shape('turtle')
    dk.color('red')
    dk.pensize(3)
    dk.speed(2)

    # run and get ready to jump
    dk.right(270)
    dk.speed(1)
    dk.forward(100)
    dk.speed(1.5)
    dk.right(225)
    dk.left(90)
    dk.right(45)

    # jump
    dk.penup()
    dk.right(45)
    dk.speed(1)
    dk.forward(75)
    dk.pendown()

    # rotating and going back
    dk.speed(2)
    dk.left(450)
    dk.speed(1)
    dk.forward(75)

    # creating a symbol
    dk.penup()
    dk.speed(2)
    dk.right(45)
    dk.speed(1)
    dk.forward(100)
    dk.pendown()
    dk.speed(2)
    dk.left(180)
    dk.speed(1)
    dk.forward(100)
    dk.speed(2)
    dk.right(45)
    dk.speed(1)
    dk.forward(75)

    # going up
    dk.penup()
    dk.speed(2)
    dk.left(90)
    dk.speed(1)
    dk.forward(75)
    dk.speed(2)
    dk.right(405)

    wn.exitonclick()


####################################################################################################################
# creating a shopping list
####################################################################################################################
def creating_a_shopping_list():
    shopping_list = []
    print('Jack: What type of things do you want to buy?')
    print('---Tip: You can enter something like "products" or "clothes"...---')
    print('')
    type_of_things = input()
    print('')

    print('Jack: How do you want to name your list?')
    print('')
    shopping_list_name = input()
    print('')

    print('Jack: OK! How many', type_of_things, 'do you want to buy?')
    print('---Tip: Please enter an integer.---')
    print('')
    num_of_things = int(input())
    print('')

    if num_of_things <= 0:
        want_to_create = lst_num_things_not_valid()
        if want_to_create == None:
            return None

    print('Jack: Yes, sir! Enter your ' + type_of_things + '.')
    print('---Tip: Please input hitting "enter" after each one.---')
    print('')

    for _ in range(num_of_things):
        thing = input()
        shopping_list.append(thing)

    print('')
    print('Jack: Good job! Do you want to check your list?')
    print('---Tip: Please enter "yes" or "no".---')
    print('')
    answer_for_checking_list = input()
    print('')
    ################################################################################################################
    # checking the list after creating
    ################################################################################################################
    if answer_for_checking_list == 'yes':
        print("Jack: No problem! That's your " + shopping_list_name + ' list:')
        print('')
        print(f'{shopping_list_name}:')
        index_of_item_in_shoplist = 0
        for __ in range(num_of_things):
            print(shopping_list[index_of_item_in_shoplist])
            index_of_item_in_shoplist += 1
            print('')
    else:
        print('Jack: Accepted!')
        print('')

    print('Jack: Your shopping list is ready and saved!')
    print('')


####################################################################################################################
# everything Jack don't know
####################################################################################################################
def idk():
    print('Jack: Sorry, now we need more knowledge to allow you to do this.')
    print('Jack: But it will be possible soon! Thank you for patience!')
    print('')


########################################################################################################################
# asking what to do
########################################################################################################################
def asking_what_to_do():
    print('Jack: What do you want to do?')
    print('---Tip: Now you can only "dance"(hit - 1) or  "create a shopping list"(hit - 2).---')
    print('---Soon you will be able to do much more. Thank you for patience!---')
    print('')
    action = input()
    print('')
    return action


########################################################################################################################
# if user wants to do smth else
########################################################################################################################
def want_to_do_smth_else():
    print('Jack: Do you want to do something else?')
    print('---Tip: Please enter "yes" or "no"---')
    answer_do_smth_else = input()
    answer_do_smth_else = answer_do_smth_else.lower()
    if answer_do_smth_else == 'yes':
        to_do = 'yes'
        return to_do
    else:
        to_do = 'no'
        return to_do

########################################################################################################################
# start!
########################################################################################################################
to_do = 'yes'
while to_do == 'yes':

    action = asking_what_to_do()
    if action == '1':
        dancing()
        to_do = want_to_do_smth_else()
    elif action == '2':
        creating_a_shopping_list()
        to_do = want_to_do_smth_else()
    else:
        idk()
        to_do = want_to_do_smth_else()


print('Jack: Goodbye!')
