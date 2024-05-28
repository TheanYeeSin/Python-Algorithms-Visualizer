import random
import time
from abc import ABCMeta, abstractmethod
from typing import List, Optional, Tuple


class Algorithm(metaclass=ABCMeta):
    def __init__(
        self,
        visualizer,  # Visualizer Class
        name: str,
        array_size: Optional[int] = 128,
    ) -> None:
        self.visualizer = visualizer
        self.name = name
        self.array = random.sample(range(512), array_size)
        self.count = 0  # Comparison count

    def update_display(
        self, swap1: Optional[int] = None, swap2: Optional[int] = None
    ) -> None:
        """Update the display of the algorithm"""
        self._increase_count()
        self.visualizer.update(algorithm=self, swap1=swap1, swap2=swap2)

    def run(self) -> Tuple[List, float, int]:
        """Start the timer and run the algorithm"""
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed, self.count

    def _increase_count(self) -> None:
        self.count += 1

    @abstractmethod
    def algorithm(self) -> None:
        """Algorithm function"""
        raise NotImplementedError
