# 產生一個隨機整數1~100 
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要說 比答案大還小

import random

r = random.randint(1,100)
count=0
while True:
	count+=1  #count=count+1
	num=int(input('請猜數字: '))
	if num == r:
		print('猜對了')
		print('這是你猜的第' ,count , '次')
		break
	elif num > r:
		print('比答案大喔')
	elif num <ｒ:
		print('比答案小喔')
	print('這是你猜的第' ,count , '次')
