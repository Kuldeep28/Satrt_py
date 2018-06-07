
k=int(input())

for i in range(k):
    a=[]
    a=[int(i) for i in input().split(" ")]
    noo=a[0];b=a[1]
    w=[8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
    no=[1,2,3,4,5,6,7,8,9]
    no=no+no[::-1]
    dic=dict(zip(w,no))
    if b in dic.keys():
        for key,values in dic.items():
            print(key,"vd",values)
            if int(key)==b:
                print(int(values)%(10**9+7))
                break
    else:print(0%(10**9+7))
