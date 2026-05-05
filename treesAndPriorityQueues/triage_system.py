# triage_system.py
# This file contains the TriageSystem class


class TriageSystem:
    def __init__(self):
        # Private queue that will store patients
        self.__queue = []

    def is_empty(self):
        # Returns True if there are no patients
        return len(self.__queue) == 0

    def size(self):
        # Returns how many patients are in the queue
        return len(self.__queue)

    def clear(self):
        # Removes all patients from the queue
        self.__queue = []