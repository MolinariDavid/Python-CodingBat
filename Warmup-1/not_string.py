'''
Given a string,
return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged. 

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
'''

def not_string(mstr):
    mehNot = 'not'
    if len(mstr) >= 3 and mstr[:3] == mehNot:
        return mstr
    return mehNot + " " + mstr


print(not_string("candy"))
print(not_string("x"))
print(not_string("not bad"))
print(not_string("no"))
