# match - match the exact sequence

import re

# 0/p match object - matched sequence and span () - start and end index
text = "hello world"
result = re.match("hello" , text)
print(result)

# using pattern

test_str = "12abcd3566abc7788habckhk"
pattern = re.compile("abc")
matches = pattern.finditer(test_str)

for match in matches:
    print(match)


# searchoperation searches the entire string

text = "python of powerfull"
result = re.search("powerfull" , text)
print(result)

my_string = 'abc123ABC123abc'
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

    #group() - Return the string matched by the re
    #atart() - REturn the starting  position of the match
    #end() - ending position of match
    #span() - tuple containg start and end

    test_string = '123abc456789abc123ABC'
    pattern = re.compile( r'abc')
    matches = pattern.finditer(test_string)

    for match in matches:
        print(match)
        print(match.span(), match.start(), match.end())
        print(match.group())