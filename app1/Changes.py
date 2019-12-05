import itertools

def Change(number,lists):
#将x转换为整数。如果x是字符串，则要base指定基数。
    basetwo = int(str(number), base=2)
    for foo in range(1,len(lists)+1):
    #创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序。
        data  = list(itertools.combinations(lists,foo))
        value  = [i for i in data if basetwo == sum(i)]
        if value:
            return list(value[0])

