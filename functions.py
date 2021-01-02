def greet_user():
    """Generic greeting for users"""
    print('Hello!')

    print('Welcome!')

def greet_user_by_name(name = 'user', greeting = 'Hello'):
    """Customized greeting"""
    print(greeting + ', ' + name)

greet_user()

greet_user_by_name(input('What is your name?' ), 'Welcome')
