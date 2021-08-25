import pygame
pygame.init() 
#Create variables as required

size = (400, 400)
screen = pygame.display.set_mode(size)
bedroom=pygame.image.load("Assets/room.png").convert()
bedroom_scaled=pygame.transform.smoothscale(bedroom,(600,400))
john=pygame.image.load("Assets/john.png").convert_alpha()
john_scaled=pygame.transform.smoothscale(john,(300,300))
pygame.display.set_caption("Project C10")
#Create "carryOn" variable and set to true
carryOn = True
#Begin the while loop
while carryOn:
  #Iterate through each event
  for event in pygame.event.get():
    #Identify is user has quit 
    if event.type == pygame.QUIT: 
      #change "carryOn" to False
      carryOn = False 
  screen.blit(bedroom_scaled,(0,0))
  #Code for user input
  
  
  
  
  screen.blit(john_scaled,(johnx,johny))
  pygame.display.flip()
pygame.quit()
