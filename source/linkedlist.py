#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        i = self.head
        while i is not self.tail:
            yield i
            i = i.next

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.head is None or self.tail is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            node = self.tail
            node.next = Node(item)
            self.tail = node.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        node = Node(item)
        if self.length() == 0:
            self.tail = node
        else:
            node.next = self.head
        self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node = self.head
        while node is not None:
            if node.data == quality:
                return node.data
            node = node.next

    def replace(self, find, replace_with):
        node = self.head
        new_node = Node(replace_with)
        while node is not None:
            next_node = node.next
            # if first node is item to replace
            if node.data == find:
                # if current node is being replaced and only node in list
                if node == self.head and node == self.tail:
                    self.head = new_node
                    self.tail = self.head
                    del node
                    return
                new_node.next = next_node
                self.head = new_node
                del node
                return
            # if current node is not last and next node is item to be replaced
            if next_node is not None and next_node.data == find:
                # if next node is also tail
                if next_node == self.tail:
                    node.next = new_node
                    self.tail = node.next
                    del next_node
                    return
                node.next = new_node
                new_node.next = next_node.next
                del next_node
                return
            else:
                node = node.next

        raise ValueError('Item not found: {}'.format(find))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node = self.head

        while node is not None:
            next_node = node.next
            # if current node is item
            if node.data == item:
                # if current node is item and only one node in list
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                    del node
                    return
                self.head = node.next
                del node
                return
            # if current node is not last and next node is item
            if next_node is not None and next_node.data == item:
                # if next node is tail and item
                if next_node == self.tail:
                    self.tail = node
                    node.next = None
                    del next_node
                    return
                node.next = next_node.next
                del next_node
                return
            # if item not found continue
            else:
                node = next_node

        raise ValueError('Item not found: {}'.format(item))




def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
