from Algorithm import Algorithm
from Visualizer import Visualizer
from typing import List, Optional


class MergeSort(Algorithm):
    """Merge sort: Sort two different parts. After done, merge."""

    def __init__(
        self,
        visualizer: Visualizer,
        array_size: Optional[int] = 128,
    ) -> None:
        super().__init__(
            visualizer=visualizer, name="Merge Sort", array_size=array_size
        )

    def algorithm(self, array: List = []) -> None:
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []

        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result


if __name__ == "__main__":
    ARRAY_SIZE = 128  # Change array size if needed
    SLOW = False  # Remove this or change to True to get faster result

    visualizer = Visualizer(slow=SLOW)
    algorithm = MergeSort(visualizer)
    try:
        _, time_elapsed, count = algorithm.run()
        visualizer.keep_open(algorithm, time_elapsed, count)
        pass
    except Exception as e:
        print(f"Error: {e}")
