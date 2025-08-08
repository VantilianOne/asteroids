import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    
    
    #create dgroups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    # instantiate player
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    dt = 0 

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        #player_one.draw(screen)
        
        updatable.update(dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        for rock in asteroids:
            if rock.check_collision(player_one):
                event.type == pygame.QUIT
                return print("Game Over!")
            for bullet in shots:
                if rock.check_collision(bullet):
                    rock.split()
                    bullet.kill()
        
        
            
        for bullets in shots:
            bullets.draw(screen)

        pygame.display.flip()
        dt = Clock.tick(60)/1000

    

if __name__ == "__main__":
    main()
