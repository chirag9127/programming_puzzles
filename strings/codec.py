"""
Design an algorithm to encode a list of strings to a string.
"""
import ast


class Codec():

    def encode(self, strs):
        return str(strs)

    def decode(self, strs):
        return ast.literal_eval(strs)


def test_codec():
    codec = Codec()
    strs = []
    assert codec.decode(codec.encode(strs)) == strs

    strs = ["This", "is", "fun"]
    assert codec.decode(codec.encode(strs)) == strs
