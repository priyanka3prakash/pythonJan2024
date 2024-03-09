import os 
import subprocess
# os.system('ls -la')

# os.system('man ls')



def execute_command(cmd):
    result = os.system(cmd)  # returns 0 if command executed successfully, else 1
    print(f"result:{result}")


execute_command("ping google.com")  # 0
execute_command("ipconfig")  # 0
execute_command("ipconfigjhg")  # 1



def execute_command(cmd):
    result = subprocess.call(cmd)  # returns 0 if command executed successfully, else 1
    print(f"result:{result}")


execute_command("ping google.com")  # 0
execute_command("ipconfig")  # 0
execute_command("ipconfigjhg")  # 1



def get_execution_result(cmd):
    p = subprocess.Popen(cmd.split(),
                        #  shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE
                          )
    output, err= p.communicate()

    output = output.decode("utf-8")
    err = err.decode("utf-8")

    print(f"\noutput:{output}")
    print(f"err   :{err}")





# get_execution_result("ping google.com")
get_execution_result("ls -la")