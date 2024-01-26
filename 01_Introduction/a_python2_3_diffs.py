# print "Hello world"    # works on in python 2
print("Hello world")

print(1+ 0)
print(1 * 0)

# try:
#   print(1 / 0)
# except Exception, ex:     # works only in python 2
#   print("Got Exception", ex)
  
  
try:
  print(1 / 0)
except Exception as ex:
  print("Got Exception", ex)