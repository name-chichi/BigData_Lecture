def flunk(s):
    return s < 60;

score = [40,80,50,70,90];
new_score = [];

# for s in filter(flunk,score):
#     print(s);

for s in filter(lambda x:x < 60,score):
    print(s);


# for s in score:
#     if s < 60:
#         new_score.append(s);
# print(new_score);

