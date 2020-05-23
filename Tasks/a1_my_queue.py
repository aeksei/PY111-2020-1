"""
My little Queue
"""
from typing import Any


deque_list = []  # очередь начало слева, конец справа


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global deque_list

    deque_list.append(elem)

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global deque_list

    return deque_list.pop(0) if deque_list else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return deque_list[ind] if ind < len(deque_list) else None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global deque_list

    deque_list.clear()

    return None
