"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # todo для очереди можно использовать python list

        # Начало очереди - слева  - dequeue
        # Конец очереди - справа - enqueue

        # append, pop(-1) -> O(1)
        # insert, del, pop(0) -> 0(n)

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.queue.append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.queue:
            return None
        value_for_ret = self.queue[0]
        del self.queue[0]
        return value_for_ret


    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        if ind >= len(self.queue):
            return None
        peek_value = self.queue[ind]
        return peek_value

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """

        self.queue = []
        return None
