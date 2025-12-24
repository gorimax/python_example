print('1: hello world')

def greet():
    print('2: こんにちは')

greet()

def print_name(name):
    print(f'3: 私の名前は{name}です')

print_name('GORI')

def get_greet():
    return 'おはようございます'

greet = get_greet()
print(f'4: {greet}')

def add(a ,b):
    return a + b

sum = add(1, 2)
print(f'5: {sum}')
