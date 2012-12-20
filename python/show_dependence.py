"""

input: task dependence . E.X:
[ {task1: [task2,task3]}, {task4:[task1]}

description:
do task2 and task3 first,
then do task1
last do task4

output:  

task2 --|
task3 --|
        |-- task 1 
              

"""


tasks = {'task4':['task1','task2','task3'],'task5':['task4'],'task1':[],'task3':['task7','task8'],'task7':['task1']}


def magic (tasks,task,history):
    print task,'->',
    assert (task not in history)
    history.append (task)
    if not tasks.get(task):
        return 
    for i in tasks.get(task):
        magic (tasks,i,history)

def test_case(tasks,task):
    magic(tasks,task,[])
    print

test_case(tasks,'task1')
test_case(tasks,'task2')
test_case(tasks,'task3')
test_case(tasks,'task4')
test_case(tasks,'task5')
