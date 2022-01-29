import itertools

print('Mihai interpreter')
def get_user_input():
    for i in itertools.count():

        try:
            yield  i, input('In [%d]: '% i)
        except KeyboardInterrupt:
            pass
        except EOFError:
            break

def exec_user_input(i, useer_input, user_globals):

    exec(useer_input, user_globals)

def main():

    user_globals = {} #input dict
    for i, user_input in get_user_input():
        exec_user_input(i, user_input, user_globals)



if __name__ == '__main__':
    main()
