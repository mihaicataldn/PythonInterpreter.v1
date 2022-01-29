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


def exec_function(user_input):# we check is user input is statment or expression
    try:
        compile(user_input, '<stdin>', 'eval')
    except SyntaxError:
        return exec
    return eval


def exec_user_input(i, useer_input, user_globals):# need to be referential transparent not to violate the principle of referrential trranparenci

    user_globals = user_globals.copy()
    try:
        retval = exec_function(useer_input)(
            useer_input, user_globals
        )
    except Exception as e: #Exception if user input is not defined
        print('%s: %s' % (e.__class__.__name__, e))
    else:
        if retval is not None:
            print('Out [%d]: %s' %(i, retval))
    return user_globals


def selected_user_globals(user_globals):
    #generator expression

    return (
        (key, user_globals[key])
        for key in sorted(user_globals)
        if not key.startswith('__') or not key.endswith('__')
    )


def save_user_globals(user_globals, path='user_globals.txt'):
    with open(path, 'w') as fd:
        for key, val in selected_user_globals(user_globals):
            fd.write('%s = %s (%s)\n' % (key, val, val.__class__.__name__))

def main():

    user_globals = {} #input dict
    save_user_globals(user_globals) #save user globals defined values
    for i, user_input in get_user_input():
        user_globals = exec_user_input(i, user_input, user_globals)
        save_user_globals(user_globals)



if __name__ == '__main__':
    main()
