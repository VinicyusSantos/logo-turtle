import curses

def call_credit(vc):
    if vc == True:

        def print_creditos(stdscr):

            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            RB = curses.color_pair(1)
            GB = curses.color_pair(2)

            while True:
                stdscr.clear()
                curses.curs_set(0)
                curses.noecho()
                h, w = stdscr.getmaxyx()
                x = w//2
                y = h//2

                stdscr.addstr(y-10, x - len('Desenvolvedores:')//2, 'Desenvolvedores:',RB)
                stdscr.addstr(y-8, x - len('Marcus Vinicius de França')//2, 'Marcus Vinicius de França',RB)
                stdscr.addstr(y-6, x - len('Maria José Cordeiro de Almeida')//2, 'Maria José Cordeiro de Almeida', RB)
                stdscr.addstr(y-4, x - len('Miguel andrey de barros silva')//2, 'Miguel Andrey de Barros Silva', RB)
                stdscr.addstr(y-2, x - len('Vinicyus Manoel de Freitas Santos')//2, 'Vinicyus Manoel de Freitas Santos', RB)
                stdscr.addstr(y+6, x - len('Clique qualquer tecla para voltar')//2, 'Clique qualquer tecla para voltar')
                stdscr.addstr(y, x - len('Orientador:')//2, 'Orientador:', GB)
                stdscr.addstr(y+2, x - len('Joabe Bezerra de Jesus Júnior')//2, 'Joabe Bezerra de Jesus Júnior', GB)

                stdscr.refresh()
                stdscr.getch()
                import main
                main.menuzeira(True)  
        
    curses.wrapper(print_creditos)