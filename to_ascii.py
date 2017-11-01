"""
Write a module Converter that can take ASCII text and convert it to hexadecimal.
The class should also be able to take hexadecimal and convert it to ASCII text."""

import binascii

class Converter():
    @staticmethod
    def to_ascii(h):
        return binascii.a2b_hex(h)
    @staticmethod
    def to_hex(s):
        return binascii.b2a_hex(s)









# to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473") # == > "Look mom, no hands"

# to_hex("Look mom, no hands") # ==> "4c6f6f6b206d6f6d2c206e6f2068616e6473"