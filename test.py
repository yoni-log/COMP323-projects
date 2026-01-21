import pygame as pg

def main() -> None:
    pg.init()
    w, h = 960, 540
    screen = pg.display.set_mode((w, h))
    pg.display.set_caption("pg window")

    clk = pg.time.Clock()

    running = True
    while running:
        clk.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        pg.draw.rect(
            surface=(
                (10, 10),
                flags=0,
                depth=0,
                masks=None
            ), 
            color=(
                128,
                128,
                250
            ), 
            rect=(
                10,
                10,
                10,
                10
            ))
        pg.display.flip()

if __name__ == '__main__':
    main()