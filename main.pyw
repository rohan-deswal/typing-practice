import pygame
from time import sleep

pygame.init()

display_width = 700
display_height = 200

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Practice Typing")
clock = pygame.time.Clock()

def text_objects(text, font):
    color = (255,0,0)
    if text == 'type':
        color = (100,100,100)
    textSurface = font.render(text, True,color)
    return textSurface, textSurface.get_rect()
def draw_cursor(rect,color = (255,0,0)):
    pygame.draw.rect(game_display,color,[rect.right,rect.top,2,rect.height])
def message_display(text,x,y,w,h,fr):
    cnt = 0
    if len(text) == 0:
        text = 'type'
        cnt = 1
    if len(text) <= 10:
        size = 100
        cnt = 1
    elif len(text) <= 21:
        size = 50
        cnt = 1
    else:
        text1 = text[:21]
        text2 = text[21:]
        size = 50
        largeText = pygame.font.Font('hmm.ttf',size)
        TextSurf, TextRect = text_objects(text1, largeText)
        TextRect.center = ((x+w/2),(y-size/2+h/2))
        game_display.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(text2, largeText)
        TextRect.center = ((x+w/2),(y+size/2+h/2))
        game_display.blit(TextSurf, TextRect)
        if fr <= 30:
            draw_cursor(TextRect)
    if cnt:
        largeText = pygame.font.Font('hmm.ttf',size)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((x+w/2),(y+h/2))
        game_display.blit(TextSurf, TextRect)
        c = (255,0,0)
        if text == 'type':
            c = (100,100,100)
        if fr <= 30:
            draw_cursor(TextRect,c)
def score_display(count,x,y):
    if count < 10:
        size = 150
    elif count < 100:
        size = 100
        x -= 9
        y += 20 

    font = pygame.font.SysFont(None,size)
    text = font.render(str(count),True,(255,255,0))
    game_display.blit(text,(x,y))
def message_display1(text):
    largeText = pygame.font.Font('hmm.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()

def main_loop():

    my_string = ''

    text_box_width = 600
    text_box_height = 150
    fr = 0
    score = 90
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                elif event.key == pygame.K_RETURN:
                    if my_string == 'abcdefghijklmnopqrstuvwxyz':
                        if score < 99:
                            score += 1
                            my_string = ''
                        else:
                            score = 0
                            my_string = 'Well Done'
                    elif my_string == 'Well Done':
                        my_string = ''
                    else:
                        score = score - 1 if score > 0 else 0
                        my_string = ''
                    
                elif event.key in range(pygame.K_a,pygame.K_z+1,1):
                    if len(my_string) < 26:
                        my_string += chr(event.key)
                elif event.key == pygame.K_SPACE: #debug event
                    if len(my_string):
                        print(my_string)
                    else:
                        print("Empty")
                elif event.key == pygame.K_BACKSPACE: #deletion
                    my_string = my_string[:-1]
        game_display.fill((20,20,20))
        message_display(my_string,(display_width-text_box_width)/8,(display_height-text_box_height)/2,text_box_width,text_box_height,fr)
        score_display(score,text_box_width + (display_width-text_box_width)/4,(display_height-text_box_height))
        pygame.draw.rect(game_display,(220,220,220),[(display_width-text_box_width)/8,(display_height-text_box_height)/2,text_box_width,text_box_height],4)


        fr = (fr + 1)%60
        pygame.display.update()
        clock.tick(60)
main_loop()
