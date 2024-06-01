from Algorithm import Algorithm
from Visualizer import Visualizer
from typing import List, Optional


class QuickSort(Algorithm):
    """Quick sort: Pick a pivot. Rearrange the items so that the lesser is on the left and the greater is on the right. Repeat."""

    def __init__(
        self,
        visualizer: Visualizer,
        array_size: Optional[int] = 128,
    ) -> None:
        super().__init__(
            visualizer=visualizer, name="Quick Sort", array_size=array_size
        )

    def algorithm(self, array: List = [], low: int = 0, high: int = 0) -> None:
        if array == []:
            array = self.array
            high = len(array) - 1

        if low < high:
            pivot_location = self.partition(array=array, low=low, high=high)
            self.algorithm(array=array, low=low, high=pivot_location - 1)
            self.algorithm(array=array, low=pivot_location + 1, high=high)

    def partition(self, array: List, low: int, high: int):
        pivot = array[low]
        left_wall = low

        for i in range(low + 1, high + 1):
            if array[i] < pivot:
                left_wall += 1
                array[i], array[left_wall] = array[left_wall], array[i]
                self.update_display(array[i], array[left_wall])

        array[low], array[left_wall] = array[left_wall], array[low]
        self.update_display(array[low], array[left_wall])

        return left_wall


if __name__ == "__main__":
    ARRAY_SIZE = 128  # Change array size if needed
    SLOW = True  # Remove this or change to True to get faster result

    visualizer = Visualizer(slow=SLOW)
    algorithm = QuickSort(visualizer)
    try:
        _, time_elapsed, count = algorithm.run()
        visualizer.keep_open(algorithm, time_elapsed, count)
        pass
    except Exception as e:
        print(f"Error: {e}")
