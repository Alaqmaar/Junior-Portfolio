def payable(shopAmount, isMember):
	discount = 0
	
	if shopAmount >= 500 and shopAmount < 1000:
		discount = shopAmount*(5/100)
	if shopAmount >= 1000 and shopAmount < 2000:
        discount = shopAmount*(8/100)
	if shopAmount >= 2000:
        discount = shopAmount*(10/100)
    if isMember:
        discount += shopAmount*(5/100)
		
    netPayable = shopAmount - discount
    return netPayable
		
shopAmount = int(input("Enter Shopping Amount: "))
isMember = bool(input("Are you a member (True/False): "))

print(payable(shopAmount, isMember))
