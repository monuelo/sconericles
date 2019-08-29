import sys, os, string, re

pid = sys.argv[1]
maps_file = open("/proc/%s/maps" % pid, 'r')
mem_file = open("/proc/%s/mem" % pid, 'r')
r=0

for line in maps_file.readlines():  # for each mapped region
    w=line.rsplit(None, 1)[-1] # last word
    if w != "/dev/isgx" and  w != "[vvar]" and w != "[vdso]" and w != "[vsyscall]":
        m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
        r += 1
        p = 0
        if m.group(3) == 'r':  # if this is a readable region
            start = int(m.group(1), 16)
            end = int(m.group(2), 16)
            while start < end:
                try:
                    mem_file.seek(start)  # seek to region start
                    chunk = mem_file.read(4096)  # read region contents
                    sys.stdout.write(chunk)
                    p += 1
                    if p > 1000:
                        sys.stderr.write("region = %02d, index=%x    \r" % (r,start))
                        p = 0
                    start += 4096
                except:
                    pass
sys.stderr.write("\n")
