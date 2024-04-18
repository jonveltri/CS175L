# Jonathan Veltri
# CS 175L
# Expense Pie Chart

import matplotlib.pyplot as plt
import numpy as np

def createPieChart(expenseAmounts, expenseNames):
    plt.pie(expenseAmounts, labels=expenseNames)
    plt.title("Monthly Expenses")
    plt.show()

def main():
    expenseNames = []
    expenseAmounts = []
    with open("expenses.txt", "r") as file:
        count = 0
        for line in file:
            everything = line.strip().split("\t")
            name = everything[0]
            if len(everything) == 2:
                try:
                    expenseNames.append(name)
                    amount = float(everything[1])
                    expenseAmounts.append(amount)
                except ValueError:
                    print(f"INVALID AMOUNT FOR {name.upper()}")
                    expenseNames.pop(count)
            count += 1
    createPieChart(expenseAmounts, expenseNames)


if __name__ == "__main__":
    main()
