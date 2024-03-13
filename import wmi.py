import psutil
import getpass

system_username = getpass.getuser()

def print_process_tree(process, indent=''):
    print(f'{indent}|- {process.name()} [PID: {process.pid}]')

    children = process.children()
    for child in children:
        print_process_tree(child, indent + '   ')

# Get the list of running processes
processes = list(psutil.process_iter())

# Sort the processes alphabetically by name
processes.sort(key=lambda p: p.name().lower())

# Print the process tree for processes not running under "SYSTEM"
for process in processes:
    if process.username() != 'admin':
        print_process_tree(process)