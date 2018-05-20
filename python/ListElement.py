"""
Template of ListElement class that represents
a single element in the list

Copyright 2016, University of Freiburg.
Olelsii Saukh <saukho@cs.uni-freiburg.de>
"""


class ListElement:
    '''
        Class represents elemnt of the list
    '''

    _key = None
    '''The key element of the ListElement'''

    _next = None
    '''Pointer to the left neighbor of this element'''

    _previous = None
    '''Pointer to the right neighbor of this element'''

    def __init__(self, key=0):
        '''
        Default constructor

        >>> node = ListElement()
        >>> node._key
        0
        >>> node = ListElement('key')
        >>> node._key
        'key'
        >>>
        '''
        self._key = key

    def set_next(self, next_element):
        '''
        Set pointer to next list element
        Args:
            ListElement next_element - object to point to

        >>> node1 = ListElement()
        >>> node1.get_next() is None
        True
        >>> node2 = ListElement(1)
        >>> node1.set_next(node2)
        >>> node1.get_next() is node2
        True
        >>> node2.set_next(node1)
        >>> node2.get_next() is node1
        True
        '''
        self._next = next_element

    def get_next(self):
        '''
        Get the pointer of _next object.
        Returns:
            ListElement: Get the next object

        >>> node1 = ListElement()
        >>> node1.get_next() is None
        True
        >>> node2 = ListElement(1)
        >>> node1.set_next(node2)
        >>> node1.get_next() is node2
        True
        '''
        return self._next

    def set_previous(self, prev):
        '''
        Set pointer to previous list element
        Args:
            ListElement prev: previous element

        >>> node1 = ListElement()
        >>> node1.get_previous() is None
        True
        >>> node2 = ListElement(1)
        >>> node1.set_previous(node2)
        >>> node1.get_previous() is node2
        True
        >>> node2.set_previous(node1)
        >>> node2.get_previous() is node1
        True
        '''
        self._previous = prev

    def get_previous(self):
        '''
        Get the previous list element.
        Returns:
            ListElement: previous object

        >>> node1 = ListElement()
        >>> node1.get_previous() is None
        True
        >>> node2 = ListElement(1)
        >>> node1.set_previous(node2)
        >>> node1.get_previous() is node2
        True
        >>> node2.set_previous(node1)
        >>> node2.get_previous() is node1
        True
        '''
        return self._previous
