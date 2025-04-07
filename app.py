from tkinter import *
import datetime
import sys

sys.set_int_max_str_digits(2100000000)

def estimated_time(time, P, val):
    initTime = datetime.datetime.time(time)
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
    
    return time_estimated

janela = Tk()
janela.geometry(f'{1100}x{580}')
janela.title("app")
janela.configure(bg='#1a1a1a')

def login_event(event):
    if userEntry.get() and passEntry.get():  # Check both fields have content
        mainWin()
    else:
        error_label.config(text="Por favor, preencha ambos os campos")

def window_quit(win):
    win.quit()
    win.destroy()
        
def mainWin():
    main = Tk()
    main.geometry(f'{1100}x{580}')
    main.configure(bg='#1a1a1a')
    window_quit(janela)

    # Configuração da grade principal
    main.columnconfigure(0, weight=0, minsize=180)  # Sidebar fixa com largura mínima
    main.columnconfigure(1, weight=1)  # Conteúdo expansível
    main.rowconfigure(0, weight=0)  # Linha do título
    main.rowconfigure(1, weight=1)  # Linha do conteúdo dinâmico

    # Sidebar à esquerda
    sidebar = Frame(main, bg='#262626', width=180)
    sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
    sidebar.grid_propagate(False)  # Impede que widgets filhos alterem o tamanho
    
    binario = Button(sidebar, text="DECIMAL → BINÁRIO", width=20, height=1, command=lambda: binary(content_frame))
    binario.grid(row=1, padx=10, pady=10)
    
    decbinario = Button(sidebar, text="BINÁRIO → DECIMAL", width=20, height=1, command=lambda: decBinary(content_frame))
    decbinario.grid(row=2, padx=10, pady=10)

    primebut = Button(sidebar, text="PRIMO", width=10, height=1, command= lambda: prime(content_frame))
    primebut.grid(row=3, padx=10, pady=10)

    merPrimebut = Button(sidebar, text="PRIMO DE MERSENNE", width=20, height=1, command= lambda: mersenePrime(content_frame))
    merPrimebut.grid(row=4, padx=10, pady=10)

    # Título centralizado no topo
    title_frame = Frame(main, bg="#1a1a1a")
    title_frame.grid(row=0, column=1, sticky="new")
    mainmsg = Label(title_frame, text='Menu de Operações', bg='#1a1a1a', fg='green', font=('arial', 28))
    mainmsg.pack(pady=10)

    # Área de conteúdo à direita
    content_frame = Frame(main, bg="#1a1a1a")
    content_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    # Add keyboard shortcuts for switching panels
    main.bind("1", lambda e: binary(content_frame))
    main.bind("2", lambda e: decBinary(content_frame))
    main.bind("3", lambda e: prime(content_frame))
    main.bind("4", lambda e: mersenePrime(content_frame))
    
    main.mainloop()


def binary(content_frame):
    # Limpa widgets antigos antes de adicionar novos
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Cria e atualiza o título da operação
    current_operation = Label(content_frame, text="Operação: Decimal → Binário", bg='#1a1a1a', fg='green', font=('arial', 18))
    current_operation.grid(pady=10)

    # Campo de entrada
    valEntry = Entry(content_frame, font=('roboto', 18), bg='#333333', fg='green')
    valEntry.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

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
    btncalc.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
    valEntry.bind('<Return>', lambda event: calcBin())

    # Campo de saída
    output = Label(content_frame, font=('roboto', 18), text='', bg='#333333', fg='green')
    output.grid(row=2, column=0, columnspan=2, padx=10, pady=10,  sticky="ew")

    # Label de tempo de execução
    tempo = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    tempo.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=1)

def decBinary(content_frame):
    # Limpa widgets antigos antes de adicionar novos
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Cria e atualiza o título da operação
    current_operation = Label(content_frame, text="Operação: Binário → Decimal", bg='#1a1a1a', fg='green', font=('arial', 18))
    current_operation.grid(pady=10)

    # Campo de entrada
    valEntry = Entry(content_frame, font=('roboto', 18), bg='#333333', fg='green')
    valEntry.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    def calc():
        try:
            val = (valEntry.get())
            decNum = 0
            initime = datetime.datetime.now()
            if(val.isdigit() and all(c in '01' for c in val)):
                    valstr = val[::-1]
                    for i in range(len(valstr)):
                        decNum += int(valstr[i]) * (2**i)
                    output.config(text=str(decNum))
                    endtime = datetime.datetime.now()
                    tempo.config(text=f'Tempo de execução: {endtime - initime}')
            else: 
                    pass

        except ValueError:
            output.config(state='normal')
            output.delete(0, END)
            output.insert(0, "Entrada inválida")
            output.config(state='disabled')

    # Botão de cálculo
    btncalc = Button(content_frame, font=("roboto", 18), text="Converter", command=calc)
    btncalc.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
    valEntry.bind('<Return>', lambda event: calc())

    # Campo de saída
    output = Label(content_frame, font=('roboto', 18), text='', bg='#333333', fg='green')
    output.grid(row=2, column=0, columnspan=2, padx=10, pady=10,  sticky="ew")

    # Label de tempo de execução
    tempo = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    tempo.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=1)


