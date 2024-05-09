import pygame as pg
pg.display.set_mode((600, 400))
while 1:
    events = pg.event.get()
    print(events)
    for i in events:
        if i.type == pg.QUIT:
            print(pg.QUIT)
            print(i)
            print(i.type)
            pg.quit()

        pg.delay