import pygame
import sys
import time
from typing import Optional


class Visualizer:
    def __init__(self, slow: Optional[bool] = False) -> None:
        pygame.init()
        self.slow = slow
        self.dimensions = [1024, 512]
        self.background_color = "#ffffff"
        self.display = pygame.display.set_mode((self.dimensions[0], self.dimensions[1]))
        self.display.fill(pygame.Color(self.background_color))

    def _check_events(self):
        """Check if the pygame window was quit"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(
        self,
        algorithm,  # Algorithm Class
        swap1: Optional[int] = None,
        swap2: Optional[int] = None,
    ) -> None:
        """Update the display by swapping position"""

        self.display.fill(pygame.Color(self.background_color))
        pygame.display.set_caption("Sorting Visualizer")
        k = int(self.dimensions[0] / len(algorithm.array))

        for i in range(len(algorithm.array)):
            colour = (0, 0, 0)
            if swap1 == algorithm.array[i]:
                colour = (0, 255, 0)
            elif swap2 == algorithm.array[i]:
                colour = (255, 0, 0)

            pygame.draw.rect(
                self.display,
                colour,
                (i * k, self.dimensions[1] - algorithm.array[i], k, algorithm.array[i]),
            )
        self._check_events()
        pygame.display.update()
        if self.slow:
            time.sleep(0.05)

    def keep_open(self, algorithm, time: float, count: int) -> None:
        """Keep the window open"""

        pygame.display.set_caption(
            "Sorting Visualizer     Algorithm: {}     Time: {:.3f}     Comparison Count: {}      Status: Done!".format(
                algorithm.name, time, count
            )
        )
        while True:
            self._check_events()