def prime(content_frame):
    # Limpa widgets antigos antes de adicionar novos
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Cria e atualiza o título da operação
    current_operation = Label(content_frame, text="Operação: Buscar Primo", bg='#1a1a1a', fg='green', font=('arial', 18))
    current_operation.grid(pady=10)
        
    valEntry = Entry(content_frame, font=('roboto', 18), bg='#333333', fg='green')
    valEntry.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
    
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
    btn.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
    valEntry.bind('<Return>', lambda event: simpleprime())

    # Campo de saída
    output = Label(content_frame, font=('roboto', 18), text='', bg='#333333', fg='green')
    output.grid(row=2, column=0, columnspan=2, padx=10, pady=10,  sticky="ew")

    # Label de tempo estimado
    queue = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    queue.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    # Label de processamento
    processamento = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    processamento.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    # Label de tempo de execução
    tempo = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    tempo.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=1)

def mersenePrime(content_frame):
    # Limpa widgets antigos antes de adicionar novos
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Cria e atualiza o título da operação
    current_operation = Label(content_frame, text="Operação: Buscar Primo de Mersenne", bg='#1a1a1a', fg='green', font=('arial', 18))
    current_operation.grid(pady=10)
        
    valEntry = Entry(content_frame, font=('roboto', 18), bg='#333333', fg='green')
    valEntry.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
    
    def calculate_mersenne():
        try:
            valE = int(valEntry.get())
            valT = (2**valE)-1
            initime = datetime.datetime.now()
            tenP = int(valT * 0.1)
            threeP = int(valT * 0.3)
            fiveP = int(valT * 0.5)
            sevenP = int(valT * 0.7)
            
            for n in range(1, valT + 1):
                if(n == 1):
                    queue.config(text="Iniciando processamento...")
                    processamento.config(text='0%')
                elif(n == tenP):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, tenP, valT)}')
                    processamento.config(text='10%')
                elif(n == threeP):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, threeP, valT)}')
                    processamento.config(text='30%')
                elif(n == fiveP):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, fiveP, valT)}')
                    processamento.config(text='50%')
                elif(n == sevenP):
                    queue.config(text=f'Tempo estimado: {estimated_time(initime, sevenP, valT)}')
                    processamento.config(text='70%')
                
                if(n == valT):
                    if(valT % n == 0):
                        output.config(text=f"O número 2^{valE}-1 é um primo de Mersenne!")
                        endtime = datetime.datetime.now()
                        processamento.config(text='100%')
                        tempo.config(text=f'Duração: {endtime - initime}')
                        break
                elif(valT % n == 0 and n != 1):
                    output.config(text=f"O número 2^{valE}-1 não é um primo de Mersenne")
                    endtime = datetime.datetime.now()
                    processamento.config(text='100%')
                    tempo.config(text=f'Duração: {endtime - initime}')
                    break
                    
        except ValueError:
            output.config(text="Entrada inválida")

    # Botão de cálculo
    btn = Button(content_frame, font=("roboto", 18), text="Verificar", command=calculate_mersenne)
    btn.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
    valEntry.bind('<Return>', lambda event: calculate_mersenne())

    # Campo de saída
    output = Label(content_frame, font=('roboto', 18), text='', bg='#333333', fg='green')
    output.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Label de tempo estimado
    queue = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    queue.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    # Label de processamento
    processamento = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    processamento.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    # Label de tempo de execução
    tempo = Label(content_frame, font=('roboto', 15), text='', bg='#1a1a1a', fg='green')
    tempo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=1)


login_frame = Frame(janela, bg='#1a1a1a')
login_frame.place(relx=0.5, rely=0.5, anchor='center')

user_label = Label(login_frame, text="Usuário:", font=('roboto', 12), bg='#1a1a1a', fg='green')
user_label.grid(row=0, column=0, padx=10, pady=(10,0), sticky='w')
userEntry = Entry(login_frame, font=('roboto', 18), bg='#333333', fg='green')
userEntry.grid(row=1, column=0, padx=10, pady=(0,10))

pass_label = Label(login_frame, text="Senha:", font=('roboto', 12), bg='#1a1a1a', fg='green')
pass_label.grid(row=2, column=0, padx=10, pady=(10,0), sticky='w')
passEntry = Entry(login_frame, font=('roboto', 18), bg='#333333', fg='green')
passEntry.grid(row=3, column=0, padx=10, pady=(0,10))

error_label = Label(login_frame, text="", fg="red", bg='#1a1a1a')
error_label.grid(row=5, column=0, pady=5)

btn = Button(login_frame, text="Login", command=lambda: login_event(None))
btn.grid(row=4, column=0, pady=20, sticky='ew')
janela.bind("<Return>", login_event)

janela.mainloop()
