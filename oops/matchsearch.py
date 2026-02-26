import re

text = "python"
print(re.search("python", text , re.I))
text = "Hello\nWorld"
print(re.search("Hello.*World", text , re.S))

pattern = re.compile(r""" 7879hbgjklksdgdskl..""", re.X)
print(pattern)

print(re.findall(r"\w+" , text , re.A))
pattern = re.compile(r"""7879hbgjklksdgdskl..%^^&*689""" , re.DEBUG)
print (pattern)


# assertions - validating the output or checking certain conditions

"""
^ - start of string
\b -- end of string
\B - Not word boundary
"""

text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d) ", text))

text = "user1 admin test2"
print(re.findall(r"\w+(?!\d)" , text))

text ="price $500"
print(re.findall(r"(?<=$)\d+") , text)

text = "500 $300"
print(re.findall(r"(?<!$)\d+") , text)



