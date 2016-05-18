def greeting(func):
    def wrapper(user):
        print('Hello {}'.format(user))
        func(user + '5555')
        
    return wrapper
