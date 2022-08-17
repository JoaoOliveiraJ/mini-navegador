import os

MSG_ERROR = 'not exist tag body, html invalid'


POSITION = {
    'init_body': None,
    'finally_body': None
}

def Parser (tokens_lecture):

    for tokens in tokens_lecture:
        print(tokens)

        if tokens == '<body>\n':
            print(f"Encontrou na posição {tokens_lecture.index(tokens)}")
            POSITION['init_body'] = tokens_lecture.index(tokens)
            print(POSITION['init_body'])

        elif tokens == '</body>':
            print(f"Encontrou na posição {tokens_lecture.index(tokens)}")
            POSITION['finally_body'] = tokens_lecture.index(tokens)
            print(POSITION['finally_body'])






def Ler ():
    filename = 'index.html'
    filecontent = list()

    if not os.path.isfile(filename):
        print('error open file')

    fileopen = open(filename, 'r')

    for fileline in fileopen:
        filecontent.append(fileline)

    print(Parser(filecontent))
    print(filecontent)





