import curses

def inicio_modo(modo):
    if (modo == 1):
        def modo_1(stdscr):
            # CONFIGURAÇÕES INICIAIS
            curses.curs_set(2)
            curses.nocbreak()
            curses.echo()
            
            # CORES
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

            RB = curses.color_pair(1)
            CB = curses.color_pair(2)
            YB = curses.color_pair(3)
            GB = curses.color_pair(4)
            MB = curses.color_pair(5)

        
            # CRIA JANELA
            altura, largura = stdscr.getmaxyx()
            janela_altura, janela_largura = altura-2, largura-1
        
            wincom = curses.newwin(janela_altura, janela_largura)

            wincom.box()
            wincom.bkgd(' ', curses.color_pair(1)) 
            wincom.refresh()
            

            # POSIÇÃO INICIAL
            max_y, max_x = stdscr.getmaxyx()
            y, x = max_y // 2, max_x // 2

            # MOVIMENTAÇÃO POR COMANDOS
            while True:

                
                wincom.addstr(0, 0, "Jogando logo turtle!") 

                # CAIXA DE TEXTO
                texto_y, texto_x = altura-2, 1
                texto_largura = largura-20
                texto_janela = curses.newwin(1, texto_largura, texto_y, texto_x)

                # ATUALIZA CAIXA DE TEXTO
                texto_janela.clear()
                texto_janela.addstr("Digite um comando: ", GB)
                texto_janela.refresh()
                texto = texto_janela.getstr(0, len("Digite um comando:"), texto_largura).decode("utf-8")

                
                
                if texto.startswith("m "):
                    direction = (texto.split(" ")[1])
                    num_passos = (texto.split(" ")[2])

                    if num_passos.isdigit():
                        distance = int(num_passos)

                        try:
                            if direction == "a":
                                if x - distance >= 1:
                                    for i in range(distance):
                                        wincom.addstr(y, x -i, "•", MB)
                                    x -= distance
                            elif direction == "d":
                                if x + distance < janela_largura - 1:
                                    for i in range(distance):
                                        wincom.addstr(y, x + i, "•", MB)
                                    x += distance
                            elif direction == "w":
                                if y - distance >= 1:
                                    for i in range(distance):
                                        wincom.addstr(y - i, x, "•", YB)
                                    y -= distance
                            elif direction == "s":
                                if y + distance < janela_altura - 1:
                                    for i in range(distance):
                                        wincom.addstr(y + i, x, "•", YB)
                                    y += distance
                            elif direction == "e":
                                if y - distance >= 1 and x + distance < janela_largura - 1:
                                    for i in range(distance):
                                        wincom.addstr(y - i , x + i, "•", GB)
                                    y -= distance
                                    x += distance
                            elif direction == "q":
                                if y - distance >= 1 and x - distance >= 1:
                                    for i in range(distance):
                                        wincom.addstr(y - i , x - i, "•", CB)
                                    y -= distance
                                    x -= distance
                            elif direction == "x":
                                if y + distance < janela_altura - 1 and x + distance < janela_largura - 1:
                                    for i in range(distance):
                                        wincom.addstr(y + i, x + i, "•", CB)
                                    y += distance
                                    x += distance
                            elif direction == "z":
                                if y + distance < janela_altura - 1 and x - distance >= 1:
                                    for i in range(distance):
                                        wincom.addstr(y + i, x - i , "•", GB)
                                    y += distance
                                    x -= distance
                            wincom.addstr(y,x, '@')
                        except:
                            wincom.addstr(0, 0, "Comando inválido!!!!", curses.A_REVERSE)
                    else:   
                       wincom.addstr(0, 0, "Comando inválido!!!!", curses.A_REVERSE)
                       wincom.refresh()
                elif texto.startswith("limpar"):
                    wincom.clear()
                    wincom.box()
                    wincom.addstr(y,x, '@')
                    wincom.addstr(0, 0, "Jogando logo turtle!")
                elif texto.startswith('sair'):
                 import main
                 main.menuzeira(True)
                elif texto.startswith('resetar'):
                    wincom.addstr(y,x, ' ')
                    x, y = max_x // 2, max_y // 2
                    wincom.addstr(y,x, '@')
                else:
                    wincom.addstr(0, 0, "Comando inválido!!!!", curses.A_REVERSE)
                wincom.refresh()
                

        curses.wrapper(modo_1)
    
    elif (modo == 2):
        def modo_2(stdscr):
            stdscr.clear()
            stdscr.refresh()
            #CONFIGURAÇÕES INICIAIS
            # POSIÇÃO INICIAL
            max_y, max_x = stdscr.getmaxyx()
            y, x = max_y // 2, max_x // 2
            curses.curs_set(0)
       
           
            # CORES
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

            RB = curses.color_pair(1)
            CB = curses.color_pair(2)
            YB = curses.color_pair(3)
            GB = curses.color_pair(4)
            MB = curses.color_pair(5)


            # CRIA JANELA
            altura, largura = stdscr.getmaxyx()
            janela_altura, janela_largura = altura-1, largura-1
        
            winbind = curses.newwin(janela_altura, janela_largura)

            winbind.border()
            winbind.bkgd(' ', curses.color_pair(1)) 
            winbind.refresh()

            #MOVIMENTAÇÃO #MODO 2
            while True:

            

                # LIMPA AVISO DE COMANDO INVÁLIDO
                winbind.addstr(0, 0, "Jogando logo turtle!") 

                key = stdscr.getkey()
                if key == "a":
                    if(x > 1):
                        winbind.addstr(y,x,"•", MB)
                        x -= 1
                    if(x < 1):
                        x = x
                elif key == "d":
                    if(x >= 1 and x < janela_largura-2):
                        winbind.addstr(y,x,"•", MB)
                        x += 1
                elif key == "w":
                    if(y > 1):
                        winbind.addstr(y,x,"•", YB)
                        y -= 1
                elif key == "s":
                    if y < janela_altura - 2:
                        winbind.addstr(y,x,"•", YB)
                        y += 1
                elif key == "e":
                    if y > 1 and x < janela_largura - 2:
                        winbind.addstr(y,x,"•",  GB)
                        y -= 1
                        x += 1
                elif key == "q":
                    if y > 1 and x > 1:
                        winbind.addstr(y,x,"•", CB)
                        y -= 1
                        x -= 1
                elif key == "x":
                    if y < janela_altura- 2 and x < janela_largura - 2:
                        winbind.addstr(y,x,"•", CB)
                        y += 1
                        x += 1
                elif key == "z":
                    if y < janela_altura - 3 and x > 1:
                        winbind.addstr(y,x,"•", GB)
                        y += 1
                        x -= 1
                elif key == "l":
                    winbind.clear()
                    winbind.border()
                    winbind.addstr(y,x, "@")
                    winbind.addstr(0, 0, "Jogando logo turtle!")
                elif key == "r":
                    winbind.addstr(y,x, ' ')
                    x,y = max_x // 2, max_y // 2
                elif key == 'm':
                    import main
                    main.menuzeira(True)
                else:
                    winbind.addstr(0, 0, "Comando inválido!!!", curses.A_REVERSE)
                winbind.addstr(y,x, "@")
                winbind.refresh()

        curses.wrapper(modo_2) 