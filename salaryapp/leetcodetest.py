def strStr(haystack: str, needle: str) -> int:
    
    count = 0
    for i in range(0,len(haystack)):
        
        if haystack[i] == needle[count]:
            count += 1
        else:
            count = 0
            
            if haystack[i] == needle[count]:
                count += 1
                
        if count == len(needle):
            return i - count + 1 
        
    return -1
    

a = "mississippi"
b = "issip"

print(strStr(a,b))