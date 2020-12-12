# c2py
Running C functions in Python

## Steps

- Convert `hello.c` to shared library

    `gcc -shared -o hello.so -fpic hello.c`

- Run
    `python3 c2py.py ./hello.so`
