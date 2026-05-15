
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = list(zip(position,speed))
        cars.sort(key=lambda x: x[0])

        for c in cars:
            rate = (target-c[0])/c[1]
            while stack and stack[-1] <= rate:
                stack.pop()
            
            stack.append(rate)







        return len(stack)