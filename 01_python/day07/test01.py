import random

dic = dict(); # {}
datas = {1,2,3,4,5};

print(type(datas));
datas.add(6);
print(datas);
datas.remove(2);
print(datas);

datas.add(5);
print(datas);


list_data = [1,2,3,4,5,5,5];
set_data = set(list_data);
print(set_data);

# 1~45까지 6개의 Random 한 숫자를 만들어 봅시다.
nums = set();
while True:
    rnum = random.randint(1,45);
    nums.add(rnum);
    if len(nums) == 6:
        break;
print(nums);

s1 = [1,2,3,4];
s2 = [3,4,5,6];
ss1 = set(s1);
ss2 = set(s2);
ss1.update(ss2);
print(ss1);
result = list(ss1);
print(result);









