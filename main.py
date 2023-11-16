import pygame
from Planet import Planet

pygame.init()
pygame.display.set_caption("SOLAR SIMULATION")

WIDTH, HEIGHT = 1500, 780
GAME = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
FONT = pygame.font.SysFont("comicsans", 16)

COLORS = {
    "WHITE": (255, 255, 255),
    "YELLOW": (255, 255, 0),
    "BLACK": (0, 0, 0),
}

if __name__ == "__main__":

    run = True
    clock = pygame.time.Clock() # TO SET AN UPPER BOUND ON FPS

    SUN = Planet("SUN", 0, 0, 30, COLORS["YELLOW"], 1.98892 * 10**30, sun = True)    
    MERCURY = Planet("MERCURY", -0.387 * Planet.AU, 0, 8, (26, 26, 26), 3.30 * 10**23, yVel = 47.4 * 1000)
    VENUS = Planet("VENUS", -0.723 * Planet.AU, 0, 14, (230, 230, 230), 4.8685 * 10**24, yVel = 35.02 * 1000)
    EARTH = Planet("EARTH", -1 * Planet.AU, 0, 16, (47, 106, 105), 5.9742 * 10**24, yVel = 29.78 * 1000)
    MARS = Planet("MARS", -1.524 * Planet.AU, 0, 12, (153, 61, 0), 6.417 * 10**23, yVel = 24.077 * 1000)
    JUPITER = Planet("JUPITER", -5.2 * Planet.AU, 0, 20, (176, 127, 53), 1.899 * 10**27, yVel = 13.07 * 1000)
    SATURN = Planet("SATURN", -9.5 * Planet.AU, 0, 17, (176, 143, 54), 5.685 * 10**26, yVel = 9.69 * 1000)
    URANUS = Planet("URANUS", -19.2 * Planet.AU, 0, 14, (85, 128, 170), 8.682 * 10**25, yVel = 6.81 * 1000)
    NEPTUNE = Planet("NEPTUNE", -30.1 * Planet.AU, 0, 15, (54, 104, 150), 1.024 * 10**26, yVel = 5.43 * 1000)

    PLANETS = [SUN, MERCURY, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE]

    while run:
        clock.tick(FPS)
        GAME.fill(COLORS["BLACK"])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in PLANETS:
            planet.updatePosition(PLANETS)
            planet.draw(GAME)
        
        pygame.display.update()
    
    pygame.quit()