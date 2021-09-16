#! /usr/local/bin/python3

def mknorm(v):
    return r'\left\lVert{' + v + r'}\right\rVert'

b = mknorm('a');
print(b)
