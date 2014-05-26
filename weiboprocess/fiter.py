
# _*_ coding:'utf-8' _*_


def singleLine(s):
    line = s.split(' ')
    length = len(line)
    date = line[1]+'/'+line[2]
    time = line[3]+'/'+line[5]
    i = 7
    str = ''
    while i < length-2:
        str += ' '+line[i]
        i += 1
    return date+' '+time+' '+str
    

if __name__ == '__main__':
    num = 0
    with open('AllRecent.txt','r') as f:
        for line in f.readlines():
            str = singleLine(line)
            with open('originweibo.txt','a') as fout:
                fout.write(str+'\n')
            num += 1
            print num/1135266.0