import curses

def call_comandos(vd):
    if vd == True:

        def print_comandos(stdscr):

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
                
                stdscr.addstr(y-14, x - len('Modo de jogo 1:')//2, 'Modo de jogo 1:',RB)
                stdscr.addstr(y-13, x - len('limpar - limpa os desenhos da tela')//2, 'limpar - Limpa os desenhos da tela', RB)
                stdscr.addstr(y-12, x - len('sair - Sai do jogo')//2, 'sair - Sai do jogo', RB)
                stdscr.addstr(y-11, x - len('resetar - volta para a posição inicial')//2, 'resetar - volta para a posição inicial', RB)
                stdscr.addstr(y-10, x - len('Para se movimentar, escreva: M (direção) (distância)')//2, 'Para se movimentar, escreva: M (direção) (distância)', RB)
                stdscr.addstr(y-9, x - len('Direções possíveis: ←a, d→ ,↖q, e↗, w↑, s↓, ↙z, x↘')//2, 'Direções possíveis: ←a, d→ ,↖q, e↗, w↑, s↓, ↙z, x↘', RB)
                stdscr.addstr(y-8, x - len('Exemplo: m w 20')//2, 'Exemplo: m w 20', RB)
                stdscr.addstr(y+9, x - len('Clique qualquer tecla para voltar')//2, 'Clique qualquer tecla para voltar')
                stdscr.addstr(y-2, x - len('Modo de jogo 2:')//2, 'Modo de jogo 2:', GB)
                stdscr.addstr(y-1, x - len('Aperte a tecla l para limpar os desenhos da tela')//2, 'Aperte a tecla l para limpar os desenhos da tela', GB)
                stdscr.addstr(y, x - len('Aperta a tecla m para sair do jogo')//2, 'Aperte a tecla m para sair do jogo:', GB)
                stdscr.addstr(y+1, x - len('Aperte a tecla r para voltar para a posição inicial:')//2, 'Aperte a tecla r para voltar para a posição inicial', GB)
                stdscr.addstr(y+2, x - len('Direções possíveis: ←a, d→ ,↖q, e↗, w↑, s↓, ↙z, x↘')//2, 'Direções possíveis: ←a, d→ ,↖q, e↗, w↑, s↓, ↙z, x↘', GB)

                stdscr.refresh()
                stdscr.getch()
                import main
                main.menuzeira(True)

  
        curses.wrapper(print_comandos)