# Author: Paldin Bet Eivaz
# Description: Program which implements a minimum heap data structure.


# Import DynamicArray and LinkedList classes
from helper_structs import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds the specified node to the min heap.
        """

        # add node to end of heap
        self.heap.append(node)
        cur_idx = self.heap.length() - 1

        # percolate node up the heap to maintain min heap property
        while cur_idx > 0:
            prev_idx = cur_idx
            cur_idx = ((cur_idx - 1) // 2)
            parent_node = self.heap.get_at_index(cur_idx)
            if parent_node > node:
                self.heap.swap(prev_idx, cur_idx)
            else:
                break

    def get_min(self) -> object:
        """
        Returns node with minimum key without removing it from the heap.
        """

        # check if heap is empty
        if self.is_empty():
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns node with minimum key and removes it from the heap.
        """

        # check if heap is empty
        if self.is_empty():
            raise MinHeapException

        # save min node and remove last node from heap
        min_node = self.get_min()
        repl_node = self.heap.pop()

        if not self.is_empty():
            # replace first node in heap with last node
            self.heap.set_at_index(0, repl_node)
            len_heap = self.heap.length()

            # current indices of replacement node and its children
            cur_idx = 0
            left_idx, right_idx = 1, 2

            # check if replacement node has no children
            if left_idx >= len_heap and right_idx >= len_heap:
                return min_node

            # if replacement node has two children, find the minimum
            if left_idx < len_heap and right_idx < len_heap:
                min_child = min(self.heap.get_at_index(left_idx), self.heap.get_at_index(right_idx))
            # if replacement node has 1 child, set as minimum
            else:
                min_child = self.heap.get_at_index(left_idx)

            # percolate replacement node down the heap to maintain min heap property
            while repl_node > min_child:
                # if replacement node has two children, find the minimum
                if left_idx < len_heap and right_idx < len_heap:
                    min_child = min(self.heap.get_at_index(left_idx), self.heap.get_at_index(right_idx))
                    # swap replacement node with minimum child if its key is greater
                    if repl_node > min_child:
                        if min_child == self.heap.get_at_index(left_idx):
                            self.heap.swap(cur_idx, left_idx)
                            cur_idx = left_idx
                        else:
                            self.heap.swap(cur_idx, right_idx)
                            cur_idx = right_idx
                # if replacement node has 1 child, set as minimum
                else:
                    min_child = self.heap.get_at_index(left_idx)
                    # swap replacement node with left child if its key is greater
                    if repl_node > min_child:
                        self.heap.swap(cur_idx, left_idx)
                        cur_idx = left_idx

                # if replacement node swapped, calculate indices of its new children
                left_idx, right_idx = ((2 * cur_idx) + 1), ((2 * cur_idx) + 2)

                # stop if replacement node has no children
                if left_idx >= len_heap and right_idx >= len_heap:
                    return min_node

        return min_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order and builds a proper MinHeap from them.
        """

        # clear current contents of heap
        self.heap = DynamicArray()

        # copy contents of DynamicArray to heap
        for i in range(da.length()):
            self.heap.append(da.get_at_index(i))

        len_heap = self.heap.length()
        cur_idx = (len_heap // 2) - 1  # index of first non-leaf node in heap

        while cur_idx >= 0:
            # get current node and the indices of its children
            cur_node = self.heap.get_at_index(cur_idx)
            left_idx, right_idx = ((2 * cur_idx) + 1), ((2 * cur_idx) + 2)

            # if current node has two children, find the minimum
            if left_idx < len_heap and right_idx < len_heap:
                min_child = min(self.heap.get_at_index(left_idx), self.heap.get_at_index(right_idx))
            # if current node has 1 child, set as minimum
            else:
                min_child = self.heap.get_at_index(left_idx)

            # save index of current node
            temp_idx = cur_idx

            # percolate current node down the heap to maintain min heap property
            while cur_node > min_child:
                # if current node has two children, find the minimum
                if left_idx < len_heap and right_idx < len_heap:
                    min_child = min(self.heap.get_at_index(left_idx), self.heap.get_at_index(right_idx))
                    # swap current node with minimum child if its key is greater
                    if cur_node > min_child:
                        if min_child == self.heap.get_at_index(left_idx):
                            self.heap.swap(temp_idx, left_idx)
                            temp_idx = left_idx
                        else:
                            self.heap.swap(temp_idx, right_idx)
                            temp_idx = right_idx
                # if current node has 1 child, set as minimum
                else:
                    min_child = self.heap.get_at_index(left_idx)
                    # swap current node with left child if its key is greater
                    if cur_node > min_child:
                        self.heap.swap(temp_idx, left_idx)
                        temp_idx = left_idx

                # if current node swapped, calculate indices of its new children
                left_idx, right_idx = ((2 * temp_idx) + 1), ((2 * temp_idx) + 2)

                # stop if current node has no children
                if left_idx >= len_heap and right_idx >= len_heap:
                    break

            # get next node and repeat
            cur_idx -= 1


# BASIC TESTING
if __name__ == '__main__':
    pass

    # print("\nadd example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)

    # print("\nadd example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    # print("\nget_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    # print("\nremove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())

    # print("\nbuild_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
