# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 170,
    "MSFT": 400
}

total_investment = 0

print("Stock Portfolio Tracker")
print("-----------------------")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stocks:
        value = stocks[stock] * quantity
        total_investment += value
        print(stock, "Value:", value)
    else:
        print("Stock not available.")

print("-----------------------")
print("Total Investment:", total_investment)