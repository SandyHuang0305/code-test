#密碼重試測試
password = 'a123456'
i = 3 #剩餘機會數
while  True :
	code = input('請輸入密碼')
	if code == password:
		print('密碼正確')
		break
	else:
		i = i - 1
		print('密碼錯誤,你還有', i,'次機會')
		if i == 0:
			break