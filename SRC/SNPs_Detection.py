def compile(file):
    seq=[]
    for line in file:
        x=line.rstrip()
        z=x.upper()
        if not z.startswith('>'):
            seq.append(z)
    sequence=''.join(seq)
    return sequence
def check(seq):
    flag=0
    while flag==0:
        if len(seq)!=466:
            x=input('Incorrect sequence,Please make sure you enter an insulin gene')
        else:
             x='None'
             flag=1
             return seq
    
def Hashtable(sequence):
    x={'A':1,'C':2,'G':3,'T':4}
    hashtable={}
    k=3
    length=len(sequence)
    value=0
    for i in range(0,length):
        f=sequence[i:i+k]
        for j in f: 
            v=x.get(j)
            value=v*(4**((2*length)- i-1)) + value
            i=i+1
        if f not in hashtable:
            hashtable[f]=[value//(400*length)**36]
        else:
            hashtable.get(f).append(value//(400*length)**36)
        if len(f)!= k:
            hashtable.pop(f)
        value=0
    return hashtable

def diff(original,query):
    import copy
    output={}
    for k1,q in query.items():
        for k2,org in original.items():
            if k1 == k2:
                if len(org)>len(q):
                    tmp = copy.deepcopy(org)
                    for k in q:
                        if k in tmp:
                            tmp.remove(k)
                    output[k1]=tmp
                elif len(q)>len(org):
                    tmp = copy.deepcopy(q)
                    for k in org:
                        if k in tmp:
                            tmp.remove(k)
                    output[k1]=tmp
    return output

def SNPs(output):
    pos={}
    x={'A':1,'C':2,'G':3,'T':4}
    length= 466
    if len(output)!=0:
        for k,i in output.items():
            j=0
            while j <= length:
                v=((x.get(k[0]))*(4**((2*length)-j-1)))+((x.get(k[1]))*(4**((2*length)-(j+1)-1)))+((x.get(k[2]))*(4**((2*length)-(j+2)-1)))
                val=v//(400*466)**36
                if val in i:
                    if j not in pos:
                        pos[j]=[k]
                        break
                    else:
                        pos.get(j).append(k)
                        break
                else:
                    j=j+1
        delete=[]
        for k,q in pos.items():
            if len(q)!=2:
                delete.append(k)
        for i in delete:
            pos.pop(i)
        print(pos)
        snps={}
        for key,i in pos.items():
            f,g=i
            z=key
            for h in range(3):
                if f[h]== g[h]:
                    z=z+1
                else:
                    snps[z]=[g[h],f[h]]
                    break
        return snps
    else:
        return 'Your sequence do not have SNPs'
