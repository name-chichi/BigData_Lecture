list1 = [1,2,3,4,5];
list2 = list1.copy();
list3 = list1;

print(list1 is list2);
print(list1 is list3);
print(list2 is list3);

list2[2] = 30;

print(list1);
