__author__ = 'Big'
'''A Bioinformatics Algorithms script containing scoring matrices.'''

import os


class BLOSUM62(object):
    """The BLOSUM62 scoring matrix class."""

    def __init__(self):
        """Initialize the scoring matrix."""
        #with open(os.path.join(os.path.dirname(__file__), 'BLOSUM62.txt')) as input_data:
        with open(os.path.join(os.path.dirname(__file__), 'BLOSUM62.txt')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]

    def __getitem__(self, pair):
        """Returns the score of the given pair of protein."""
        for s in self.items:
            print(s)
        i = 0

        for el in self.items[0]:
            i+=1
            if el == pair[0]:
                break

        j = 0
        for line in self.items:

            if line[0]==pair[1]:
                break
            j +=1

        return self.items[i][j]

    def init2(self,pair):
        with open(os.path.join(os.path.dirname(__file__), 'BLOSUM62.txt')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            #print(items)
        for s in items:
            print(s)
        i = 0

        for el in items[0]:
            i+=1
            if el == pair[0]:
                break

        j = 0
        for line in items:

            if line[0]==pair[1]:
                break
            j +=1

        return items[i][j]
