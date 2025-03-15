"""

    Comma Seperated DNS List to Server List Converter
    
    by Segilmez06
    15 March 2025 15:54


    Converts from
        <Provider>,<Address 1>,<Address 2>
    comma seperated format to
        <Address 1> <Provider>
        <Address 2> <Provider>
    raw text format.
  
"""

INPUT_FILE = 'servers.csv'
OUTPUT_FILE = 'server.list'

INPUT_LINES: list[str] = []
OUTPUT_LINES: list[str] = []

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    INPUT_LINES = f.readlines()

for line in INPUT_LINES:
    (NAME, IP1, IP2) = line.split(',')
    NAME = NAME.strip()
    IP1 = IP1.strip()
    IP2 = IP2.strip()

    OUTPUT_LINES.append(f'{IP1} {NAME}')
    OUTPUT_LINES.append(f'{IP2} {NAME}')

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.writelines(OUTPUT_LINES)
