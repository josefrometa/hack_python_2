"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(word):
# this part replaces charactes for the new ones we need 
    original_characters = "aeiou"
    new_characters = "@3¡0v"
    my_string = str.maketrans(original_characters, new_characters)
    replaced_characters = word.translate(my_string)
# here concatenates the splited string to upper the last part and the fist part of this string 
    if len(replaced_characters) <= 2 and replaced_characters[1] == 'v':
        first = replaced_characters[0].upper()
        last = replaced_characters[1]
        result = first + last.lower() 
        return result
    else:
        first = replaced_characters[0].upper()
        middle = replaced_characters[1:-1]
        last = replaced_characters[-1].upper()
        result = first + middle + last
        return result


fn_hack_3('fooziman')
print(fn_hack_3('fooziman'))
print(fn_hack_3('3Q'))
print(fn_hack_3('qux'))
print(fn_hack_3('qu'))