def p():
    a+1
    global b,c
    b=0


a = 1
p()
print(b,c)