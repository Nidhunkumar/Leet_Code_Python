'''
Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.

'''
# stri="def validate(num):    return num=num[::-1]"
# if "def" not in stri:
#     print("missing def")
# elif "()"  in stri:
#     print("missing param")
# elif ":" not in stri:
#     print("missing :")
# elif "("  and ")"not in stri:
#     print("missing param")
# elif "validate" not in stri:
#     print("missing wrong name")
# elif "return" not in stri:
#     print("missing return")
# elif "    " not in stri:
#     print("missing intent")
# else:
#     print(True)

print(list(map(lambda x ,v: x*3+v*3, [i for i in range(1,10) ],[i for i in range(1,10) ])))

