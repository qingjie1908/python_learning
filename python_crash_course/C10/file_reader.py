from pathlib import Path

# path = Path('pi_digits.txt')
path = Path('/Users/qingjie/github/python_learning/python_crash_course/C10/pi_digits.txt')
contents = path.read_text()
print(contents)
"""
3.1415926535
  8979323846
  2643383279
"""
lines = contents.splitlines()

pi = ''
for line in lines:
    pi += line
    print(line)
# 3.1415926535
#   8979323846
#   2643383279

print(pi)
print(len(pi))
# 3.1415926535  8979323846  2643383279
# 36

pi = ''
for line in lines:
    pi += line.lstrip()
print(pi)
print(len(pi))
# 3.141592653589793238462643383279
# 32

str1 = '0101199508290202'
birthday = input('Enter your bittyday: ')
if birthday in str1:
    print("Birthday is in str1.")
else:
    print("Birthday not in str1.")