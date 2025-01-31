from job import Job
from scheduler import Scheduler
import unittest

class TestJobScheduling(unittest.TestCase):
    """
    Unit tests for the Scheduler class and job scheduling functionality.
    """

    def setUp(self):
        """Sets up a scheduler and a sample job before each test."""
        self.scheduler = Scheduler(cores=4, resources={'cpu': 4, 'memory': 1024, 'io': 100})
        self.job1 = Job(name="Job1", arrival_time=0, burst_time=4, priority=2, resource_requirements={'cpu': 1, 'memory': 100, 'io': 10})
        self.scheduler.add_job(self.job1)

    def test_schedule_job(self):
        """Tests if a job is successfully scheduled when resources are available."""
        result = self.scheduler.schedule_job(self.job1)
        self.assertEqual(result, "Job scheduled successfully")

    def test_schedule_job_with_insufficient_resources(self):
        """Tests if a job is correctly rejected when resources are insufficient."""
        job2 = Job(name="Job2", arrival_time=1, burst_time=3, priority=1, resource_requirements={'cpu': 5, 'memory': 500, 'io': 50})
        result = self.scheduler.schedule_job(job2)
        self.assertEqual(result, "Resources not available")

# Run tests in a Jupyter/Colab-friendly way
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
