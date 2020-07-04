#Python Regex examples 
import re
pattern = '^a...s$'
test_string = 'abbbs'
result = re.match(pattern, test_string)
if result:
    print(result)
    print("Search successful")
else:
    print(result)
    print("Search not successful")