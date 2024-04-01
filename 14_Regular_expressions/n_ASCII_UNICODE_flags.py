"""
Purpose: ASCII, UNICODE, LOCALE flags
"""

import re

print(re.findall(r"\w+", "fox:αλεπού"))
print(re.findall(r"\w+", "fox:αλεπού", flags=re.A))  # ASCII only
print(re.findall(r"[a-zA-Z0-9_]+", "fox:αλεπού"))
print(re.search(r"[a-zA-Z]", "İıſK"))  # False
print(re.search(r"[a-z]+", "İıſK", flags=re.I)[0])
print(re.search(r"[a-z]", "İıſK", flags=re.I | re.A))  # False
print()


print([hex(ord(c)) for c in "fox"])
print([c.encode("unicode_escape") for c in "αλεπού"])
print([c.encode("unicode_escape") for c in "İıſK"])
print(re.findall(r"[\u0061-\u007a]+", "fox:αλεπού,eagle:αετός"))
print()
