"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(word):
    new_value = []
    for counter, i in enumerate(word):
        if counter % 3 == 2:
            new_value.append('-')
        else:
            new_value.append(i)
    final_value = ''.join(new_value)
    return final_value


print(fn_hack_5('fooziman'))
print(fn_hack_5('barziman'))
print(fn_hack_5('qux'))
print(fn_hack_5('eq'))