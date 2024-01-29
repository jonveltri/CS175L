commission_rate_purchase = float(input("Enter Commission rate percentage (ex 0.03) on stock purchase: "))
commission_rate_sale = float(input("Enter Commission rate percentage (ex 0.03) on stock sale: "))
number_shares_purchased = float(input("Enter number of shares purchased: "))
number_shares_sold = float(input("Enter number of shares sold: "))
purchase_price = float(input("Enter purchase price per share: "))
sell_price = float(input("Enter sell price per share: "))

amountPaidForStock = (number_shares_purchased * purchase_price)
purchaseCommission = (commission_rate_purchase * amountPaidForStock)
totalPaid = (amountPaidForStock + purchaseCommission)

stockSoldFor = (number_shares_sold * sell_price)
sellingCommission = (commission_rate_sale * stockSoldFor)
totalRecieved = (stockSoldFor - sellingCommission)

profit = (totalRecieved - totalPaid)

print(f'Amount paid for stock: ${amountPaidForStock:,.2f}') 
print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print(f"Amount the stock sold for: ${stockSoldFor:,.2f}")
print(f"Commission paid on the sale: ${sellingCommission:,.2f}")
print(f"Profit (Or loss if negative): ${profit:,.2f}")