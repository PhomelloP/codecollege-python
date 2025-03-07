import pygame.font
import pygame

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)  # Green
        self.text_color = (255, 255, 255)  # White
        self.border_color = (0, 0, 0)  # Black border
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button, border, and then draw message."""
        # Draw the button background
        self.screen.fill(self.button_color, self.rect)
        # Draw the border
        pygame.draw.rect(self.screen, self.border_color, self.rect, 2)
        # Draw the message
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def is_clicked(self, mouse_pos):
        """Check if the button is clicked."""
        return self.rect.collidepoint(mouse_pos)