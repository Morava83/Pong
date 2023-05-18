#BRIAN MORAVA
#January 18, 2019 
#Pong Game - Culminating Assignment
'''
The purpose of my program is to run pong, or a game which involves a ball bouncing between two user controlled paddles. The objective of the game is to not let the ball go 
past your paddle and try to make the ball go past your opponents paddle. The ball bounces off your paddle thus pong is similar to a 2d version of tennis where the paddles 
are the tennis rackets and the tennis ball is the pong ball. You lose a point every time the ball passes your paddle and you gain a point every time the ball passes your
opponent's paddle.  
'''
#Here I import the pygame module inorder to display shapes, pictures, and text to the screen.
import pygame
#I imported the random module inorder to create multiple random numbers throughout the program (e.x. the winning score is a random number).
import random
'''
I imported the time module for the GAME OVER screen, since the code for this is outside the while loop I needed a stall or buffer in the program for it to be displayed for 
a sustained amount of time. Without this the pygame.quit command would immediately close the program and the GAME OVER screen would merley flash.
'''
import time
#The next three lines are from the pygame base code
pygame.init()
size = (800,500)
screen = pygame.display.set_mode(size)
#These are some colors I use later on with their corrresponding color codes in RGB order.
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (160,32,240)
#I need a color variable because I want the inital color of something in my program (the words PLAY) to be black but then to change to something else later. 
color = BLACK
#The number of points one has to score is determined by generating a random number between 10 and 20 as seen below.
winning_points = random.randrange(10,21)
#These are the initial x and y coordinates of the pong ball. I need these to be variables as the pong ball will move and thus so will their coordinates.
circle_x_pos = 400
circle_y_pos = 250
'''
These are the inital speeds (as well as direction of movements) of the pong ball. I need these to be variables as the speed and direction of the pong ball will change each 
time that it touches a paddle.
'''
circle_x_speed = 7
circle_y_speed = 7
'''
This is an accumulator variable which increases every time that the pong ball touches a paddle. (This is done later on in the program) It is added on (or subtracted on 
depending on how you look at it) to the speed variable in order to increase the speed of the pong ball.
'''
variable_x_speed = 0
#This is the y-coordinate of the top left corner of player 1's paddle or the left paddle. It must be a variable as the y-position of both paddles change. 
bar_1_y_pos = 190 
#This is used to create a smooth flow of downward paddle movement for the left paddle. If this were not here then you would have to keep pressing the s key over and over again
bar_1_pos_y_desire = False
#This is used to create a smooth flow of upward paddle movement for the left paddle. If this were not here then you would have to keep pressing the w key over and over again
bar_1_neg_y_desire = False
#This is the y-coordinate of the top left corner of player 2's paddle or the right paddle. It must be a variable as the y-position of both paddles change.
bar_2_y_pos = 190
#This is used to create a smooth flow of downward paddle movement for the right paddle. If this were not here then you would have to keep pressing the down key over and over again
bar_2_pos_y_desire = False
#This is used to create a smooth flow of upward paddle movement for the right paddle. If this were not here then you would have to keep pressing the up key over and over again
bar_2_neg_y_desire = False
#Here I am defining some fonts for later use
font = pygame.font.SysFont("Calibri",35,True,True)
font_2 = pygame.font.SysFont("Arial",70,True,True)
font_3 = pygame.font.SysFont("Arial",40,True,True)
#These are the score variables of player 1 and 2 respectively. These must be variables as the players' scores change.
score_a = 0
score_b = 0 
#This loads my pong music  
pygame.mixer.music.load("pong.ogg")
#This plays my pong music indefinetly as the loop number is set to -1. The music starts playing at the 10 second mark of the song as the second parameter is 10.  
pygame.mixer.music.play(-1,10)
screen_mode = 1
#Clock used to regulate the movement speed of mainly just the ball as its speed increases each time it touches a paddle. 
clock = pygame.time.Clock()
'''
Done is inialized to false which will make the while loop run due it being negated in the loop's condition. Done's value is overwritten to false which will end the loop 
under conditions in which the game should end i.e when the winning score is reached or when a player presses the x in the top right corner.
'''
done = False
'''
This is the while loop which holds the important parts of the programe. It's condition is not (done) because we want the game to end when done is true. The 
conditions which make done true are if the x button is pressed or if the winning score is reached by any one of the two players.
'''
while not done:
    #The next three lines of code constantly retrive the position of the mouse which is important later on
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]          
    #This for loop constantly loops through all of the events that have been generated 
    for event in pygame.event.get():
        #If an event is the user pressing the x button then this if statement will set done true which will end the loop and ultimately the game
        if event.type == pygame.QUIT:
            done = True
        '''This if statement dictates what happens if a key is pressed down. If a key is pressed down the program will check to see if the key was a w,s,UP or DOWN key and 
        then change their corresponding boolean value to True which represents a sustained movement of either up or down.''' 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bar_1_neg_y_desire =  True
            if event.key == pygame.K_s:
                bar_1_pos_y_desire =  True  
            if event.key == pygame.K_UP:
                bar_2_neg_y_desire =  True
            if event.key == pygame.K_DOWN:
                bar_2_pos_y_desire =  True              
        '''This if statement changes all of those values to False which means that the sutained movement of either up or down will stop as soon as they lift their finger 
        from the particular key or generate a KEYUP event.'''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                bar_1_neg_y_desire =  False
            if event.key == pygame.K_s:
                bar_1_pos_y_desire =  False
            if event.key == pygame.K_UP:
                bar_2_neg_y_desire =  False
            if event.key == pygame.K_DOWN:
                bar_2_pos_y_desire =  False             
        '''This if statement checks if any three of the mouse buttons were pressed. If any one of these three were pressed then the program retrives which one is pressed 
        and performs another if statment to see if it were the right mouse button and if it were in a particaler area of the screen (where the play button is) when it 
        was pressed. It then changes the screen to the main/actual game screen if all of these condition held true. This effectively brings the player to the game screen 
        when the play button is pressed.''' 
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons = pygame.mouse.get_pressed()
            if buttons[0] and x >= 340 and x <= 450 and y >= 220 and y <= 280:
                screen_mode = 2          
    #Due to my inefficent flashing mechanisim of the play button I force the game screen to appear after 33 seconds becuase the play button only flashes for 33 seconds
    if pygame.time.get_ticks() > 33000:
        screen_mode = 2 
    #This loads my pong image which is later displayed between the two scores 
    logo = pygame.image.load("ponglogo.png")
    #This resizes my image to make it fit between the two scores and above the horizontal line
    logo = pygame.transform.scale(logo,(150,40))
    #Bar Movement and Restrictions 
    #If the w key is held which makes the negative y desire true then the position of the left paddle will consitently move 6 pixels up until the w key is no longer being held down
    if bar_1_neg_y_desire:
        bar_1_y_pos -= 6
    #If the s key is held which makes the positive y desire true then the position of the left paddle will consitently move 6 pixels down until the s key is no longer being held
    if bar_1_pos_y_desire:
        bar_1_y_pos += 6
    #This ensures that the left bar does not go past the white line (drawn after)
    if bar_1_y_pos <= 55:
        bar_1_y_pos = 55
    #This ensures that the bottom of the left bar does not go past the bottom of the screen
    elif bar_1_y_pos >= 420:
        bar_1_y_pos = 420
    #If the UP key is held which makes the negative y desire true then the position of the right paddle will consitently move 6 pixels up until the UP key is let go
    if bar_2_neg_y_desire:
        bar_2_y_pos -= 6
    #If the DOWN key is held which makes the positive y desire true then the position of the right paddle will consitently move 6 pixels down until the DOWN key is let go
    if bar_2_pos_y_desire:
        bar_2_y_pos += 6
    #This ensures that the right bar does not go past the white line (drawn after)
    if bar_2_y_pos <= 55:
        bar_2_y_pos = 55
    #This ensures that the bottom of the right bar does not go past the bottom of the screen
    elif bar_2_y_pos >= 420:
        bar_2_y_pos = 420      
    #Intro screen visuals 
    if screen_mode == 1:
        screen.fill(WHITE)
        #This is the purple trapezoid that you see in the starting screen
        pygame.draw.polygon(screen,PURPLE, [[300,50],[50,400],[750,400],[500,50]])
        #This renders the PONG text into an image 
        pong_text = font_2.render("PONG",True,BLACK)
        #This displays the PONG text or technically image to the screen
        screen.blit(pong_text,[310,90])
        #This renders the randomly generated number of winning points as an image 
        points = font.render("FIRST TO: " + str(winning_points) + " POINTS WINS!",True,BLACK)
        #This displays that image to the screen
        screen.blit(points,[210,330])
        #This renders my name as an image
        by = font.render("By: Brian Morava 10J",True,BLACK)
        #This displays my name to the screen
        screen.blit(by,[250,430])        
        #Play Button
        #This is the white rectangle play button 
        pygame.draw.rect(screen, WHITE,[340,220,110,60])
        #This renders the PLAY text as an image 
        play = font_3.render("PLAY",True,color)
        #This displays the PLAY text or technically image right above the play button 
        screen.blit(play,[350,224])
        '''The next 56 lines of code change the color of the PLAY text from BLACK to WHITE every second for 33 seconds. Since the color of the button is white this makes it 
        seem as though the words PLAY are flashing.''' 
        if pygame.time.get_ticks() > 3000 and pygame.time.get_ticks() < 4000:
            color = WHITE 
        if pygame.time.get_ticks() > 4000 and pygame.time.get_ticks() < 5000:
            color = BLACK 
        if pygame.time.get_ticks() > 5000 and pygame.time.get_ticks() < 6000:
            color = WHITE  
        if pygame.time.get_ticks() > 6000 and pygame.time.get_ticks() < 7000:
            color = BLACK     
        if pygame.time.get_ticks() > 7000 and pygame.time.get_ticks() < 8000:
            color = WHITE 
        if pygame.time.get_ticks() > 8000 and pygame.time.get_ticks() < 9000:
            color = BLACK  
        if pygame.time.get_ticks() > 9000 and pygame.time.get_ticks() < 10000:
            color = WHITE 
        if pygame.time.get_ticks() > 10000 and pygame.time.get_ticks() < 11000:
            color = BLACK  
        if pygame.time.get_ticks() > 11000 and pygame.time.get_ticks() < 12000:
            color = WHITE 
        if pygame.time.get_ticks() > 12000 and pygame.time.get_ticks() < 13000:
            color = BLACK  
        if pygame.time.get_ticks() > 13000 and pygame.time.get_ticks() < 14000:
            color = WHITE 
        if pygame.time.get_ticks() > 14000 and pygame.time.get_ticks() < 15000:
            color = BLACK  
        if pygame.time.get_ticks() > 15000 and pygame.time.get_ticks() < 16000:
            color = WHITE 
        if pygame.time.get_ticks() > 16000 and pygame.time.get_ticks() < 17000:
            color = BLACK  
        if pygame.time.get_ticks() > 17000 and pygame.time.get_ticks() < 18000:
            color = WHITE                                                     
        if pygame.time.get_ticks() > 18000 and pygame.time.get_ticks() < 19000:
            color = BLACK  
        if pygame.time.get_ticks() > 19000 and pygame.time.get_ticks() < 20000:
            color = WHITE                                                             
        if pygame.time.get_ticks() > 20000 and pygame.time.get_ticks() < 21000:
            color = BLACK                                                                  
        if pygame.time.get_ticks() > 21000 and pygame.time.get_ticks() < 22000:
            color = WHITE 
        if pygame.time.get_ticks() > 22000 and pygame.time.get_ticks() < 23000:
            color = BLACK  
        if pygame.time.get_ticks() > 23000 and pygame.time.get_ticks() < 24000:
            color = WHITE
        if pygame.time.get_ticks() > 24000 and pygame.time.get_ticks() < 25000:
            color = BLACK
        if pygame.time.get_ticks() > 25000 and pygame.time.get_ticks() < 26000:
            color = WHITE
        if pygame.time.get_ticks() > 27000 and pygame.time.get_ticks() < 28000:
            color = BLACK
        if pygame.time.get_ticks() > 28000 and pygame.time.get_ticks() < 29000:
            color = WHITE
        if pygame.time.get_ticks() > 30000 and pygame.time.get_ticks() < 31000:
            color = BLACK
        if pygame.time.get_ticks() > 31000 and pygame.time.get_ticks() < 32000:
            color = WHITE
        if pygame.time.get_ticks() > 32000 and pygame.time.get_ticks() < 33000:
            color = BLACK                   
    #If the screen mode is changed to 2 either by 33 seconds passing or by the player clicking on the play button then the "actual game code" is executed
    if screen_mode == 2:
        '''The program first checks if either player has reached the winning score in which case done is set to true, the loop ends and the game ultimatley finishes. It 
        also moves the pong ball off of the screen because later on the program displays the game screen before the game over screen and the pong ball does not look good in 
        that shot. These 2 lines can be placed at the top or bottom as the buffer or stall implemented down below removes any differences from their 2 possible placements.'''
        if score_a == winning_points or score_b == winning_points:
            done = True
            circle_x_pos = 900  
        #This fills the screen Black whick allows for proper animation of the paddles and the ball
        screen.fill(BLACK)
        #This displays the pong logo between the two scores
        screen.blit(logo,[320,10])
        #This renders the first score as an image, score_a increases every time the ball passes through player 2's paddle (this is programmed later on)   
        score_1 = font.render("Score: " + str(score_a),True,WHITE)
        #This renders the second score as an image, score_b increases every time the ball passes through player 1's paddle (this is programmed later on)
        score_2 = font.render("Score: " + str(score_b),True,WHITE)    
        #This displays player 1's score to the screen
        screen.blit(score_1,[10,5])
        #This displays player 2's score to the screen
        screen.blit(score_2,[640,5])
        #Draws the dotted middle line which bisects the screen (even though the x coordinate of the rectange is only 390 for some reason it looks better than the math calculates) 
        for i in range(20):
            pygame.draw.rect(screen,WHITE,[390,80 * (i + 1),5,40])
        #Draws the horizontal Line which separtes the scores from the bars and prevents the bars or the ball from covering the scores and the pong logo
        for i in range(20):
            pygame.draw.line(screen,WHITE,[0,55],[800,55])        
        '''This animates the pong ball or makes the pong ball move in both the x and y directions as we are constantly adding the x and y speeds to their positions. Adding 
        to both the x and y positions makes the pong ball move diagonally.''' 
        circle_x_pos += circle_x_speed
        circle_y_pos += circle_y_speed
        '''This draws the pong ball to the screen. Converting the x and y positions of the pong ball to integars before we draw it allows us to use decimals for our speed of 
        the pong ball. Even though this speed will be converted to an integar it still affects the speed of the ball because while two speeds can be completely different they
        can still be rounded to the same speed which will either prolong the amount of time that the ball is going at a slow speed (make it slower) or prolong the amount of 
        time that the ball is going at a fast speed (make it faster or keep it fast)'''  
        pygame.draw.circle(screen, WHITE,[int(circle_x_pos),int(circle_y_pos)],10)
        '''If the circle's center is either its radius away from the bottom of the screen or its radius away from the bottom of the horizontal line then this code makes 
        it invert its y direction (through using the speed variable) or makes it go the opposite way (it effectively makes the ball bounce off of the bottom and top parts of 
        the screen)'''
        if circle_y_pos >= 490 or circle_y_pos <= 65:
            circle_y_speed = -circle_y_speed 
        '''If the circle's center is less than or equal to zero (in terms of horizontal distance) than it must have passed player 1's paddle in which case the position of 
        the ball is reset to the center of the screen and player 2's score (score_b) is increased by 1 point.'''
        if circle_x_pos <= 0: 
            circle_y_pos = 250
            circle_x_pos = 400
            score_b += 1
        #Similarly if this is not the case and the circle's center is equal to or past 800 (in terms of horizontal distance) then it must have passed player 2's paddle in which case the position of the ball is reset to the center of the screen and player 1's score (score_a) is increased by 1 point. 
        elif circle_x_pos >= 800:
            circle_y_pos = 250
            circle_x_pos = 400
            score_a += 1
        #Collision of ball and bar 
        #Collision of ball with width of paddles
        '''if the y position of the center of the circle is (about since pong ball is not a perfect circle) its radius lenght away  or less from the y position of the 
        left paddle and is above or on the y position of the paddle and is past the paddles outer side (in terms of horizontal distance) then it must ricochet off the paddle. 
        This makes it go upward (-7 circle_y_speed) as it must be coming from above the paddle due to us comparing the short side on the top of the paddle.''' 
        if  circle_y_pos - bar_1_y_pos >= -11 and circle_y_pos - bar_1_y_pos <= 0 and circle_x_pos <= 35:
            circle_y_speed = -7
        #If this is not the case but the y position of the center of the circle is (about since pong ball is not a perfect circle) below the y position of the left paddle by the length of the paddle plus the length of the ball's radius and is on or below the y position of the paddle plus the length of the paddle (the bottom side of the paddle) and is past the outer side of the paddle (in terms of horizontal distance) then it must ricochet off the paddle. This makes it go downward (7 circle_y_speed) as it must be coming from below the paddle due to us comparing the short side on the bottom of the paddle.   
        elif circle_y_pos - bar_1_y_pos <= 92 and circle_y_pos - bar_1_y_pos >= 80 and circle_x_pos <= 35:
            circle_y_speed = 7
        #The next two lines are the same scenarios except they apply for the right paddle instead of the left one. The basic logic is the same, but the numbers will be different.
        elif circle_y_pos - bar_2_y_pos >= -12 and circle_y_pos - bar_2_y_pos <= 0 and circle_x_pos >= 765:
            circle_y_speed = -7
        elif circle_y_pos - bar_2_y_pos <= 92 and circle_y_pos - bar_2_y_pos >= 80 and circle_x_pos >= 765:
            circle_y_speed = 7    
        #Collision of ball with length of paddles
        '''if the x position of the ball is less than that of the left paddle's top left corner plus the length of the ball's radius and the difference between the two 
        objects (in terms of vertical distance) is between 0 and the length of the paddle then the ball must have hit the paddle. If the ball hits the paddle then it bounces 
        off of it by moving towards the right of the screen (circle_x_speed = 7). As an extra feature the speed at which it moves to the right will increase every time that 
        the ball hits the paddle by a radom number between 0 and 0.3.''' 
        if circle_x_pos <= 35 and circle_y_pos - bar_1_y_pos >= 0 and circle_y_pos - bar_1_y_pos <= 80:
            circle_x_speed = 7 + variable_x_speed 
            variable_x_speed += random.randrange(3) / 10
        #The next two lines are the same scenario except they apply for the right paddle instead of the left one. The basic logic is the same, but the numbers will be different. (e.x circle_x_speed will be negative as well as the variable speed as this is the right paddle so the ball must bounce towards the left which is a decreasing x coordinate amount)   
        elif circle_x_pos >= 765 and circle_y_pos - bar_2_y_pos >= 0 and circle_y_pos - bar_2_y_pos <= 80:
            circle_x_speed = -7 - variable_x_speed 
            variable_x_speed += random.randrange(3) / 10
        '''These two lines of code draw the two bars on the screen. Surronding int around the bar y positions is currently unnecessary but could be useful if I want to change 
        their speeds by non integar values'''
        pygame.draw.rect(screen, WHITE,[10,int(bar_1_y_pos),15,80])
        pygame.draw.rect(screen, WHITE,[775,int(bar_2_y_pos),15,80])           
    #Updates all of the changes to the screen
    pygame.display.flip()
    #Regulates the flow of movement on the screen to a steady 60 frames per second 
    clock.tick(60)
