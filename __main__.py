"""

    Latency Test Utility
    
    by Segilmez06
    15 March 2025 02:19

"""



from datetime import datetime
from subprocess import getoutput as shell_cmd

from yaml import safe_load

from rich.console import Console
from rich.table import Table
from rich.progress import Progress



CONFIG_FILE = 'config.yml'
CONFIG: dict = {}

TARGET_LIST: list[tuple[str, str]] = [] # (<Name>, <Address>)

SUCCESSFUL_TARGETS: list[tuple[str, str, int]] = [] # (<Name>, <Address>, <Avg MS>)
TIMEOUT_TARGETS: list[tuple[str, str, int]] = [] # (<Name>, <Address>, <Avg MS>)
FAILED_TARGETS: list[tuple[str, str]] = [] # (<Name>, <Address>)




print('Latency Test Utility by Segilmez06')
print(f'Test started at {datetime.now().strftime("%d %B %Y %H:%M:%S")}')
print()



print('Reading config...')
with open(CONFIG_FILE, 'r', encoding='utf-8') as config_content:
    CONFIG = safe_load(config_content)
LIST_FILE = CONFIG['list_file']
PING_COUNT = int(CONFIG['ping_count'])
PING_TIMEOUT = int(CONFIG['time_limit'])



print('Reading server list...')
with open(LIST_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        line += ' '
        i = line.index(' ')
        server = line[0:i].strip()
        name = line[i:-1].strip()
        if len(server) > 1:
            TARGET_LIST.append((name, server))



with Progress() as progress:
    task = progress.add_task("Testing servers...", total=len(TARGET_LIST))
    for (NAME, SERVER) in TARGET_LIST:
        command_result = shell_cmd(f'ping -n {PING_COUNT} {SERVER}')
        if 'Average' in command_result:
            result_line = command_result.split('\n')[-1]
            avg = int(result_line.split(' = ')[-1].split('ms')[0].strip())
            if avg < PING_TIMEOUT:
                SUCCESSFUL_TARGETS.append((NAME, SERVER, avg))
            else:
                TIMEOUT_TARGETS.append((NAME, SERVER, avg))
        else:
            FAILED_TARGETS.append((NAME, SERVER))
        progress.update(task, advance=1)



print('Fetching results...')
if len(SUCCESSFUL_TARGETS) > 0:
    SUCCESSFUL_TARGETS.sort(key=lambda x: x[2])
    h_SUCCESSFUL = SUCCESSFUL_TARGETS[-1][2]
    if h_SUCCESSFUL == 0:
        k_SUCCESSFUL = float(1)
    else:
        k_SUCCESSFUL = min(float(40 / h_SUCCESSFUL), 1)

    success_table = Table(title='Test Results', show_header=True, header_style='green')
    success_table.add_column('Name', style='blue')
    success_table.add_column('Address', style='blue')
    success_table.add_column('Average', style='blue')
    success_table.add_column('Result', style='blue', width=(h_SUCCESSFUL if k_SUCCESSFUL == 1 else 40))

    for (SERVER, IP, AVG) in SUCCESSFUL_TARGETS:
        bar = int(AVG * k_SUCCESSFUL)
        success_table.add_row(SERVER, IP, f'{AVG}ms', ('#' * bar if bar > 0 else 'Instant'))
        
    print()
    Console().print(success_table)

if len(TIMEOUT_TARGETS) > 0:
    TIMEOUT_TARGETS.sort(key=lambda x: x[2])
    h_TIMEOUT = TIMEOUT_TARGETS[-1][2]
    if h_TIMEOUT == 0:
        k_TIMEOUT = float(1)
    else:
        k_TIMEOUT = min(float(40 / (h_TIMEOUT - PING_TIMEOUT)), 1)

    timeout_table = Table(title='Response after Timeout', show_header=True, header_style='yellow')
    timeout_table.add_column('Name', style='yellow')
    timeout_table.add_column('Address', style='yellow')
    timeout_table.add_column('Average', style='yellow')
    timeout_table.add_column('Result', style='yellow', width=(h_TIMEOUT if k_TIMEOUT == 1 else 40))

    for (SERVER, IP, AVG) in TIMEOUT_TARGETS:
        bar = int((AVG - PING_TIMEOUT) * k_TIMEOUT)
        timeout_table.add_row(SERVER, IP, f'{AVG}ms', '#' * bar)
        
    print()
    Console().print(timeout_table)

if len(FAILED_TARGETS) > 0:
    fail_table = Table(title='Failed', show_header=True, header_style='red')
    fail_table.add_column('Name', style='red')
    fail_table.add_column('Address', style='red')

    for (SERVER, IP) in FAILED_TARGETS:
        fail_table.add_row(SERVER, IP)
        
    print()
    Console().print(fail_table)



print()
print(f'Test finished at {datetime.now().strftime("%d %B %Y %H:%M:%S")}')
