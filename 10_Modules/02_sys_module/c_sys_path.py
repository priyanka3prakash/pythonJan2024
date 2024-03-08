import sys 


# print(sys.path)

for each_path in sys.path:
    print(each_path)
print()

# /workspaces/pythonJan2024/10_Modules/02_sys_module
# /usr/local/python/3.10.13/lib/python310.zip
# /usr/local/python/3.10.13/lib/python3.10
# /usr/local/python/3.10.13/lib/python3.10/lib-dynload
# /workspaces/pythonJan2024/.venv/lib/python3.10/site-packages
    

# NOTE: Installed modules are stored in "site-packages"


# def add(n1, n2):
#     return n1 + n2


# def sub(n1, n2):
#     return n1 - n2


sys.dont_write_bytecode = False

# absolute import 
import calculator


print(f"{calculator.add(1, 2) =}")
print(f"{calculator.sub(1, 2) =}")


# absolute import 
import calculator as cl


print(f"{cl.add(1, 2) =}")
print(f"{cl.sub(1, 2) =}")




# selective import
from  calculator import add, sub

print(f"{add(1, 2) =}")
print(f"{sub(1, 2) =}")


sys.path.append("/workspaces/pythonJan2024/02_Basics/01_Arithmetic_Operations/")

import b_ration_store


print(b_ration_store)


# NOTE: use the condition if __name__ == '__main__' to avoid executing all imported code
