class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo = {}
        return self.dfs(start, fuel, finish, locations) % (10 ** 9 + 7)
        # 因为到同一个点，fuel 情况不同，状态会发生变化！！ 所以 cur 和fuel 一起作为 状态
    def dfs(self, cur, fuel, target, location):
        if cur == target:
            result = 1
        else:
            result = 0
        if (cur, fuel) in self.memo:
            return self.memo[(cur, fuel)]
        for i in range(len(location)):
            if cur != i and abs(location[i] - location[cur]) <= fuel:
                result += self.dfs(i, fuel - abs(location[i] - location[cur]), target, location)
        self.memo[(cur, fuel)] = result
        return result 