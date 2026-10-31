import pygame

pygame.init()


screen = pygame.display.set_mode((1536, 1024))

pygame.display.set_caption("Bad Dino")
icon_image = pygame.image.load("icon.png")
pygame.display.set_icon(icon_image) 

start_fon = pygame.image.load("start_fon.jfif")
start_fon = pygame.transform.scale(start_fon,(1536, 1024))
start = pygame.image.load("button_start.png") # завантажуємо зображення кнопки "Почати гру"
start = pygame.transform.scale(start,(1000,700)) # змінюємо розмір зображення кнопки на 150 на 100 пікселів
rect_start = start.get_rect()# отримуємо хітбокс, який відповідає розміру зображення кнопки
rect_start.center = (768,512)# розміщуємо хітбокс по центру вікна

nepacetko = pygame.image.load("nepacetko.png")
nepacetko = pygame.transform.scale(nepacetko, (175, 175)) #налаштування розмірів непацєтка
pacetko = pygame.image.load("pacetko.webp")
pacetko = pygame.transform.scale(pacetko, (150, 150)) #налаштування розміру пацєтка
petarda = pygame.image.load("petarda.webp")
petarda = pygame.transform.scale(petarda, (150, 150))

#супер класний фон
fon = pygame.image.load("fon(2).png")
bg_width = fon.get_width()

#Мега ульра шрифт
font = pygame.font.SysFont("Arial",70)

over = pygame.image.load("game_over.png")

#Супер класна чудова мкзичка
pygame.mixer.music.load("pacesong.mp3")
#pygame.mixer.music.play()

#хітбокс центру нашого любімчика
rect_pacetko_img = pacetko.get_rect()
rect_pacetko_img.center = (100,640)

#хітбокс любімчика
rect_pacetko = pygame.Rect(100, 640, 125, 125)
rect_pacetko.center = rect_pacetko_img.center

#наш центр антагоніста
nepacetko_rect_img = nepacetko.get_rect()
nepacetko_rect_img.bottomleft = (2300,400)

#хітбокс антагоніста
nepacetko_rect= pygame.Rect(2300, 400, 125, 125)
nepacetko_rect.center = nepacetko_rect_img.center

#помічник антагоніста
petarda_rect = petarda.get_rect()
petarda_rect.bottomleft = (1700,720)

x_fon = 0
clock = pygame.time.Clock()
game = 0
vverh = 0 
is_jump = False
score = 0
game_start = 1
game_finish = 0
speed = 10
score_speed = 0

#старт
while game_start:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: # якщо користувач закриває вікно
            game_start = 0 # закриваємо екран початку гри
        if ev.type == pygame.MOUSEBUTTONDOWN:# якщо користувач натискає на кнопку миші
            x,y = pygame.mouse.get_pos()# отримуємо координати курсора миші
            if rect_start.collidepoint(x,y):# якщо координати курсора миші знаходяться всередині хітбокса кнопки "Почати гру"
                game_start = 0# закриваємо екран початку гри
                game = 1# запускаємо гру


    screen.blit(start_fon, (0, 0))           
    screen.blit(start,rect_start)# малюємо зображення кнопки "Почати гру" на екрані, використовуючи його хітбокс для позиціювання
    pygame.display.update()# оновлюємо екран, щоб відобразити зміни


while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = 0
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE and not is_jump:
                vverh = -26
                is_jump = True
    if is_jump:
        rect_pacetko.y+=vverh
        vverh+=1
        if rect_pacetko.bottom >=700:
            rect_pacetko.bottom = 700
            is_jump = False
    if rect_pacetko.colliderect(petarda_rect):
        game = 0
        game_finish =1
    if rect_pacetko.colliderect(nepacetko_rect):
        game = 0
        game_finish = 1
    petarda_rect.x -=speed
    
    if petarda_rect.x < -100:
        petarda_rect.x = 1536
        
        if nepacetko_rect.x < -100:
            
            nepacetko_rect.x = 2500
        
    nepacetko_rect.x -=speed

    #це тобі не треба
    #if nepacetko_rect.x < -100:
        #nepacetko_rect.x = 2500
        
    x_fon -=speed
    score+=1

    #швидкість гри
    score_speed+=1
    if score_speed >= 200:
        speed+=1
        score_speed = 0
    
    #Ваші очки(не ті шо ти вдягаєш від сонця)
    score_text = font.render(f"Очки:{score}", True,  (0,0,0))
    
    if x_fon < -bg_width:
        x_fon = 0
    screen.blit(fon, (x_fon, 0)) #прикріплення фону                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #какашк
    screen.blit(fon, (x_fon +bg_width, 0 )) #прикріплення фону
    screen.blit(pacetko,rect_pacetko) #прикріплення пацєтка
    screen.blit(nepacetko, nepacetko_rect)
    screen.blit(petarda, petarda_rect)
    screen.blit(score_text,(0,0))

    pygame.display.update()
    clock.tick(50)
    
while game_finish:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_finish = 0

#тобі це потрібно якщо ти ПРОГРАВ!!!
    screen.fill((255,255,255))
    finish_text = font.render(f"Game Over", True,  (0,0,0))
    #screen.blit(finish_text,(600,450))
    screen.blit(over,(300, 0))
    screen.blit(score_text,(600,600))
    pygame.display.update()
    
#Пока
pygame.quit()

