import random

# 0.0 ~ 0.9999999999999
for i in range(5):
    print(random.random());

for i in range(5):
    print(random.randint(1,100));

for i in range(5):
    print(random.uniform(1,100));

data = [100,200,500,300,400];
print(random.choice(data));
print(random.sample(data,3));

random.shuffle(data);
print(data);

lotto_num = random.sample(range(1,46),6);
print(lotto_num);