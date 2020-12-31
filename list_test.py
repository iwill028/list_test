from collections import Counter
#list1=[1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 6, 4, 2, 3, 4, 6, 2, 2]
#set1=set(list1)
#for item in set1:
 #   print("The %d has found %d" %(item, list1.count(item)))


#list2=[17, 22, 36, 37, 52]
#list3=[7, 9, 14, 45, 49]
#list2.extend(list3)
#set2=set(list2)
#for item in set2:
 #   print("The %d has found %d" %(item, list2.count(item)))

from collections import Counter
list1=[1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 6, 4, 2, 3, 4, 6, 2, 2]
set1=Counter(list1)
set1=sorted(set1.items(), key=lambda item:item[1], reverse=True)
print(set1)