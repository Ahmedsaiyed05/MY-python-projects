task = []
completed = []
def add(i):
    task.append(i)

#itvoyagers.in

def delete(i):
    print("n"+i + " is deleted from the list")
    task.remove(i)

#itvoyagers.in

def view():
    n = 1
    print("nTasks in list")
    for t in task:
        print(str(n)+" : "+t)
        n = n + 1
    n = 1 
    if(completed != []):
        print("Tasks Completed")
        for t in completed:
            print(str(n)+" : "+t)
            n = n + 1
    else:
        print("No task completed yetn")

#itvoyagers.in

def done(i):
    print("n"+ i + " is donen")
    task.remove(i)
    completed.append(i)
