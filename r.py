data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if  count % 1000 == 0 :
			print(len(data))
print('總共有', len(data), '筆資料')

sum = 0
for d in data:
	sum = sum + len(d)
print('留言平均長度為', sum/len(data))	

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('有', len(new), '筆資料長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('有', len(good), ' 筆資料提到good')