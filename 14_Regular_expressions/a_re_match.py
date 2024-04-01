"""
Purpose: Regular Expressions
    Using re.match
        - It helps to identify patterns at the starting of string
        - By default, it is case-sensitive
"""

import re
# print(dir(re))

# ['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 
#  'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE',
  
#    '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 
#    '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 
   
# 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
 


target_string = "Python Programming is good for health"
search_string = "Python" # "python"

print(f"{target_string.find(search_string) =}")
print(f"{search_string in target_string    =}")
print()


reg_obj = re.compile(search_string)
print(reg_obj, type(reg_obj))


result = reg_obj.match(target_string)
print(f"{result =}")



if result:
    print(f"result.group():{result.group()}")
    print(f"result.span() :{result.span()}")
    print(f"result.start():{result.start()}")
    print(f"result.end()  :{result.end()}")
else:
    print("NO match found")