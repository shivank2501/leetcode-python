def longestSubstr(s):
    d = {}
    start = 0
    m = 0
    for i,n in enumerate(s):
        if n in  d and start <=d[n]:
            start = d[n] +1
        else:
            m = max(m,i - start + 1)
        d[n] = i
    return m                


s = "pwwkew"
print(longestSubstr(s))








