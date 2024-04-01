import os
import re 

LOG_FILES_PATH = '../12_Logging/a_builtin_logging/logs'
os.chdir(LOG_FILES_PATH)
# print(os.getcwd())
# print(os.listdir())


# Method 1 - traditional
with open('07_logging.log', 'r') as fh:
    file_content = fh.readlines()

error_logs = []
for each_line in file_content:
    if 'ERROR' in each_line:
        error_logs.append(each_line)

print(error_logs)
print()

# Method 2 - using re
with open('07_logging.log', 'r') as fh:
    file_content = fh.read()
    
error_logs = re.findall('.*ERROR.*', file_content)
print(error_logs)
print()

print('\n error_log_times')
error_log_times = re.findall('.*ERROR', file_content)
print(error_logs)
