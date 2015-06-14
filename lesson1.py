x = int(raw_input('enter an integer : '))
ans = 0
while ans**3 < abs(x):
    ans += 1
    break
if ans**3 != abs(x):
    print x,'is no perfect square'
else:
    if x < 0:
        ans = -ans
        print 'cube root of' + str(x) + 'is' + str(ans)
