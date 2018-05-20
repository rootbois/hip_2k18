"""
Template of DoublyLinkedList Data Structure

Copyright 2016, University of Freiburg.
Olelsii Saukh <saukho@cs.uni-freiburg.de>
"""


from ListElement import ListElement


class DoublyLinkedList:
    '''
    Implementation of DoublyLinked List
    '''

    head = None

    def is_empty(self):
        """
        Returns:
            True if list is empty

        >>> list = DoublyLinkedList()
        >>> list.is_empty()
        True
        >>> list.append(ListElement())
        >>> list.is_empty()
        False
        >>>
        """
        if self.head is None:
            return True
        else:
            return False

    def get_length(self):
        '''
        Returns:
            int : length of the list

        >>> list = DoublyLinkedList()
        >>> list.get_length()
        0
        >>> list.append(ListElement())
        >>> list.append(ListElement())
        >>> list.get_length()
        2
        >>>
        '''

        tmp = self.head
        i = 0
        while tmp is not None:
            i += 1
            tmp = tmp.get_next()

        return i

    def prepend(self, new_element):
        '''
        Insert a new object before the first
        element of the list
        Args:
            ListElement new_element - new element

        >>> list = DoublyLinkedList()
        >>> list.prepend(ListElement())
        >>> list.get_first()._key
        0
        >>> list.prepend(ListElement(1))
        >>> list.get_first()._key
        1
        >>> list.prepend(ListElement(2))
        >>> list.get_first()._key
        2
        >>> list.prepend(ListElement('key'))
        >>> list.get_first()._key
        'key'
        >>>
        '''

        if not self.is_empty():
            new_element.set_next(self.head)
            self.head.set_previous(new_element)
            self.head = new_element
        else:
            tmp = ListElement()
            #  had to do it this way, with tmp
            #  as the styleguide was complaining
            tmp = new_element
            self.head = tmp

    def append(self, new_element):
        '''
        Inseret a new object at the end of the list
        Args:
            ListElement new_element - new element

        >>> list = DoublyLinkedList()
        >>> list.append(ListElement())
        >>> list.get_first()._key
        0
        >>> list.append(ListElement('key'))
        >>> list.get_last()._key
        'key'
        '''
        if self.is_empty():
            self.head = new_element
        else:
            tmp = self.head
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_element)
            new_element.set_previous(tmp)

    def insert_after(self, current, new_element):
        '''
        Insert new object after certain element
        Args:
            current - element after witch to insert
            new_element - element to insert

        >>> list = DoublyLinkedList()
        >>> list.insert_after(list.get_first(), ListElement(3))
        >>> list.get_first()._key
        3
        >>> list.insert_after(list.get_first(), ListElement(4))
        >>> list.insert_after(list.get_first(), ListElement('key'))
        >>> list.insert_after(list.get_last(), ListElement(5))
        >>> list.printlist()
        3
        key
        4
        5
        >>>
        '''

        if not self.is_empty():
            tmp = self.head
            while tmp is not current:
                tmp = tmp.get_next()
            new_element.set_next(tmp.get_next())
            new_element.set_previous(tmp)
            tmp.set_next(new_element)
        else:
            self.append(new_element)

    def insert_before(self, current, new_element):
        '''
        Insert new object before certain element
        Args:
            current - element before which to insert
            new_element - new element to insert

        >>> list = DoublyLinkedList()
        >>> list.insert_before(list.get_first(), ListElement('key'))
        >>> list.insert_before(list.get_first(), ListElement(1))
        >>> list.insert_before(list.get_last(), ListElement(2))
        >>> list.insert_before(list.get_last(), ListElement(1))
        >>> list.insert_before(list.get_first().get_next(), ListElement(3))
        >>> list.printlist()
        1
        3
        2
        1
        key
        '''

        if current is self.head and self.head is not None:
            self.prepend(new_element)
        elif not self.is_empty():
            prev = None
            tmp = self.head
            while tmp is not current:
                prev = tmp
                tmp = tmp.get_next()
            new_element.set_next(tmp)
            new_element.set_previous(prev)
            tmp.set_previous(new_element)
            prev.set_next(new_element)

        else:
            self.append(new_element)

    def delete_element(self, current):
        '''
        Remove element from the list
        Args:
            current - object to delete from the list

        >>> list = DoublyLinkedList()
        >>> list.delete_element(list.get_last())
        list already empty
        >>>
        >>> list.append(ListElement())
        >>> list.append(ListElement(1))
        >>> list.append(ListElement(2))
        >>> x = list.get_first()
        >>> list.delete_element(list.get_first())
        >>> list.delete_element(x)
        Invalid input, value might be of the wrong type \
or not contained in the list
        >>> list.delete_element(list.get_first())
        >>> list.printlist()
        2
        >>>
        '''

        try:
            if not self.is_empty():
                prev = None
                tmp = self.head
                i = self.get_length()
                while tmp is not current and i >= 0:
                    prev = tmp
                    tmp = tmp.get_next()
                    i -= 1
                if i < 0:
                    raise ValueError("Specified Element not in the List")
                elif tmp.get_next() is not None and tmp != self.head:
                    nxt = tmp.get_next()
                    nxt.set_previous(prev)
                    prev.set_next(nxt)
                elif tmp == self.head:
                    self.head = tmp.get_next()
                    self.head.set_previous(None)
                else:
                    prev.set_next(None)
            else:
                print("list already empty")
        except AttributeError:
            print("Invalid input, value might be of the wrong type or not "
                  + "contained in the list")

    def get_first(self):
        '''
        Returns:
            first element of the list,
            or None, if list is empty

        >>> list = DoublyLinkedList()
        >>> list.get_first()

        >>> node = ListElement()
        >>> list.append(node)
        >>> list.get_first() is node
        True
        >>> anotherNode = ListElement(3)
        >>> list.append(anotherNode)
        >>> list.get_first() is node
        True
        >>> list.delete_element(list.head)
        >>> list.get_first() is anotherNode
        True
        >>>
        '''
        return self.head

    def get_last(self):
        '''
        Returns:
            last element of the list,
            or None, if list is empty

        >>> list = DoublyLinkedList()
        >>> list.get_last() is None
        True
        >>> node = ListElement()
        >>> list.append(node)
        >>> list.get_last() is node
        True
        >>> anotherNode = ListElement(3)
        >>> list.prepend(anotherNode)
        >>> list.get_last() is node
        True
        >>> list.delete_element(node)
        >>> list.prepend(node)
        >>> list.get_last() is anotherNode
        True
        >>>
        '''
        if not self.is_empty():
            tmp = self.head
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            return tmp
        else:
            return None

    def printlist(self):
        '''
        A method for printing out the keys of the elements
        contained in the Doubly Linked List

        >>> list = DoublyLinkedList()
        >>> list.printlist()

        >>> list.append(ListElement())
        >>> list.append(ListElement(1))
        >>> list.append(ListElement(2))
        >>> list.append(ListElement("3"))
        >>> list.printlist()
        0
        1
        2
        3
        '''
        tmp = self.head
        while tmp is not None:
            print(tmp._key)
            tmp = tmp.get_next()
