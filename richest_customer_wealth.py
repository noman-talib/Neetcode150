class Solution:
    def maximumWealth(self, accounts):

        rich = 0

        for i in accounts:

            wealth = 0

            for j in i:
                wealth += j

            rich = max(rich, wealth)

        return rich