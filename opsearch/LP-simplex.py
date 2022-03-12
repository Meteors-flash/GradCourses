import numpy as np   
d = [
    [1,4,2,1,0,48],
    [1,2,4,0,1,60],
    [6,14,13,0,0,0]#z
]
d = np.array(d, dtype='float64')
def solve(d):
    (bn,cn) = d.shape
    s = list(range(cn-bn,cn-1)) #基变量列表
    while max(d[-1][:-1]) > 0:
        jnum = np.argmax(d[-1][:-1]) #转入下标
        out = d[:-1,-1]/np.maximum(0,d[:-1,jnum])
        np.place(out,np.isnan(out),np.inf) # np.nan替换为np.inf
        inum = np.argmin(out)  #转出下标
        s[inum] = jnum #更新基变量
        d[inum]/=d[inum][jnum]
        for i in range(bn):
            if i != inum:
                d[i] -= d[i][jnum] * d[inum]
    #打印
    for i in range(d.shape[1] - 1):
        print("x%d=%.2f" % (i,d[s.index(i)][-1] if i in s else 0))
    print("objective is %.2f"%(-d[-1][-1]))
solve(d)