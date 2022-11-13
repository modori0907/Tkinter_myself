import re

lists = ['/Users/suzukiatsushiiki/Desktop/python/Tkinter_myself/01_cpu.txt', '/Users/suzukiatsushiiki/Desktop/python/Tkinter_myself/01_mem.txt', '/Users/suzukiatsushiiki/Desktop/python/Tkinter_myself/main.py']
cpu_match_lists = []
mem_match_lists = []


for x in lists:
    if re.search(r"cpu.txt$", x):
        cpu_match_lists.append(x)
    elif re.search(r"mem.txt$", x):
        mem_match_lists.append(x)

print((len(cpu_match_lists) + len(mem_match_lists)) % 2)


if (len(cpu_match_lists) + len(mem_match_lists)) % 2 == 0:
    print("good")
else:
    print("not enough ")



