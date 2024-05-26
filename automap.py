import subprocess
from datetime import datetime
import time
import re


"""
Global Variables
"""
info = '[*]'
success = '[+]'
error = '[!]'
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
scan_delimiter = "─" * 21


def banner():
    print('\r')

    A = [['┌', '─', '┐'], ['├', '─', '┤'], ['┴', ' ', '┴']]
    U = [['┬', ' ', '┬'], ['│', ' ', '│'], ['└', '─', '┘']]
    T = [['┬', '─', '┬'], [' ', '│', ' '], [' ', '┴', ' ']]
    O1 = [['┌', '─', '┐'], ['│', ' ', '│'], ['└', '─', '┘']]
    M = [['┐', ' ', '┌'], ['|', 'V', '|'], ['┴', ' ', '┴']]
    P = [['┌', '─', '┐'], ['├', '─', '┘'], ['┴', ' ', ' ']]

    banner = [A, U, T, O1, M, A, P]
    final = []
    init_color = 46
    txt_color = init_color
    cl = 0

    for charset in range(0, 3):
        for pos in range(0, len(banner)):
            for i in range(0, len(banner[pos][charset])):
                clr = f'\033[38;5;{txt_color}m'
                char = f'{clr}{banner[pos][charset][i]}'
                final.append(char)
                cl += 1
                txt_color = txt_color + 36 if cl <= 3 else txt_color

            cl = 0
            txt_color = init_color

        init_color += 1
        if charset < 2:
            final.append('\n   ')

    print(f"   {''.join(final)}")


def hacker_text(text, leading_spaces=0):

    text_chars = list(text)
    current, mutated = '', ''

    for i in range(len(text)):

        original = text_chars[i]
        current += original
        mutated += f'\033[1;38;5;82m{text_chars[i].upper()}\033[0m'
        print(f'\r{" " * leading_spaces}{mutated}', end='')
        time.sleep(0.05)
        print(f'\r{" " * leading_spaces}{current}', end='')
        mutated = current

    print(f'\r{" " * leading_spaces}{text}\n')


def port_scan():
    print(f"{info} {formatted_time} | PORT SCAN | {target}\n")
    command = f"sudo nmap -p- --open -sS -vvv --min-rate 5000 {target}"
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode == 0:
        # Print the output of the command
        port_scan_raw = re.compile(r'(\d+)/\w+\s+(?!on)(\w+)\s+(\w+)')
        service_matches = re.findall(port_scan_raw, result.stdout)
        print(f"{success} PORT SCAN RESULTS")
        print(scan_delimiter + '┐')
        ports = []
        for match in service_matches:
            port, state, service = match
            ports.append(port)
            print(
                f"""
PORT   STATE   SERVICE
{port}     {state}     {service}
""")
            
        print(scan_delimiter + '┘')

    else:
        print("PORT SCAN ERROR:", result.returncode)
        # Print the error output
        print(result.stderr)


banner()
hacker_text('Enumerare Mundum!', 7)
target = input("[?] INSERT TARGET ADDRESS: ")
port_scan()
