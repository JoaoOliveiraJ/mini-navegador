import os

MSG_ERROR = 'not exist tag body, html invalid'


POSITION = {
    'init_body': None,
    'finally_body': None,
    'position_h1_value': []
}

value_h1 = []

def Parser (tokens_lecture):

    for index, tokens in enumerate(tokens_lecture):
        #print(tokens_lecture[0])

        if tokens == '<body>\n':
            #print(f"Encontrou na posição {tokens_lecture.index(tokens)}")
            POSITION['init_body'] = tokens_lecture.index(tokens)


        elif tokens == '</body>':
            #print(f"Encontrou na posição {tokens_lecture.index(tokens)}")
            POSITION['finally_body'] = tokens_lecture.index(tokens)

        elif tokens == '<h1>\n':

            value_h1.append(index + 1)
            POSITION['position_h1_value'] = value_h1




    print('a,', POSITION['init_body'])
    print('b', POSITION['position_h1_value'])







def Ler ():
    filename = 'index.html'
    filecontent = list()

    if not os.path.isfile(filename):
        print('error open file')

    fileopen = open(filename, 'r')

    for fileline in fileopen:
        filecontent.append(fileline.replace(" ", ''))

    print(Parser(filecontent))
    print(filecontent)


    def Written_Text(tokens):
        import pygame as pg

        pg.init()

        # use a (r, g, b) tuple for color
        yellow = (255, 255, 0)

        # create the basic window/screen and a title/caption
        # default is a black background
        screen = pg.display.set_mode((1240, 680))
        pg.display.set_caption("Text adventures with Pygame")
        # pick a font you have and set its size
        myfont = pg.font.SysFont("Comic Sans MS", 30)
        # apply it to text on a label
        for value_h1_wrriten in value_h1:
            print(value_h1)
            testjoao = tokens[value_h1_wrriten].replace("\n", "")
            label = myfont.render(f"{testjoao}", 1, yellow)
            # put the label object on the screen at point x=100, y=100
            screen.blit(label, (100, 100))
            # show the whole thing
            pg.display.flip()

            if value_h1_wrriten > 1:
                del value_h1[0]
                print(value_h1)
                testjoao = tokens[value_h1[0]].replace("\n", "")
                label = myfont.render(f"{testjoao}", 1, yellow)
                # put the label object on the screen at point x=100, y=100
                screen.blit(label, (100 * 1.5, 100 * 1.5))
                # show the whole thing
                pg.display.flip()


            # event loop
        while True:
            for event in pg.event.get():
                # exit conditions --> windows titlebar x click
                if event.type == pg.QUIT:
                    raise SystemExit


    Written_Text(filecontent)






