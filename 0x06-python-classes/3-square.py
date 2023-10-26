#!/usr/bin/python3
class Square:

    def __int__(self, size):
        if not isinstance (size, int):
            raise TypeError ('size must be integer')
        if size < 0:
            raise ValueError ('size must be >= 0')
    def area(self):

        return self.__size ** 2
