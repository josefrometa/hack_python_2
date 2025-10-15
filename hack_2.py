"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

# requerimientos: eliminar las "o", "i", "a", "u" de cada string 


def fn_hack_2(original_string):
    new_string =[]
    omited_string = "aeiouAEIOU"
    for i in original_string:
        if i not in omited_string:
            new_string.append(i)

    result = "".join(new_string)
    print(result) 
    return result 


fn_hack_2("fooziman")
fn_hack_2("barziman")
fn_hack_2("qux")

