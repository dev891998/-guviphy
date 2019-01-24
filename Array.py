n,k=map(int,input().split())
aa=[]
c=0
aa=list(map(int,input().split()))
for i in range(0,len(aa)-1):
    if i<k:
        c=c+aa[i]
print(c)
