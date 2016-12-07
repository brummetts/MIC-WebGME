from subprocess import *;
import sys;

def getTasks():
    task=(check_output("tasklist", shell=True));
    task=task.decode();
    task=task.split('\n');
    l=[]
    for t in task:
        newlist=t.split();
        l.append(newlist);
    l.reverse();
    l.pop();
    l.pop();
    l.pop();
    l.reverse();
    l.pop()
    return(l);

def terminateTask(name):
        task=getTasks();
        for t in task:
                if name == t[0]:
                        command="Taskkill /PID "+t[1]+" /F";
                        call(command, shell=True);
        return 'True'
    
terminateTask(sys.argv[1]);

