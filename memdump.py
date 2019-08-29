#! /usr/bin/env python
import ctypes
import re
import sys

def maps_line_range(line):
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    return [int(m.group(1), 16), int(m.group(2), 16), m.group(3)]

def cat_proc_mem(pid):
    maps_file = open("/proc/" + pid + "/maps", 'r')
    ranges = map(maps_line_range, maps_file.readlines())
    maps_file.close()
    mem_file = open("/proc/" + pid + "/mem", 'r', 0)
    for r in ranges:
        if r[2] == 'r':
            mem_file.seek(r[0])
            chunk = mem_file.read(r[1] - r[0])
            print(chunk)
    mem_file.close()

if __name__ == "__main__":
    for pid in sys.argv[1:]:
        cat_proc_mem(pid)