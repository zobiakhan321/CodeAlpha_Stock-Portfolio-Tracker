# Stock Portfolio Tracker

# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

# Dictionary to store user's stock holdings
portfolio = {}

print("Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Stock not found. Please enter a valid symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock} shares: "))
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number for quantity.")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
total_investment = 0
print("\nInvestment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to a .txt file
save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Summary saved to portfolio_summary.txt")
