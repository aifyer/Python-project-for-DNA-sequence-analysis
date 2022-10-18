##=======python genome final project=======

import os
os.chdir("/Users/aifyer/Documents/work/python")

def removelines(value):
    return value.replace('\n','')

#==function read_fasta to read a fasta file and store in a dictionary

def read_fasta(file):
    try:
        f=open(file)
    except IOError:
        print ("File %s does not exist!" % file)

    seqs={}
    for line in f:
        line=removelines(line)
        if line[0]=='>':
            words=line.split()
            name=words[0][1:]
            seqs[name]=''
        else:
            line=line.rstrip()
            seqs[name]=seqs[name]+line
    f.close()
    return seqs

#===function fa_len to read a fasta dictionary and get seq length dictionary
def fa_len(seqs):
    flen={}
    for name,seq in seqs.items():
        flen[name]=len(seq)
    return flen

#====function find_orf to find the longest open reading frame
def find_orf(seqs,frame):
    out={}
    start_codon='atg'
    stop_codon=['tga','tag','taa']
    for name,seq in seqs.items():
        for i in range(frame-1,len(seq),3):
            codon=seq[i:i+3].lower()
            if codon in start_codon:
                for j in range(i+3,len(seq),3):
                    co=seq[j:j+3].lower()
                    if co in stop_codon:
                        start_pos=i+1
                        orf_len=j+3-i
                        posid=f'{name}{"_ORFpos_"}{start_pos}'
                        out[posid]=orf_len
                        break
            continue
    return out

def all_orf(seqs):
    allout={}
    d1=find_orf(seqs,1)
    d2=find_orf(seqs,2)
    d3=find_orf(seqs,3)
    allout=d1|d2|d3
    return allout

#========function  motif_repeat ======

def motif_rep(seqs,n):
    mout={}
    for name,seq in seqs.items():
        for i in range(0,len(seq)):
            m=seq[i:i+n].upper()
            if m not in mout:
                mout[m]=1
            else:
                mout[m]=mout[m]+1
    return mout


            
                
#===get max value from dict==
max(seqs.values()) #get max value
max(seqs,key=seqs.get) # get key of max value
#get multiple keys of max value
max_keys = [key for key, value in ages.items() if value == max(ages.values())]



