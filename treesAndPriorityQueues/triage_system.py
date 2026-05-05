# triage_system.py
# This file contains the TriageSystem class

import heapq


class TriageSystem:
    # Class-level counter to track arrival order
    arrival_counter = 0

    def __init__(self):
        # Private queue that will store patients
        self.__queue = []

    @staticmethod
    def next_arrival_order():
        # Gets the current arrival number, then increases it
        current_order = TriageSystem.arrival_counter
        TriageSystem.arrival_counter += 1
        return current_order

    def add_patient(self, name, severity):
        # Checks that the name is not empty
        if name == "":
            raise ValueError("Patient name cannot be empty.")

        # Checks that severity is between 1 and 5
        if severity < 1 or severity > 5:
            raise ValueError("Severity must be between 1 and 5.")

        arrival_order = TriageSystem.next_arrival_order()

        # heapq is a min-heap, so severity is made negative
        patient = (-severity, arrival_order, name, severity)

        heapq.heappush(self.__queue, patient)

    def process_next(self):
        # If the queue is empty, return None
        if self.is_empty():
            return None

        # Remove the highest priority patient
        patient = heapq.heappop(self.__queue)

        name = patient[2]
        severity = patient[3]

        return name, severity

    def peek_next(self):
        # If the queue is empty, return None
        if self.is_empty():
            return None

        # Look at the highest priority patient without removing it
        patient = self.__queue[0]

        name = patient[2]
        severity = patient[3]

        return name, severity

    def is_empty(self):
        # Returns True if there are no patients
        return len(self.__queue) == 0

    def size(self):
        # Returns how many patients are in the queue
        return len(self.__queue)

    def clear(self):
        # Removes all patients from the queue
        self.__queue = []