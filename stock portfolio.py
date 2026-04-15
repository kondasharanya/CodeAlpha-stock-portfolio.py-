def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 330,
        "AMZN": 145,
        "NVDA": 875
    }
    portfolio = {}
    total_investment = 0
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter 'done' when finished adding stocks.\n")
    while True:
        stock_name = input("Enter stock symbol: ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print(f"Stock {stock_name} not available. Choose from {list(stock_prices.keys())}")
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

        print(f"Added {quantity} shares of {stock_name}\n")
    print("\n" + "=" * 40)
    print("YOUR PORTFOLIO SUMMARY")
    print("=" * 40)
    if not portfolio:
        print("No stocks added to portfolio.")
        return
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock}: {qty} shares x ${price} = ${value}")
    print("-" * 40)
    print(f"Total Investment Value: ${total_investment}")
    save = input("\nSave result to file? (y/n): ").lower()
    if save == 'y':
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("=" * 30 + "\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
            file.write("-" * 30 + "\n")
            file.write(f"Total Investment Value: ${total_investment}\n")
        print("Saved to portfolio_summary.txt")
if __name__ == "__main__":
    stock_portfolio_tracker()