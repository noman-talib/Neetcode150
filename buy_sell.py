def maxProfit(prices):
    min = prices[0]
    max = 0

    for i in range(0, len(prices)):
        if prices[i] < min:
            min = prices[i]

        profit = prices[i] - min

        if profit > max:
            max = profit

    return max


prices = [7, 1, 5, 4, 6, 4]
print(maxProfit(prices))