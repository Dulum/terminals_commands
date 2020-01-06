import time
import sys

CANCELED_MSG = "closing youtube"
WAIT_BEFORE_WAKING = 3

def rewrite_hosts(text):
    with open('/etc/hosts', 'w') as f:
        f.write(text)

# copy hosts file:
with open('/etc/hosts', 'r') as f:
    old_text = f.read()

# print('opening youtube in {} minutes'.format(WAIT_BEFORE_WAKING))

# turn the line blocking youtube to a comment:
new_text = old_text.replace('127.0.0.1\twww.youtube', '# 127.0.0.1\twww.youtube')
rewrite_hosts(new_text)

# sleep specified amount:
num_of_mins = int(sys.argv[1])
print('opening youtube for {} minutes'.format(num_of_mins))

try:
    interupted = False
    time.sleep(num_of_mins * 60)


except KeyboardInterrupt as e:
    interupted = True
    print(CANCELED_MSG)
    
    

# return the line blocking youtube:
rewrite_hosts(old_text)

if interupted: 
    exit()
