import time
import sys

WAIT_BEFORE_WAKING = 5
# import os

# def get_pid_of_chrome_tabs():
#     response = os.popen('ps -C chrome')
#     progs = response.read().split('\n')
#     progs = [pr.split() for pr in progs[1:-1]]
#     return [pr[0] for pr in progs] 

# copy hosts file:
with open('/etc/hosts', 'r') as f:
    hosts_text = f.read()

# wait 5 minutes before doing anything:
time.sleep(WAIT_BEFORE_WAKING * 60)
print('opening youtube in ' + str(WAIT_BEFORE_WAKING) + ' minutes')

# make the line blocking youtube into a comment:
hosts_text_new = hosts_text.replace('127.0.0.1\twww.youtube', '# 127.0.0.1\twww.youtube')
with open('/etc/hosts', 'w') as f:
    f.write(hosts_text_new)

# # fining the pid of all open chrome programs:
# old_pids = get_pid_of_chrome_tabs()
# time.sleep(1)

# # open youtube in chrome
# os.system("google-chrome youtube.com")
# time.sleep(3)

# # get the pid of the new open tab:
# new_pids = get_pid_of_chrome_tabs()
# new_pid = [pid for pid in new_pids if not pid in old_pids]
# print(new_pid)
# new_pid = new_pid[0]

# sleep specified amount:
num_of_mins = int(sys.argv[1])
print('opening youtube for {} minutes'.format(num_of_mins))
time.sleep(num_of_mins * 60)

# return the line blocking youtube:
with open('/etc/hosts', 'w') as f:
    f.write(hosts_text)

# kill youtube tab
# os.system('kill -9 ' + new_pid)


