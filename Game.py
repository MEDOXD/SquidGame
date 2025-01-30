import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Light, Green Light")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.Font(None, 74)

def red_light_green_light():
    print("Welcome to Red Light, Green Light!")
    print("You need to reach the finish line without getting caught.")
    
    distance = 0
    running = True
    light = "red"
    light_change_time = time.time() + random.uniform(0.5, 2)
    
    while running:
        screen.fill(WHITE)
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Change light
        if time.time() >= light_change_time:
            light = "green" if light == "red" else "red"
            light_change_time = time.time() + random.uniform(0.5, 2)
        
        # Display light
        if light == "green":
            pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), 100)
        else:
            pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 100)
        
        # Handle player movement
        keys = pygame.key.get_pressed()
        if light == "green" and keys[pygame.K_RETURN]:
            move = random.randint(1, 10)
            distance += move
            print(f"Green light! You moved {move} steps. Total distance: {distance}")
            time.sleep(0.1)  # Simulate reaction time
        elif light == "red" and keys[pygame.K_RETURN]:
            print("You were caught moving! Game over.")
            running = False
        
        # Check if player reached the finish line
        if distance >= 100:
            print("Congratulations! You reached the finish line.")
            running = False
        
        # Update the display
        pygame.display.flip()
        pygame.time.delay(100)
    
    pygame.quit()

def main():
    print("Welcome to Squid Game!")
    print("1. Play Red Light, Green Light")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        red_light_green_light()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
