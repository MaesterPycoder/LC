class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] == 0:
                    continue
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    placed += 1
                    break
                        

        return len(fruits) - placed
