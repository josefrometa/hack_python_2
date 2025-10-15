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
    new_string = []
    original_characters = "aeiou"
    replaced_characters = "@3¡0v"
    for i in word:
        if i in word:
            
            
    
    return result
