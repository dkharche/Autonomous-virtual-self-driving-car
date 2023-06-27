import pygame
import math
pygame.init()


window = pygame.display.set_mode((1200,400))
track = pygame.image.load('path29.png')

car = pygame.image.load('car1.png')
font = pygame.font.SysFont("Arial", 25)

car = pygame.transform.scale(car, (43, 60))

car_x = 150
car_y = 300


obs = pygame.image.load('obs.png')
obs = pygame.transform.scale(obs, (87, 150))
obs_x = 250
obs_y = 200

obs1 = pygame.image.load('obs1.png')
obs1 = pygame.transform.scale(obs1, (150, 87))
obs1_x = 255
obs1_y = 65

obs2 = pygame.image.load('obs2.png')
obs2 = pygame.transform.scale(obs1, (200, 90))
obs2_x = 815
obs2_y = 275

obs3 = pygame.image.load('obs3.png')
obs3 = pygame.transform.scale(obs3, (95,150))
obs3_x = 1030
obs3_y = 150

focal_dis = 17
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'

# counter = 100

drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    obs_x=obs_x-0.05
    obs3_x = obs3_x+0.05

    # counter -= 0.05
    # 
    # petrolPump_x = 550
    # petrolPump_y = 150
    # def goToPetrolPump(self, petrol_pump_x, petrol_pump_y, car_x, car_y, car, counter):
    #     dist_from_petrol_pump = self.distance(petrol_pump_x, petrol_pump_y)

    # def distance(self, pmX, pmY):
    #     xDist = math.sqrt(((car_x - pmX) * (car_x - pmX)))
    #     yDist = math.sqrt(((car_y - pmY) * (car_y - pmY)))
    # 
    #     if xDist > yDist:
    #         greaterDist = xDist
    #     else:
    #         greaterDist = yDist
    #     return greaterDist

    # if counter<20:
    #     def goToPetrolPump(self, petrol_pump_x, petrol_pump_y, car_x, car_y, car, counter):
    #         dist_from_petrol_pump = self.distance(petrol_pump_x, petrol_pump_y)
    #         car = pygame.transform.rotate(car, 180)
    #         if counter < 20 and dist_from_petrol_pump > 0:
    #             if car_x > petrol_pump_x and direction == 'up' and up_px == 255:
    #                 car_y = car_y - 2
    # 
    #             elif car_x < petrol_pump_x and direction == 'right' and right_px == 255:
    #                 car_x = car_x + 2
    #             elif car_y > petrol_pump_y and direction == 'up' and left_px == 255:
    #                 car_y = car_y - 2
    #             elif car_y < petrol_pump_y and direction == 'down' and down_px == 255:
    #                 car_y = car_y + 2
    #             self.chargeLevel -= 0.1
    #         else:
    #             self.carStop = True
    #             counter += 0.05

    text = font.render(str(int(counter)), True, (0, 0, 0))
    text_rect = text.get_rect(center=(155, 350))


    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    left_px = window.get_at((cam_x - focal_dis, cam_y))[0]
    print(up_px, right_px,left_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car,90)
    elif direction == 'up' and up_px != 255 and left_px == 255:
        direction = 'left'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car,-90)

    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2

    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2

    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2

    elif direction == 'up' and left_px == 255:
        car_y = car_y - 2

    # Initializing coordinates of the petrol pump
    petrolPump_x = 550
    petrolPump_y = 150


    window.blit(track, (0, 0))
    window.blit(text, text_rect)
    window.blit(car, (car_x, car_y))
    window.blit(obs, (obs_x, obs_y))
    window.blit(obs1, (obs1_x, obs1_y))
    window.blit(obs2, (obs2_x, obs2_y))

    window.blit(obs3, (obs3_x, obs3_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
