#!/usr/bin/python3

class Square:

    def __int__(self, size):

        if not isinstance(size, int):
            raise TypeError('size must be an integar')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
