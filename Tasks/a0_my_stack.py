"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.stack.append(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if not self.stack:
            return None

        last_index = len(self.stack) - 1
        return_value = self.stack[last_index]
        del self.stack[last_index]
        # O(1) + O(1) + O(1)
        return return_value
        # self.stack.pop() # возможное решение

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """

        if ind >= len(self.stack):
            return None
        value_elem = self.stack[- 1 - ind]
        print(ind)
        return value_elem

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.stack = []
        return None
