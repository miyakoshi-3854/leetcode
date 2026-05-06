class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            if fleet and fleet[-1] >= (target - pos) / spd:
                continue
            fleet.append((target - pos) / spd)

        return len(fleet)
