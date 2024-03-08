import sys

print(sys.argv)


"""
$ python b_command_lines_args.py 
['b_command_lines_args.py']

$ python ../02_sys_module/b_command_lines_args.py 
['../02_sys_module/b_command_lines_args.py']

$ python ../../10_Modules/02_sys_module/b_command_lines_args.py 
['../../10_Modules/02_sys_module/b_command_lines_args.py']


$ python b_command_lines_args.py 12
['b_command_lines_args.py', '12']


$ python b_command_lines_args.py 12 True
['b_command_lines_args.py', '12', 'True']

"""