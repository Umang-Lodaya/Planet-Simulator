import math
import pygame
pygame.init()

WIDTH, HEIGHT = 1500, 780

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 200 / AU  # 1 AU = 200 px
    TIMESTEP = 60 * 60 * 24 * 1 # 1 DAY

    def __init__(self, name, x, y, radius, color, mass, yVel = 0, sun = False):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = sun
        self.distanceToSun = 0

        self.xVel = 0
        self.yVel = yVel

    def draw(self, GAME, displayName = True):
        # SCALING AND ADJUSTING AT THE CENTRE
        x = self.x * self.SCALE + WIDTH // 2
        y = self.y * self.SCALE + HEIGHT // 2
        pygame.draw.circle(GAME, self.color, (x, y), self.radius)

        updatedPoints = []
        if len(self.orbit) > 2:
            for x, y in self.orbit:
                x = x * self.SCALE + WIDTH // 2
                y = y * self.SCALE + HEIGHT // 2
                updatedPoints.append((x, y))
        
            pygame.draw.lines(GAME, self.color, False, updatedPoints, 2)
        
        if displayName:
            name = FONT.render(f"{self.name.upper()}", 1, (255, 255, 255))
            GAME.blit(name, (x - name.get_width() / 2, self.radius + y - name.get_height() / 2))


    def attraction(self, other):
        otherX, otherY = other.x, other.y
        distX = otherX - self.x
        distY = otherY - self.y
        dist = math.sqrt(distX**2 + distY**2)

        if other.sun:
            self.distanceToSun = dist

        # F = G x M x m / r ** 2
        force = self.G * self.mass * other.mass / dist ** 2
        theta = math.atan2(distY, distX)
        # tan(Θ) = Y / X
        forceX = math.cos(theta) * force
        forceY = math.sin(theta) * force
        return forceX, forceY
    
    def updatePosition(self, planets):
        FX, FY = 0, 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            FX += fx
            FY += fy
        
        # F = ma = mv / t
        # v = F * t / m
        self.xVel += FX * self.TIMESTEP / self.mass
        self.yVel += FY * self.TIMESTEP / self.mass

        self.x += self.xVel * self.TIMESTEP
        self.y += self.yVel * self.TIMESTEP
        self.orbit.append((self.x, self.y))