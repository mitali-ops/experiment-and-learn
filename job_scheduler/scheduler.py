from job import Job
import time

class Scheduler:
    """
    Implements a priority-based job scheduling system with aging.

    Attributes:
        jobs (list): List of jobs in the system.
        cores (int): Number of CPU cores available.
        resources (dict): Dictionary of available system resources (CPU, memory, I/O).
    """

    def __init__(self, cores=4, resources=None):
        self.jobs = []
        self.cores = cores
        self.resources = resources if resources else {'cpu': cores, 'memory': 1024, 'io': 100}

    def add_job(self, job):
        """
        Adds a new job to the scheduler's queue.

        Args:
            job (Job): The job to be added.
        """
        self.jobs.append(job)

    def priority_scheduling_with_aging(self):
        """
        Executes jobs based on priority scheduling with aging.
        
        Aging prevents starvation by increasing the priority of long-waiting jobs.
        """
        current_time = 0
        completed_jobs = []
        while self.jobs:
            # Sort jobs by arrival time and priority
            self.jobs = sorted(self.jobs, key=lambda job: (job.arrival_time, -job.priority))

            for job in self.jobs:
                if job.resource_is_available(self.resources):
                    job.allocate_resources(self.resources)
                    print(f"Executing {job.name} with priority {job.priority}")
                    time.sleep(job.remaining_burst_time * 0.1)  # Simulate processing time
                    current_time += job.remaining_burst_time
                    job.completion_time = current_time
                    job.update_waiting_time(current_time)
                    job.update_turnaround_time()
                    completed_jobs.append(job)
                    self.jobs.remove(job)
                    job.release_resources(self.resources)
                    break

            # Apply aging: Increase priority of jobs that have been waiting too long
            for job in self.jobs:
                if job.waiting_time > 10:
                    job.priority += 1

        return completed_jobs

    def collect_statistics(self, completed_jobs):
        """
        Collects and displays job execution statistics.

        Args:
            completed_jobs (list): List of completed jobs.
        """
        total_waiting_time = total_turnaround_time = total_burst_time = 0
        for job in completed_jobs:
            total_waiting_time += job.waiting_time
            total_turnaround_time += job.turnaround_time
            total_burst_time += job.burst_time
            print(f"Job: {job.name}, Waiting Time: {job.waiting_time}, Turnaround Time: {job.turnaround_time}")

        num_jobs = len(completed_jobs)
        print(f"Average Waiting Time: {total_waiting_time / num_jobs}")
        print(f"Average Turnaround Time: {total_turnaround_time / num_jobs}")
        print(f"Average Burst Time: {total_burst_time / num_jobs}")

    def schedule_job(self, job):
        """
        Attempts to schedule a job based on available resources.

        Args:
            job (Job): The job to be scheduled.

        Returns:
            str: A message indicating whether the job was scheduled successfully.
        """
        if job.resource_is_available(self.resources):
            job.allocate_resources(self.resources)
            print(f"Executing {job.name} with priority {job.priority}")
            time.sleep(job.remaining_burst_time * 0.1)  # Simulate job execution
            return "Job scheduled successfully"
        else:
            return "Resources not available"


