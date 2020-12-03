# introduzione studente
# design logic- request list- list below is the copy of request list reverse to get value in same index

requests = []
# list = [321]
# set limit of list to 8 int
cache = []
main_program = True


# menu
def program():
    print('Hello human')
    get_value()


def option():
    global requests
    global main_program

    option = input('Please select 1 for FIFO, 2 for LFU or q for exit: ')
    if(option == '1'):
        print(fifo())  # chiamando funzione ancora non definita
    elif(option == '2'):
        print(ulf())  # chiamando funzione ancora non definita
    elif(option == 'q'):
        print('See ya')
        main_program = False


def get_value():
    global requests
    while True:
        try:
            value = int(input('please enter a value or 0 to go back to cache selection: '))
            requests.append(value)
            option()
            if (value < 0):
                raise ValueError
            elif (value == 0):
                option()
            break
        except ValueError:
            print('my processors cannot understand the input')
    return value


# creando prima funzione
def fifo():
    global requests  # accessing request
    global cache
    reqlist = []
    reqlist = requests[:: -1]

    # will print inverted list
    if(reqlist[0] in cache):
        print('hit')
        print('page ' + str(reqlist[0]) + ' already inside cache')
    else:
        cache.append(reqlist[0])
        print('miss')
        if(len(cache) <= 8):
            print('page ' + str(reqlist[0]) + ' added to the cache')
        else:
            cache.pop(0)
            print('page ' + str(reqlist[0]) + ' added and ' + str(cache[0]) + ' removed')


# creando la seconda funzione
def ulf():
    global requests  # iterating over requests
    return requests


while main_program:
    program()
