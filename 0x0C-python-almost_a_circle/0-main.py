#!/usr/bin/python3
""" 0-main """

from models.base import Base

if __name__ == "__main__":
    
    b1 = Base()

    b2 = Base(12)

    b3 = Base('93re')

    print(f"b1 id: {b1.id}\nb2 id: {b2.id}\nb3 id: {b3.id}")
