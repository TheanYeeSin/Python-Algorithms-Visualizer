from Algorithm import Algorithm
from Visualizer import Visualizer
from typing import Optional


class SelectionSort(Algorithm):

    def __init__(
        self,
        visualizer: Visualizer,
        array_size: Optional[int] = 128,
    ) -> None:
        super().__init__(
            visualizer=visualizer, name="Selection Sort", array_size=array_size
        )

    def algorithm(self) -> None:
        array = self.array
        n = len(array)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if array[j] < array[min_idx]:
                    min_idx = j

            if min_idx != i:
                array[i], array[min_idx] = array[min_idx], array[i]
                self.update_display(array[i], array[min_idx])


if __name__ == "__main__":
    ARRAY_SIZE = 128  # Change array size if needed
    SLOW = False  # Remove this or change to True to get faster result

    visualizer = Visualizer(slow=SLOW)
    algorithm = SelectionSort(visualizer)
    try:
        _, time_elapsed, count = algorithm.run()
        visualizer.keep_open(algorithm, time_elapsed, count)
        pass
    except Exception as e:
        print(f"Error: {e}")
