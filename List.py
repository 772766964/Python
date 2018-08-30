
# 第一个索引为0，第二个为1……以此类推

# list类型用‘[]’表示

#创建list1,list2,list3三个列表并分别装入字符型整型和字节型
list1 = ["lalala","biubiubiu"] 
list2 = [1,2,3,4] 
list3 = ['a','b','c','d'] 

#输出的多种方式
print(list1[0])                    #将会输出  ["lalala","biubiubiu"] 

print(list2[0])                    #将会输出  1  （输出第一个）

print(list2[-2])                   #将会输出  3   (输出倒数第二个）

print(list3[0:3])                  #将会输出  ['a','b','c'] 
print(list3[0:4])                  #将会输出  ['a','b','c','d'] 
print(list3[0:5])                  #将会输出  ['a','b','c','d']

print(list3[4:0])                  #将会输出  []
print(list3[4:0:-1])               #将会输出  ['d','c','b']
print(list3[::-1])                 #将会输出  ['d','c','b','a']
print(list3[3::-1])                #将会输出  ['d','c','b','a']
print(list3[:0:-1])                #将会输出  ['d','c','b']
print(list3[2::-1])                #将会输出  ['c','b','a']

#Python列表脚本操作符(cmd中的python操作，故不需要print输出)
len(list3)          #输出结果为  4
list1+list2         #输出结果为  ["lalala","biubiubiu",1,2,3,4] 
list4=["Hello,"*5]  #输出结果为  ["Hello,Hello,Hello,Hello,Hello"]
list4=["Hello,"]*5  #输出结果为  ["Hello","Hello","Hello","Hello","Hello"]
"Hello" in list4    #输出结果为  True
2 in list2          #输出结果为  True

#如何在列表中添加元素呢？
list2.append(5)
list2 = [1,2,3,4,5] 
