############################################
#USERINPUT
#If you use a different number of elements and/or different characters you need to change this in element_names in Helpfunctions
############################################

multiplication_table = [
                        ['e','a','b'],
                        ['a','e','b'],
                        ['b','b','e']]

neutral_element = 'e'


############################################
#Helpfunctions
############################################

#Convert multiplication table into table that uses 0, 1 and 2 instead of e, a and b
element_names_dict = {'e':0, 'a':1, 'b':2}
element_names_array = ['e', 'a', 'b']
number_of_elements = len(element_names_array)

def bijection_row(row):
    transformed_row = [element_names_dict[x] for x in row]
    return transformed_row

def bijection_table(table):
    transformed_table = [bijection_row(row) for row in table]
    return transformed_table

#printing
def linebreak():
    print('')

def print_adjective_truthy(truthvalue, adjective):
    if truthvalue:
        return adjective
    else:
        return 'NOT '+adjective

def print_if_true(truthvalue, word):
    if truthvalue:
        return word
    else:
        return ''


############################################
#Define algebraic operations given a multiplication table with values in 0, 1 and 2
############################################

def multiply(a,b, table):
    return table[b][a]

def print_left_multiplication(a,b,table):
    return f'{element_names_array[a]}*{element_names_array[b]} = {element_names_array[multiply(a,b,table)]}'

def print_right_multiplication(a,b,table):
    return f'{element_names_array[b]}*{element_names_array[a]} = {element_names_array[multiply(b,a,table)]}'

#(a*b)*c
def left_brackets(a,b,c, table):
    return multiply(multiply(a,b, table),c, table)

def left_brackets_string(a,b,c, table):
    return f'({element_names_array[a]}*{element_names_array[b]})*{element_names_array[c]} = {element_names_array[left_brackets(a,b,c,table)]}'

#a*(b*c)
def right_brackets(a,b,c, table):
    return multiply(a,multiply(b,c, table), table)

def right_brackets_string(a,b,c, table):
    return f'{element_names_array[a]}*({element_names_array[b]}*{element_names_array[c]}) = {element_names_array[right_brackets(a,b,c,table)]}'


############################################
#Check for associativity
############################################

def check_associativity_local(a,b,c, table):
    return left_brackets(a,b,c, table) == right_brackets(a,b,c, table)

def check_associativity_global(table):
    is_associative = True
    for i in range(number_of_elements):
        for j in range(number_of_elements):
            for k in range(number_of_elements):
                if not check_associativity_local(i,j,k, table):
                    print(f'{left_brackets_string(i,j,k,table)} but {right_brackets_string(i,j,k,table)}')
                    is_associative = False

    if is_associative:
        print('The multiplication table defines an associative operation.')
    else:
        print('The multiplication table does NOT define an associative operation.')
    return is_associative


############################################
#Check for neutral element
############################################

def check_left_neutral(e,a,table):
    return a == multiply(e,a,table)

def check_right_neutral(e,a,table):
    return a == multiply(a,e,table)

def check_neutral(e,table):
    is_neutral = True
    for i in range(number_of_elements):
        if not check_left_neutral(e,i,table):
            print(print_left_multiplication(e,i,table))
            is_neutral = False
        if not check_right_neutral(e,i,table):
            print(print_right_multiplication(e,i,table))
            is_neutral = False
    if is_neutral:
        print(f'The element {element_names_array[e]} is a neutral element.')
    else:
        print(f'The element {element_names_array[e]} is NOT a neutral element.')
    return is_neutral


############################################
#Check for inverses
############################################

def check_left_inverse(inv,a,table):
    return element_names_dict[neutral_element] == multiply(inv, a, table)

def check_right_inverse(inv,a,table):
    return element_names_dict[neutral_element] == multiply(a, inv, table)

def check_inverse_local(element, table):
    inverse_exists = False
    for i in range(number_of_elements):
        if check_left_inverse(i, element, table) and check_right_inverse(i, element, table):
            inverse_exists = True
            print(f'{print_left_multiplication(i, element, table)} and {print_right_multiplication(i, element, table)}')
            print(f'Therefore {element_names_array[i]} is an inverse of {element_names_array[element]}.')
            linebreak()

    return inverse_exists

def check_inverse_global(table):
    inverses_exist = True
    for element in range(number_of_elements):
        if not check_inverse_local(element, table):
            print(f'The element {element_names_array[element]} does NOT have an inverse.')
            inverses_exist = False

    if inverses_exist:
        print('Every element has an inverse.')
    else:
        print('NOT every element has an inverse.')
    return inverses_exist


############################################
#Check for commutativity
############################################

def check_commutatvity_local(a,b,table):
    return multiply(a,b,table) == multiply(b,a,table)

def check_commutativity_global(table):
    commutative = True
    for i in range(number_of_elements):
        for j in range(i, number_of_elements):
            if not check_commutatvity_local(i,j,table):
                commutative = False
                print(f'{print_left_multiplication(i,j, table)} but {print_right_multiplication(i,j,table)}')
    
    if commutative:
        print('The operation is commutative.')
    else:
        print('The operation is NOT commutative.')
    return commutative


############################################
#MAIN
############################################

if __name__ == "__main__":
    multiplication_table_transform = bijection_table(multiplication_table)

    print('Checking commutatvity.')
    commutativity = check_commutativity_global(multiplication_table_transform)
    linebreak()

    print('Checking associativity.')
    associativity = check_associativity_global(multiplication_table_transform)
    linebreak()

    print('Checking neutral element.')
    neutrality = check_neutral(element_names_dict[neutral_element], multiplication_table_transform)
    linebreak()

    inverses = False
    if neutrality:
        print(f'Checking for inverses with respect to the neutral element {neutral_element}.')
        inverses = check_inverse_global(multiplication_table_transform)
    else:
        print('Since there is no neutral element it does not make sense to check for inverses.')

    linebreak()
    print('Summary.')
    print(f'The multiplication table together with the element {neutral_element} is:')
    print(f'- {print_adjective_truthy(commutativity, "commutative")}')
    print(f'- {print_adjective_truthy(associativity, "assoicative")}')
    print(f'- {neutral_element} is {print_adjective_truthy(neutrality, "a neutral element")}')
    print(f'- {print_adjective_truthy(inverses, "every element has an inverse")}')
    linebreak()

    print('Therefore this defines')
    if associativity:
        if neutrality:
            if inverses:
                print(f'A {print_if_true(commutativity, "(commutative)")} group.')
            else:
                print(f'A {print_if_true(commutativity, "(commutative)")} monoid but not a group.')
        else:
            print(f'A {print_if_true(commutativity, "(commutative)")} semigroup but not a monoid, group.')
    else:
        print(f'A {print_if_true(commutativity, "(commutative)")} magma but not a semigroup, monoid, group.')
