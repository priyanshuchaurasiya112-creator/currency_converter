from numpy import array

rates = array([
    [1,0.012, 0.011,0.0097,0.018,0.016,1.78,0.087],
    [90,1.07,1,0.87,1.68,1.47,158,7.75 ],
    [83,1,0.93,0.81,1.56,1.36,147.5,7.22 ],
    [103,1.23,1.15,1,1.93,1.7,182,8.92 ],
    [56,0.64,0.59,0.52,1,0.88,94.3,4.62 ],
    [62,0.74,0.68,0.59,1.13,1,107.2,5.15 ],
])

currency = ["INR", "EUR", "USD", "GBP","AUD","CAD"]

def conversion(amount, From, to):
    a = currency.index(From)
    b = currency.index(to)
    c = amount * rates[a][b]
    return c

print("Available Currencies: INR, EUR, USD, GBP, AUD, CAD ")
From = input("CONVERT FROM: ").upper()
to   = input("CONVERT TO: ").upper()

amt = float(input("Enter amount: "))
if amt>=0:
    r = conversion(amt, From, to)
    print(f"{amt} {From} = {r} {to}")
else:
    print("amount is not a negative no.")