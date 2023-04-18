#!/usr/bin/python3
"""
module square.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """construtor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """str method for the class"""
        return f"[sqare] ({self.id}) {self.x}/{self.y} - \
                {self.width}"

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        if args is not None and len(args) != 0:
            lst_args = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if lst_args[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, lst_args[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns a dict of the instance"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
