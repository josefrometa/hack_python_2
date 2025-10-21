"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(word):
    # result = []
    for i in word:
        if len(word) >= 5 :
            result = word[1:-1]
        else:
            result = word
    print(result)
    return result


fn_hack_4('fooziman')
fn_hack_4('barziman')
fn_hack_4('qux')