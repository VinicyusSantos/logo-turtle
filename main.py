import curses
import modeselector
import creditos
import comandos

def menuzeira(va):
    if va == True:

        menu = ['Iniciar Jogo', 'Créditos' , 'Comandos', 'Sair']
        def print_menu(stdscr, selected_row_idx):
            stdscr.clear()
            altura, largura = stdscr.getmaxyx()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
  
            for idx, row in enumerate(menu):
                x = largura//2 - len(row)//2
                y = altura//2 - len(menu)//2 + idx
                if idx ==  selected_row_idx:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, row)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, row)
            

                stdscr.refresh()

        def main(stdscr):
            curses.curs_set(0)
            current_row_idx = 0
            print_menu(stdscr, current_row_idx)
            while True:
                key = stdscr.getch()
                stdscr.clear()
                if key in [curses.KEY_UP, ord('w')] and current_row_idx > 0:
                    current_row_idx -= 1
                elif key in [curses.KEY_DOWN, ord('s')] and current_row_idx < len(menu) -1:
                    current_row_idx += 1
                elif key == curses.KEY_ENTER or key in [10,13] and current_row_idx == 0:
                    modeselector.inicio(True)
                elif key == curses.KEY_ENTER or key in [10,13] and current_row_idx == 1:
                    creditos.call_credit(True)
                elif key == curses.KEY_ENTER or key in [10,13] and current_row_idx == 2:
                    comandos.call_comandos(True)
                elif key == curses.KEY_ENTER or key in [10,13] and current_row_idx == 3:
                    exit()

                print_menu(stdscr, current_row_idx)
                stdscr.refresh()

        curses.wrapper(main)
menuzeira(True)
