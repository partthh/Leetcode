class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
    # def canCompleteCircuit(gas, cost):
        total_surplus = 0
        current_surplus = 0
        start_index = 0

        for i in range(len(gas)):
            balance = gas[i] - cost[i]
            total_surplus += balance
            current_surplus += balance

            if current_surplus < 0:
                start_index = i + 1
                current_surplus = 0

        return start_index if total_surplus >= 0 else -1