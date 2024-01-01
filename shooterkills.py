import pygame as pg
import time
import random
pg.font.init()

width,height=1365,785
win=pg.display.set_mode((width,height))
pg.display.set_caption("ShooterKills")

BG=pg.transform.scale(pg.image.load("H:\Python_game\Shooterkills\game\\New folder\Game\Lib\Assets\space_bg.jpg"),(width,height))
player_width=60
player_height=90
player_vel=5

star_width=20
star_height=30
star_vel=5
hit=False

start_time=time.time()
elapsed_time=0
clock =pg.time.Clock()
fon=pg.font.SysFont("comicsans",30)
fan=pg.font.SysFont("Arial Black",100)

def draw(player,elapsed_time,stars):
    win.blit(BG,(0,0))
    time_text=fon.render(f"Time:{round(elapsed_time)}s",1,"green","purple")
    win.blit(time_text,(10,10))
    pg.draw.rect(win,"red",player)
    for star in stars:
        pg.draw.rect(win,"Gold",star)
    pg.display.update()
    
def main():
    run=True
    player=pg.Rect(100, height-player_height,player_width,player_height)
    star_add_increement=2000
    star_count=0
    stars=[]
    hit=False
    
    while run:
        star_count+=clock.tick(60)
        elapsed_time=time.time()-start_time
        
        if star_count>star_add_increement:
            for _ in range(3):
                star_x=random.randint(0,width-star_width)
                star=pg.Rect(star_x,-star_height,star_width,star_height)
                stars.append(star)
            star_add_increement=max(200,star_add_increement-50)
            star_count=0
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
                break
        keys=pg.key.get_pressed()
        if keys[pg.K_a] and player.x-player_vel>=0:
            player.x-=player_vel
        if keys[pg.K_d] and player.x+player_vel+player_width<=width:
            player.x+=player_vel
        if keys[pg.K_w] and player.y-player_vel>=0:
            player.y-=player_vel
        if keys[pg.K_s] and player.y+player_vel+player_height<=height:
            player.y+=player_vel
        if keys[pg.K_q]:
            pg.quit()
            
        for star in stars[:]:
            star.y+=star_vel
            if star.y>height:
                stars.remove(star)
            elif star.y+star.height>=player.y and star.colliderect(player):
                stars.remove(star)
                hit=True
                break
        
        if hit:
            lost_text=fan.render("Game Over",1,"red")
            win.blit(lost_text,(width/2-lost_text.get_width()/2,height/2-lost_text.get_height()/2))
            pg.display.update()
            pg.time.delay(4000)
            break
            
        draw(player,elapsed_time,stars)
    pg.quit()

if __name__=="__main__":
    main()