import os

def read_file(filename):
	product = []
	with open(filename,'r', encoding = 'UTF-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue 
			name, price = line.strip().split(',') 
			product.append([name, price])
	return product

def user_input(product):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		product.append([name, price])
	return product

def print_product(product):
	for p in product:
		print(p[0],'的價格為', p[1])
	
def write_product(filename, product):
	with open(filename, 'w', encoding = 'UTF-8') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n') 

def main(filename):
	if os.path.isfile(filename):			
		print('讀取檔案中...')
		product = read_file(filename)
	else:
		product = []
		print('找不到檔案，請使用者填寫商品名稱')
	product = user_input(product)
	print_product(product)
	write_product(filename, product)

main('product.csv')