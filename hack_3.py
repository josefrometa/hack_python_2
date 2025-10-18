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
    original_characters = "aeiou"
    new_characters = "@3¡0v"
    my_string = str.maketrans(original_characters, new_characters)
    replaced_characters = word.translate(my_string)
    # this part of the code is incompleted, needs to be updated
    # if len(replaced_characters) < 2:
    #     short_result = []
    #     for i in replaced_characters:
    #         if i in new_characters:
    #             short_result.append(i)
    #         else:
    #             short_result.append(i.upper())
    #     return "".join(short_result)

    first = replaced_characters[0].upper()
    middle = replaced_characters[1:-1]
    last = replaced_characters[-1].upper()
    result = first + middle + last
    return result


fn_hack_3('fooziman')
print(fn_hack_3('fooziman'))
print(fn_hack_3('3Q'))
print(fn_hack_3('qux'))
print(fn_hack_3('qv'))