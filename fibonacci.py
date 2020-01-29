num = int(input("how many terms?"))
a1,a2 = 0,1
count = 0
print("fibonacci seq")
while count<num:
    print(a1)
    nth=a1+a2
    a1=a2
    a2=nth
    count+=1


'''
sample output:
how many terms?5
fibonacci seq
0
1
1
2
3
'''
