from Algorithm import Algorithm
from Visualizer import Visualizer
from typing import Optional


class BubbleSort(Algorithm):
    """Bubble sort: Push greater item forward."""

    def __init__(
        self,
        visualizer: Visualizer,
        array_size: Optional[int] = 128,
    ) -> None:
        super().__init__(
            visualizer=visualizer, name="Bubble Sort", array_size=array_size
        )

    def algorithm(self) -> None:
        array = self.array
        n = len(array)

        for i in range(n):
            for j in range(0, n - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self.update_display(array[j], array[j + 1])


if __name__ == "__main__":
    ARRAY_SIZE = 128  # Change array size if needed
    SLOW = False  # Remove this or change to True to get faster result

    visualizer = Visualizer(slow=SLOW)
    algorithm = BubbleSort(visualizer)
    try:
        _, time_elapsed, count = algorithm.run()
        visualizer.keep_open(algorithm, time_elapsed, count)
        pass
    except Exception as e:
        print(f"Error: {e}")
