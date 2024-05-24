import nmap3
import time


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

	
hacker_text('Enumerate The World', 17)
