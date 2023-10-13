class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        peak = self.find_peak_element(mountain_arr)
        first_try = self.binary_search(mountain_arr, target, 0, peak, True)
        if first_try == -1:
            return self.binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, False)
        return first_try

    def find_peak_element(self, mountain_arr):
        start, end = 0, mountain_arr.length() - 1

        while start < end:
            mid = start + (end - start) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                end = mid
            else:
                start = mid + 1
        return start

    def binary_search(self, mountain_arr, target, start, end, is_ascending):
        while start <= end:
            mid = start + (end - start) // 2
            mid_value = mountain_arr.get(mid)

            if mid_value == target:
                return mid

            if (is_ascending and mid_value < target) or (not is_ascending and mid_value > target):
                start = mid + 1
            else:
                end = mid - 1
        return -1