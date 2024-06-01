from Algorithm import Algorithm
from Visualizer import Visualizer
from typing import Optional


class InsertionSort(Algorithm):
    """Insertion Sort: Move item left until you find the correct place. Repeat until end of list."""

    def __init__(
        self,
        visualizer: Visualizer,
        array_size: Optional[int] = 128,
    ) -> None:
        super().__init__(
            visualizer=visualizer, name="Insertion Sort", array_size=array_size
        )

    def algorithm(self) -> None:
        array = self.array
        n = len(array)

        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                self.update_display(array[j], array[i])
                j -= 1

            array[j + 1] = key


if __name__ == "__main__":
    ARRAY_SIZE = 128  # Change array size if needed
    SLOW = True  # Remove this or change to True to get faster result

    visualizer = Visualizer(slow=SLOW)
    algorithm = InsertionSort(visualizer)
    try:
        _, time_elapsed, count = algorithm.run()
        visualizer.keep_open(algorithm, time_elapsed, count)
        pass
    except Exception as e:
        print(f"Error: {e}")
