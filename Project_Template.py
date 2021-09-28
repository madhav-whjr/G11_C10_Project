import pygame
pygame.init() 

# Set the value of johnx to 190
johnx = 
# Set the value of johny to 150
johny = 

size = (400, 400)
screen = pygame.display.set_mode(size)
bedroom=pygame.image.load("room.png").convert()
bedroom_scaled=pygame.transform.smoothscale(bedroom,(600,400))
john=pygame.image.load("john.png").convert_alpha()
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
  # Check for the user input
  if event.type == pygame.KEYDOWN:
        # Check if event.key is left key
        if event.key ==           :
                # Decrement johnx by 5 units
                johnx =   
              
  screen.blit(john_scaled,(johnx,johny))
  pygame.display.flip()
pygame.quit()
