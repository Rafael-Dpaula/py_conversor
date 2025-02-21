from tkinter import *
import datetime
import sys

sys.set_int_max_str_digits(2100000000)

def estimated_time(time, P, val):
    initTime = datetime.datetime.time(time)
    #print(f'---------the init time is: ->{initTime}')
    if(int(datetime.datetime.now().strftime("%M")) > int(initTime.strftime("%M"))):
        min_passed = (int(datetime.datetime.now().strftime("%M")) - int(initTime.strftime("%M")))
    else:
        min_passed = (int(initTime.strftime("%M")) - int(datetime.datetime.now().strftime("%M")))
    if(int(datetime.datetime.now().strftime("%H")) > int(initTime.strftime("%H"))):
        hour_passed = (int(datetime.datetime.now().strftime("%H")) - int(initTime.strftime("%H")))
    else:
        hour_passed = (int(initTime.strftime("%H")) - int(datetime.datetime.now().strftime("%H")))
    if(int(datetime.datetime.now().strftime("%S")) > int(initTime.strftime("%S"))):
        sec_passed = (int(datetime.datetime.now().strftime("%S")) - int(initTime.strftime("%S")))
    else:
        sec_passed = (int(initTime.strftime("%S")) - int(datetime.datetime.now().strftime("%S")))
    if(int(datetime.datetime.now().strftime("%f")) > int(initTime.strftime("%f"))):
        milisec_passed = (int(datetime.datetime.now().strftime("%f")) - int(initTime.strftime("%f")))
    else:
        milisec_passed = (int(initTime.strftime("%f")) - int(datetime.datetime.now().strftime("%f")))

    rest = (val - P)
    
    estimated_min = ((int(rest) * int(min_passed) // int(P)))
    estimated_hour = ((int(rest) * int(hour_passed) // int(P)))
    estimated_sec = ((int(rest) * int(sec_passed) // int(P)))
    estimated_milisec = ((int(rest) * int(milisec_passed) // int(P)))
    
    if(estimated_sec % 60 >= 1):
        estimated_min = estimated_min + (estimated_sec // 60)
        estimated_sec = estimated_sec % 60
    elif(estimated_min % 60 >= 1):
        estimated_hour = estimated_hour + (estimated_min // 60)
        estimated_min = estimated_min % 60
    elif(estimated_milisec % 1000 >= 1):
        estimated_sec = estimated_sec + (estimated_milisec // 1000)
        estimated_milisec = estimated_milisec % 1000
    
    
    if(estimated_hour <= 10):
        estimated_hour = int(f'0{estimated_hour}')
    elif(estimated_min <= 10):
        estimated_min = int(f'0{estimated_min}')
    elif(estimated_sec <= 10):
        estimated_sec = int(f'0{estimated_sec}')
    elif(estimated_milisec <= 10):
        estimated_milisec = int(f'0{estimated_milisec}')
    
    time_estimated = (f'{estimated_hour}h:{estimated_min}m:{estimated_sec}.{estimated_milisec}s')
    
    print(f'The estimated time is: {time_estimated}')
    return time_estimated

janela = Tk()
janela.geometry(f'{1100}x{580}')
janela.title("app")
janela.configure(bg='#1a1a1a')

def login_event(event):
    mainWin()

def window_quit(win):
    win.quit()
    win.destroy()
        
def mainWin():
    main = Tk()
    main.geometry(f'{1100}x{580}')
    main.configure(bg='#1a1a1a')
    window_quit(janela)

    # Configuração da grade principal
    main.columnconfigure(0, weight=0)  # Sidebar fixa
    main.columnconfigure(1, weight=1)  # Conteúdo expansível
    main.rowconfigure(0, weight=0)  # Linha do título
    main.rowconfigure(1, weight=1)  # Linha do conteúdo dinâmico

    # Sidebar à esquerda
    sidebar = Frame(main, bg='#262626', width=300)
    sidebar.grid(row=0, column=0, rowspan=2, sticky="nsw")
    
    binario = Button(sidebar, text="BINÁRIO", width=10, height=1, command=lambda: binary(content_frame))
    binario.grid(row=1, padx=10, pady=10)
    
    primebut = Button(sidebar, text="PRIMO", width=10, height=1, command= lambda: prime(content_frame))
    primebut.grid(row=2, padx=10, pady=10)

    # Título centralizado no topo
    title_frame = Frame(main, bg="#1a1a1a")
    title_frame.grid(row=0, column=1, sticky="new")
    mainmsg = Label(title_frame, text='Menu de Operações', bg='#1a1a1a', fg='green', font=('arial', 28))
    mainmsg.pack(pady=10)

    # Área de conteúdo à direita
    content_frame = Frame(main, bg="#1a1a1a")
    content_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    main.mainloop()


def binary(content_frame):
    # Limpa widgets antigos antes de adicionar novos
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Campo de entrada
    valEntry = Entry(content_frame, font=('roboto', 18), bg='#333333', fg='green')
    valEntry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    def calcBin():
        binNum = ''
        try:
            val = int(valEntry.get())
            result = int(val)
            
            initime = datetime.datetime.now()
            if(str(val).isdigit()):
                if (val > 1):
                    while (result != 1):
                        binNum = binNum + str((result % 2))
                        if (result // 2 == 1):
                            binNum = binNum + str((result // 2))
                            break
                        else: 
                            result = result // 2
                    endtime = datetime.datetime.now()
                    output.config(text=f'{binNum[::-1]}')
                    tempo.config(text=f'Tempo de execução: {endtime - initime}')
                elif (val == 0): 
                    binNum = '0'
                    endtime = datetime.datetime.now()
                    output.config(text=f'{binNum[::-1]}')
                    tempo.config(text=f'Tempo de execução: {endtime - initime}')
                elif (val == 1):
                    binNum = '1'
                    endtime = datetime.datetime.now()
                    output.config(text=f'{binNum[::-1]}')
                    tempo.config(text=f'Tempo de execução: {endtime - initime}')
            else: 
                output.config(text=f'ERROR: Invalid Input...')

        except ValueError:
            output.config(state='normal')
            output.delete(0, END)
            output.insert(0, "Entrada inválida")
            output.config(state='disabled')

    # Botão de cálculo
    btncalc = Button(content_frame, font=("roboto", 18), text="Converter", command=calcBin)
    btncalc.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    # Campo de saída
    output = Label(content_frame, font=('roboto', 18), text='', bg='#333333', fg='green')
    output.grid(row=1, column=0, columnspan=2, padx=10, pady=10,  sticky="ew")

    # Label de tempo de execução
    tempo = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    tempo.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=1)

def prime(content_frame):
    # Limpa widgets antigos antes de adicionar novos
    for widget in content_frame.winfo_children():
        widget.destroy()
        
    valEntry = Entry(content_frame, font=('roboto', 18), bg='#333333', fg='green')
    valEntry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
    
    def simpleprime():
        val = int(valEntry.get())
        initime = datetime.datetime.now()
        start = (val * (1/100))
        tenP = int(val * 0.1)
        threeP = int(val * 0.3)
        fiveP = int(val * 0.5)
        sevenP = int(val * (70/100))
        if(str(val).isdigit()):
            for n in range(1, int(val) + 1):
                if(n == int(start)):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, start, val)}')
                    processamento.config(text='0%')
                elif(n == int(tenP)):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, tenP, val)}')
                    processamento.config(text='10%')
                elif(n == int(threeP)):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, threeP, val)}')
                    processamento.config(text='30%')
                elif(n == int(fiveP)):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, fiveP, val)}')
                    processamento.config(text='50%')
                elif(n == int(sevenP)):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, sevenP, val)}')
                    processamento.config(text='70%')
                if(n == int(val)):
                    ##print('test1 pass')
                    if(val % n == 0 and val % 1 == 0):
                        output.config(text=f"O número {val} escolhido é Primo.")
                        endtime = datetime.datetime.now()
                        processamento.config(text='100%')
                        tempo.config(text=f'Duração: {endtime - initime}')
                        break
                elif(val % n == 0 and n != 1):
                    output.config(text=f"O número {val} escolhido não é Primo.")
                    endtime = datetime.datetime.now()
                    processamento.config(text='100%')
                    tempo.config(text=f'Duração: {endtime - initime}')
                    break
        else:
            processamento.config(text='ERROR: Invalid Input...')

    # Botão de cálculo
    btn = Button(content_frame, font=("roboto", 18), text="Converter", command=simpleprime)
    btn.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    # Campo de saída
    output = Label(content_frame, font=('roboto', 18), text='', bg='#333333', fg='green')
    output.grid(row=1, column=0, columnspan=2, padx=10, pady=10,  sticky="ew")

    # Label de tempo estimado
    queue = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    queue.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    # Label de processamento
    processamento = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    processamento.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    # Label de tempo de execução
    tempo = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    tempo.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=1)



btn = Button(janela, text="Apertar", command=mainWin)
btn.pack()
janela.bind("<Return>", login_event)

janela.mainloop()
