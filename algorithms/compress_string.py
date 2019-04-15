# compress the string provided
# Input --> aabbbccdd
#Output --> a1b3c2d2


s = "aabbbbblllllskkdkfdsfsfdsfd"

# Version 1
def compress(s):
    compressed_s = ""
    i = 0
    while(i < len(s)):
        cnt = 1
        while (i+1 < len(s) and s[i] == s[i+1]):
            cnt = cnt + 1
            i = i + 1
            print("in",i)
        compressed_s = compressed_s + s[i] + str(cnt)
        i = i + 1
        print("out",i);
    return compressed_s
