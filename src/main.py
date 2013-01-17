import pygame, sys #Distro
import conf, jezz #Self
pygame.init()

drawing_line = False
cursor_direction = 0
collision = False
collision_fill = False

screen = pygame.display.set_mode(conf.size)
#cursor_horizontal = pygame.parse_cursor(conf.horizontal_cursor)

ball = pygame.image.load(conf.ball_sprite)
ballrect = ball.get_rect()
screen.fill(conf.black)
collision_timer = conf.collision_timer
frame_clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
           
    ballrect = ballrect.move(conf.ball_speed)
    if ballrect.left < 0 or ballrect.right > conf.width:
        conf.ball_speed[0] = -conf.ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > conf.height:
        conf.ball_speed[1] = -conf.ball_speed[1]
    
    if collision:
        screen.fill(conf.red)
        collision = False
        collision_fill = True
        
    if collision_fill:
        collision_timer -= 1
        if collision_timer == 0:
            screen.fill(conf.black)
            collision_fill = False

    
    m1, m2, m3 = pygame.mouse.get_pressed()
    if m1:
        drawing_line = True
        direction_determined = False
        mox, moy = pygame.mouse.get_pos()
        to_right = to_left = mox
        to_top = to_bottom = moy
            
    if m3:
        cursor_direction = jezz.determine_cursor_direction(cursor_direction)
        
    #print m1, m2, m3
    
    screen.fill(conf.black)
    if collision:
        collision = False
        screen.fill(conf.black)
        
    if drawing_line:
        if direction_determined == False:
            if cursor_direction == 0:
                to_pos = to_right
                to_neg = to_left
                #pygame.mouse.set_cursor(cursor_horizontal)
                #pygame.mouse.set_cursor(conf.mouse_horizontal_cursor)
            elif cursor_direction == 1:
                to_pos = to_top
                to_neg = to_bottom
                #pygame.mouse.set_cursor(conf.mouse_vertical_cursor)
                #pygame.mouse.set_cursor(cursor_vertical)
            direction_determined = True
            
        drawing_line = jezz.draw_line(drawing_line, cursor_direction, screen, mox, moy, to_pos, to_neg)
        
        to_neg -= conf.line_speed
        to_pos += conf.line_speed
        
        collision = jezz.determine_wall_hit(ballrect, mox, moy, to_pos, to_neg, cursor_direction)
        
        if collision:
            drawing_line = False
            screen.fill(conf.red)
            
    screen.blit(ball, ballrect)
    pygame.display.flip()
    frame_clock.tick(conf.fps)