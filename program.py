import itertools
from pprint import pprint
n = int(input("Enter the number of records n: "))

nums = ['r'+str(i) for i in range(1,n+1)]

l = []
i = 1
while i<n+1:
    a_ = list(itertools.combinations(nums,i))
    l.append(a_)
    i = i+1

print(l)
def isunique(item,mainlist):
    l = []
    for i in item:
        for j in i:
            l.append(j)
    if len(l) == len(set(l)):
        if set(l) == set(mainlist):
            return item


def party(ll,n):
    nums = ['r'+str(i) for i in range(1,n+1)]
    l1 = []
    l2 = []
    for i in ll:
        for j in i:
            l1.append(j)
            for k in j:
                l2.append(k)

    q = []
    m = []
    print(l1)
    for i in range(2,n+1):
        mylist = list(itertools.combinations(l1[:-1],i))
        m.append(mylist)
        for i in mylist:
            q.append(isunique(i,nums))
    pprint(m)
    q = [i for i in q if i!=None]
    q.append(l1[-1])
    return q

def nprint(p,n):
    i = 1

    while i!=n+1:
        print("Clustering arrangements with ",i, " cluster:")
        if i == 1:
            print('No. of clustering arrangements:',i)
            print('The clusters are:' )
            print(p[-1],'\n')
        elif i==n:
            l = [j for j in p if len(j)==i]
            print('No. of clustering arrangements: ', len(l)-1)
            print('The clusters are:' )
            print(l[0],'\n')
        else:
            l = [j for j in p if len(j)==i]
            print('No. of clustering arrangements: ', len(l))
            print('The clusters are:' )
            print(l,'\n')
        i=i+1
    return


def main():
    partitions = party(l,n)
    print("Total number of possible clustering arrangements is ",len(partitions), '\n')
    nprint(partitions,n)


if __name__ == '__main__':
    main()
