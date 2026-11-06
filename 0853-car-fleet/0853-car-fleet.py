class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        que = deque()
        fleet = 0
        for p, s in cars:
            time = (target - p) / s
            if not que or time > que[-1]:
                que.append(time)


        return len(que)