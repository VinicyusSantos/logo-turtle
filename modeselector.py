import curses


def inicio(vb):
    if vb == True:
        def modoselect(stdscr):            
                curses.curs_set(1)
                curses.nocbreak()
                curses.echo()

                #cores
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
                curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
              
                RB = curses.color_pair(1)
                GB = curses.color_pair(2)

                max_y, max_x = stdscr.getmaxyx()
                y, x = max_y // 2, max_x // 2



                # CRIA JANELA
                altura, largura = stdscr.getmaxyx()
                janela_altura, janela_largura = altura-2, largura-1
            
                window = curses.newwin(janela_altura, janela_largura, 0, 0)

                window.box()
                window.bkgd(' ', curses.color_pair(1)) 
                window.refresh()
           
                # CAIXA DE TEXTO
                texto_y, texto_x = y-2, 2
                texto_largura, texto_altura = largura-6, y
                texto_janela = curses.newwin(texto_altura, texto_largura, texto_y, texto_x)
                
                # ATUALIZA CAIXA DE TEXTO

                while True:

                    texto_janela.clear()
                    texto_janela.addstr("Digite o modo [1],[2]: ", GB)
                    texto_janela.refresh()
                    recebido = texto_janela.getstr(0, len("Digite o modo [1],[2]: "), texto_largura).decode("utf-8")

                    if recebido.isdigit():
                        gamemode = int(recebido)

                        window.clear()
                        texto_janela.clear()
                        import game
                        game.inicio_modo(gamemode)
                    else:
                        window.addstr(0, 0, "[Comando inválido! Tente 1 ou 2]", curses.A_REVERSE)
                        window.refresh()
                
        curses.wrapper(modoselect)


