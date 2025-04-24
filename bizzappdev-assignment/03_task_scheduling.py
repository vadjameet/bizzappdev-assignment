"""
Problem: Task Scheduling Optimization
Approach: Greedy algorithm - sort tasks by deadline, schedule earliest deadlines first.
"""
def max_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['deadline'])
    current_time = 0
    count = 0
    
    for task in sorted_tasks:
        if current_time + task['duration'] <= task['deadline']:
            current_time += task['duration']
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    tasks = [
        {'name': 'Task 1', 'deadline': 4, 'duration': 2},
        {'name': 'Task 2', 'deadline': 3, 'duration': 1},
        {'name': 'Task 3', 'deadline': 2, 'duration': 1},
        {'name': 'Task 4', 'deadline': 1, 'duration': 2},
    ]
    print("Maximum tasks completable:", max_tasks(tasks))