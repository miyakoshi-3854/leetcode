"""
121. Best Time to Buy and Sell Stock

条件
1番安い日に買う
買った日以降の1番高い日に売る

思考
sliding window使う問題
どんなアルゴだったか覚えていないな

1番安い日は、sortして1つ目を取るとかでいけそうだが、しゃばいか？
→ min(prices)でいいんじゃね


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
