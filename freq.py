def freq(s):
    alpha_count={}
    for alpha in s:
        alpha_count[alpha]=0
    for alpha in s:
        alpha_count[alpha]+=1
    return alpha_count   


# You can avoid an extra loop like this
def freq(s):
    alpha_count = {}
    for alpha in s:
        if s in alpha_count:
            alpha_count[alpha] += 1
        else:
            alpha_count[alpha] = 1
    return alpha_count
