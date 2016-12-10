def panagram(s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in s:
           return False
    return True   
