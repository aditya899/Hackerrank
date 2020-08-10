def decryptPassword(s):
    # Write your code here
    S = list(s)
    num = []
    string = []
    i = 0
    while(i<len(s)):
        if(S[i].isnumeric() and int(S[i])!=0):
            num.append(S[i])
        elif(S[i].isupper() and S[i+1].islower()):
            string.append(S[i+1]+S[i])
            i+=2
        elif(S[i]=='0'):
            string.append(num[-1])
            num.pop()
        elif(S[i].islower() or S[i].isupper()):
            string.append(S[i])
        i+=1
    return ''.join(i for i in string)


if __name__ == '__main__':

    s = input()

    result = decryptPassword(s)

    print(result)
