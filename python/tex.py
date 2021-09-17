#! /usr/local/bin/python3

def mknorm(v):
    return r'\left\lVert{' + v + r'}\right\rVert'

def concat(*args, sep=' '):
    return sep.join(args)

b = mknorm('a');
print(b)

print(concat('hello', 'world', sep=''))
print(concat('hello', 'world', sep='_'))
print(concat('hello', 'world'))
