#!/usr/bin/python3


class Square:

    def __int__(self, size=0):

        self.size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):

        return self.__size ** 2
