class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = collections.Counter(s)
        countt = collections.Counter(t)
        
        return (countt-counts).keys().pop()
        
"""
s = 'qwert'
>>> t = 'wet'

>>> import collections
>>> ds = collections.Counter(s)
>>> dt = collections.Counter(t)
>>> ds-dt
Counter({'r': 1, 'q': 1})

>>> dt-ds
Counter()
>>> ds
Counter({'e': 1, 'r': 1, 'w': 1, 't': 1, 'q': 1})
>>> dt
Counter({'e': 1, 'w': 1, 't': 1})

string 查找字符
string.index(xx)

collection
第一种是新建一个dict，键是列表中的元素，值是统计的个数，然后遍历list。
搜索
items = ["cc","cc","ct","ct","ac"]
 
count = {}
for item in items:
    count[item] = count.get(item, 0) + 1
print(count)
#{'ac': 1, 'ct': 2, 'cc': 2}
之中用到了一个小技巧，当dict中不还没有统计过一个元素时，直接索引count[item]会报错，而使用get方法count.get(item, 0)能够设置索引不存在的键时返回0。

第二种
from collections import Counter
 
items = ["cc","cc","ct","ct","ac"]
count = Counter(items)
print(count)
#Counter({'ct': 2, 'cc': 2, 'ac': 1})


统计一个列表中每一个元素的个数

1. list 是否为空list
    if len(mylist):
    else:

    if mylist:
    else:
        
2.遍历 list 的同时获取索引

    i = 0
    for element in mylist: 
    # Do something with i and element
    i += 1
  
    for i, element in enumerate(mylist):
    # Do something with i and element
    pass

3. list排序
在包含某元素的列表中依据某个属性排序
    
    from operator import attrgetter
    for element in sorted(persons, key=attrgetter('age')):
    print "Age:", element.age
  
    
        """
