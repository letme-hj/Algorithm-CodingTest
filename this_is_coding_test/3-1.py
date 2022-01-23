def change(price):
    hunds = price // 100
    tens = price % 100 // 10
    five_hund = hunds // 5
    one_hund = hunds % 5
    fifty = tens // 5
    ten = tens % 5
    return five_hund + one_hund + fifty + ten


print(change(1260))
    
