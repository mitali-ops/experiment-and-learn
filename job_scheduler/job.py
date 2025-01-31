import time
from collections import deque

class Job:
    """
    Represents a job in the scheduling system.

    Attributes:
        name (str): The job's name.
        arrival_time (int): The time when the job arrives in the system.
        burst_time (int): The time required to execute the job.
        priority (int): The job's priority (lower value means higher priority).
        resource_requirements (dict): A dictionary of resources required (CPU, memory, I/O).
        completion_time (int): The time when the job finishes execution.
        waiting_time (int): The time the job spends waiting before execution.
        turnaround_time (int): The total time from arrival to completion.
        remaining_burst_time (int): Time left for execution (for preemptive scheduling).
    """

    def __init__(self, name, arrival_time, burst_time, priority, resource_requirements):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.resource_requirements = resource_requirements
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_burst_time = burst_time  # Useful for preemptive scheduling

    def update_waiting_time(self, current_time):
        """Calculates the job's waiting time."""
        self.waiting_time = current_time - self.arrival_time - (self.burst_time - self.remaining_burst_time)

    def update_turnaround_time(self):
        """Calculates the job's turnaround time."""
        self.turnaround_time = self.completion_time - self.arrival_time

    def resource_is_available(self, available_resources):
        """
        Checks if the job's resource requirements can be met.
        
        Args:
            available_resources (dict): Dictionary of available system resources.
        
        Returns:
            bool: True if resources are available, False otherwise.
        """
        return all(self.resource_requirements[resource] <= available_resources.get(resource, 0) for resource in self.resource_requirements)

    def allocate_resources(self, available_resources):
        """Allocates the required resources to the job."""
        for resource, quantity in self.resource_requirements.items():
            available_resources[resource] -= quantity

    def release_resources(self, available_resources):
        """Releases resources back to the system after job completion."""
        for resource, quantity in self.resource_requirements.items():
            available_resources[resource] += quantity
