import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage the game assets and behavior."""

    def __init__(self):
        """Intializes the game, and create game resources."""
        # Initializes the background settings that Pygame needs to work properly.
        pygame.init()
        # Defines the pygame clock.
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Creates a display window.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # If the user clicks the game window close button, the game is exited.
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            # Sets the framerate to 60.
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()