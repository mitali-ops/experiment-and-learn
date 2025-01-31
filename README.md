# Job Scheduler with Resource Management

This project implements a job scheduler with priority scheduling and resource management. It simulates job execution, resource allocation, and updates job statistics like waiting time and turnaround time. The scheduler handles multiple jobs with varying priority, burst time, and resource requirements (CPU, memory, and I/O).

## Features

- **Priority Scheduling**: Jobs are scheduled based on their priority and arrival time.
- **Aging**: Jobs that wait longer for execution have their priority increased to prevent starvation.
- **Resource Management**: Each job has specific resource requirements, and the scheduler checks if sufficient resources are available before scheduling.
- **Job Execution Simulation**: The scheduler simulates the execution of jobs and computes important metrics like waiting time and turnaround time.
- **Testing**: Unit tests are included to verify the functionality of the job scheduling and resource allocation mechanisms.

## File Structure

- **job.py**: Contains the `Job` class, representing a job with properties like burst time, priority, resource requirements, etc.
- **scheduler.py**: Contains the `Scheduler` class, which manages job scheduling, resource allocation, and statistics collection.
- **test_scheduler.py**: Contains unit tests to ensure the correct functionality of the job scheduling and resource allocation.

## Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

**1. Clone this repository**:

```bash
git clone https://github.com/mitali-ops/experiment-and-learn.git
cd experiment-and-learn
```

**2. Add jobs and schedule them in your main script (scheduler.py)**:

- Create jobs with various attributes like name, arrival time, burst time, priority, and resource requirements.
- Use the scheduler to add jobs and run priority scheduling with resource allocation.

**3. Run the scheduler**:

   ```bash
   python scheduler.py
  ```

**4. The program will print job execution details, along with the resource allocation and job statistics.**

**5. Run tests to ensure everything is working correctly**:

 ```bash
python test_scheduler.py
```

## Contributing

Feel free to fork this project, open issues, and create pull requests. Contributions are welcome!
