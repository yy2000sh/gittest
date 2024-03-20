#  返回n进制转换
def convert_to_base_n(n, i):
    base_n = ""
    dic = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']
    while i > 0:
        digit = i % n
        base_n = dic[digit] + base_n
        i //= n
    return base_n

# 判断字符串是否回文
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]
         
if __name__ == '__main__':
    n = int(input("请输入一个20以内的整数："))
    for i in range(1,200):
        basen = convert_to_base_n(n,i*i)
        if (is_palindrome(basen)):
            print(f"整数为{i},转换后为{basen}")