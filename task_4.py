new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))
print("1. task_005 перенесена в completed_tasks")

new_tasks.remove('task_007')
print("2. task_007 удалена из new_tasks")

print("3. Последняя задача в new_tasks:", new_tasks[-1])

print("Итоговые списки:")
print("new_tasks:", new_tasks)
print("completed_tasks:", completed_tasks)