'''Stalls the program by 0.7 seconds in order for the player to see both of the scores before the game over screen appears, this is were the pong ball does not look nice so 
it gets moved off of the visable screen area (a player has lost at this point since all of this code is outside the while loop)'''
time.sleep(0.7)
#The GAME OVER screen starts with filling the screen to white
screen.fill(WHITE)
#The GAME OVER title is rendered as an image, is smoothed, and has a font color of purple
over = font.render("GAME OVER",True,PURPLE)
'''if the player 1's score (score_a) is greater than player 2's score (score_b) then the text, Player 1 Won!, is rendered as the winner image with the same font as the 
score font and same purple color as GAME OVER.''' 
if score_a > score_b:
    winner = font.render("Player 1 Won!",True,PURPLE)
    screen.blit(winner,[290,400])
#If player 1 did not win than player 2 must have won since the game only ends when a player has more points than their opponent (or by pressing the x button). If this turns out to be the case than the text, Player 2 Won!, is rendered as the winner image and is displayed to the screen below the GAME OVER text.
else:
    winner = font.render("Player 2 Won!",True,PURPLE)
    screen.blit(winner,[290,400])    
#The GAME OVER text or technically image is displayed on the screen above the winner image
screen.blit(over,[300,200])
#The trophy image is loaded in
trophy = pygame.image.load("trophy.png")
#The tropy image is resized to fit in between the GAME OVER text and the winner text 
trophy = pygame.transform.scale(trophy,(170,100))
#The trophy image is displayed on the screen
screen.blit(trophy,[300,250])
#Draws multiple purple rectangles in order to create a dotted middle line to the left of the trophy (it draws them vertically it is a vertical line)
for i in range(50):
    pygame.draw.rect(screen,PURPLE,[250,10 * (i + 1),5,5])
#Draws multiple purple rectangles in order to create a dotted middle line to the right of the trophy (it draws them vertically it is a vertical line)
for i in range(50):
    pygame.draw.rect(screen,PURPLE,[520,10 * (i + 1),5,5])
#Updates the screen with these new changes 
pygame.display.flip()
#Stalls or buffers the program by 4 seconds in order to sustain the GAME OVER screen after the while loop and main game screen have finished
time.sleep(4)
#Quits out of the program 
pygame.quit()