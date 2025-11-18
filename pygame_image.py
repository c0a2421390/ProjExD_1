import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flipped = pg.image.load("fig/pg_bg.jpg")
    bg_img_flipped = pg.transform.flip(bg_img_flipped, True, False)
    bg_img_2 = pg.image.load("fig/pg_bg.jpg")
    kokaton_img = pg.image.load("fig/3.png")
    kokaton_img = pg.transform.flip(kokaton_img, True, False)
    kokaton_rct = kokaton_img.get_rect()
    kokaton_rct.center = 300, 200
    tmr = 0
    bg_val = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kokaton_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:
            kokaton_rct.move_ip(0, 1)
        if key_lst[pg.K_LEFT]:
            kokaton_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:
            kokaton_rct.move_ip(1, 0)

        screen.blit(bg_img, [-bg_val, 0])
        screen.blit(bg_img_flipped, [1600 - bg_val, 0])
        screen.blit(bg_img_2, [3200 - bg_val, 0])
        
        screen.blit(kokaton_img, kokaton_rct)
        pg.display.update()
        tmr += 1
        bg_val += 5
        if bg_val == 3200:
            bg_val = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()