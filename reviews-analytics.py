data=[]
count=0
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count+=1
		if count % 1000 ==0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100')

print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
# print(good[0])
# good = [1 for d in data if 'good' in d]
# print(good)

# bad = ['bad'in d for d in data ]
# print(bad)

#文字計數
wc = {} #word_count
for d in data:
	words = d.split() #如果有連續3個空字串 ''會切成3分 但若直接打split()會跳過不切
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的Key進wc字典
for word in wc:
	if wc[word] > 1000000: 
		print(word, wc[word])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break 
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else: 
		print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')



