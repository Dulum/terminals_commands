import time
import sys


# copy hosts file:
with open('/etc/hosts', 'r') as f:
    hosts_text = f.read()

# make the line blocking youtube into a comment:
hosts_text_new = hosts_text.replace('127.0.0.1\twww.youtube', '# 127.0.0.1\twww.youtube')
with open('/etc/hosts', 'w') as f:
    f.write(hosts_text_new)

# sleep specified amount:
num_of_mins = int(sys.argv[1])
print('opening youtube for {} minutes'.format(num_of_mins))
time.sleep(num_of_mins * 60)

# return the line blocking youtube:
with open('/etc/hosts', 'w') as f:
    f.write(hosts_text)
