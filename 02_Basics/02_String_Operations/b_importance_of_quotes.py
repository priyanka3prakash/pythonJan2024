#!/usr/bin/python3
"""
Purpose: Importance and usage of multiple quotes
"""
language = 'Python Programming'
print(language, type(language))

question = 'How are you?'
print(question, type(question))

# where_abouts = 'whats' up! friend!!' 
# SyntaxError: unterminated string literal (detected at line 11)

where_abouts = 'whats` up! friend!!' 
print(where_abouts, type(where_abouts))

where_abouts = 'whats\' up! friend!!' 
print(where_abouts, type(where_abouts))
# NOTE 1: Placing \ before any operator with result
# in treating operator as a ordinary character

other_string = 'What\'s going in yours\' in-laws\' house'
print(other_string, type(other_string))

other_string = "What's going in yours' in-laws' house"
print(other_string, type(other_string))

# some_other_string = "What's up in yours' daugther's "wedding""
some_other_string = '''What's up in yours' daugther's "wedding"'''
print(some_other_string, type(some_other_string))

some_other_str = """ python -c 'awdwad' asdss "sfdsdfd", '''dedfdfwef sd -m jd;jd''' """
print(some_other_str)

print("\n\n")
# '\''
# "'"
# '"'
# ''' '""' '''
# """ ''' '""' '''' """
# "  ''' "


# sql_query = "select * from users where name = "udhay""
# SyntaxError: invalid syntax


sql_query = "select * from users where name = 'udhay' "
print(sql_query)

sql_query = "select * from users where name = 'udhay'; "
print(sql_query)
print()


# Multi-line Strings
print(
    'Today is an awesome day to learn python'
)

print(
    "Today is an awesome day\
    to learn python"
)

print(
    "Today is an awesome day\
to learn python"
)

print(
    '''Today is an awesome day\
    to learn python'''
)
print(
    """Today is an awesome day\
    to learn python"""
)
print()

print(
    '''Today is an awesome day
    to learn python'''
)
print(
    """Today is an awesome day
    to learn python"""
)