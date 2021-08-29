product = []

with open('products.txt' ,'r', encoding = 'UTF-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue 
		name, price = line.strip().split(',') 
		product.append([name, price])

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	product.append([name, price])

for p in product:
	print(p[0],'的價格為', p[1])

with open('products.txt', 'w', encoding = 'UTF-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n') 