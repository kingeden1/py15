print("Position Arguments")
def cal_amount(amount,tip):
    tip_percent=(amount*tip)/100
    total=amount+tip_percent
    print("Total Amount:",total)


cal_amount(1000,3)