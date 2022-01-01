class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(s.split())
        d=[]
        y=[x for x in s]
        f=""
        for i in range(len(s)):
            res=[]
            x=int(s[i][len(s[i])-1])
            res.append(x-1)
            res.append(s[i])
            d.append(res)

        d.sort()
        i=0
        result=[]
        while i<len(d):
            result.append(d[i][1])
            i=i+1

        for i in range(len(result)):
            for j in result[i]:
                if not j.isdigit():
                    f=f+j
            f=f+" "

        f=f.strip()


        return f


        
