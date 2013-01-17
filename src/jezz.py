## Python 2.7.2 (x86 32-bit, for use with pygame)

import pygame #Distro
import conf #Self
pygame.init()

def draw_line(drawing_line, cursor_direction, screen, mox, moy, to_pos, to_neg):
    ''' (bool, int, Surface, int, int) -> bool
    Draws line at current mouse click in appropriate direction.
    '''
    
    if cursor_direction == 0:
        pygame.draw.line(screen, conf.white, (mox, moy), (to_pos, moy), conf.line_width)
        pygame.draw.line(screen, conf.white, (mox, moy), (to_neg, moy), conf.line_width)
    elif cursor_direction == 1:
        pygame.draw.line(screen, conf.white, (mox, moy), (mox, to_pos), conf.line_width)
        pygame.draw.line(screen, conf.white, (mox, moy), (mox, to_neg), conf.line_width) 

    #print "TR:", to_right, "TL:", to_left
    if(to_pos >= conf.width and to_neg <= 0):
        pygame.draw.line(screen, conf.black, (0, moy), (conf.width - conf.line_speed, moy), conf.line_width)
        drawing_line = False
        
    return drawing_line

def determine_cursor_direction(direction):
    ''' (int) -> int
    Switches cursor direction, to be used with mouse click 3 (right click).
    Returns direction.
    '''
    
    if direction == 1:
        direction = 0
    elif direction == 0:
        direction = 1
        
    return direction

def determine_wall_hit(ballrect, mox, moy, to_pos, to_neg, cursor_direction):
    ''' (pygame.ballrect, int, int, int, int) -> bool
    Takes in current ball and line position and determines if there's a collision.
    Returns boolean yes/no.
    '''
    
    hit = False
    
    if cursor_direction == 0:
        # Check to see if the ball is on the horizontal line.
        if ballrect.bottom == mox or ballrect.top == mox:
            # See if that line is drawn yet at the space where the ball currently occupies.
            if to_neg < ballrect.left < to_pos or to_neg < ballrect.right < to_pos:
                hit = True
    
    return hit

def compile_cursor(cursor_string):
    pygame.cursors.compile(cursor_string, black='#', white='*')
    
    return None