months = ["January", "February", "March", "April", "May", "June", \
          "July", "August", "Septmeber", "October", "Nomvember", \
            "December"]

revenue = [32,000, 48,000, 72,000, 96,000, 120,000, 144,000, \
           168,000, 192,000, 216,000, 240,000, 264,000, 2888,000]

profit = [5,000, 10,000, 15,000, 20,000, 25,000, 30,000, \
           35,000, 40,000, 45,000, 50,000, 55,000, 60,000]

def month_idx(months):
    for idx, month in enumerate(months,1):
        print(f"{idx}. {month}")
    
def main():
    month_idx(months)

if __name__ == "__main__":
    main()