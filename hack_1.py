"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(word):
    new_output = []
    for counter, words in enumerate(word):
        if counter == 1 and words == 'o' or counter == 1 and words == 'u' or words == 'i':
            new_output.append(words.upper())
        else:
            new_output.append(words)
    result = ''.join(new_output)
    print(result)
    return result

fn_hack_1("fooziman")
fn_hack_1("qux")
fn_hack_1("eq")