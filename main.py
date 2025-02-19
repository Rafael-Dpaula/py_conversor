import customtkinter
import psycopg2.extras
import subprocess
import os
import re
import datetime
import sys
sys.set_int_max_str_digits(2100000000)
currentsize = sys.get_int_max_str_digits()

conn = None
try:
    with psycopg2.connect(
        "dbname='py_API'"
        "user='postgres'"
        "password='root'"
        "host='localhost'"
        "port=51120"
    ) as conn:  
        print('conexao bem sucedida')
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
        def select_login():
            query = "SELECT id, email, nickname, ip_login from  login"
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                print(row)
        select_login()
        conn.commit()
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("green")
        window = customtkinter.CTk()
        window.geometry(f"{1100}x{580}")
        window.title("app")
        login_text = customtkinter.CTkLabel(window, text="Login", fg_color="transparent", font=('roboto', 28)).pack(padx=10, pady=10)
        nickname_entry = customtkinter.CTkEntry(window, font=('roboto', 18), placeholder_text="Username")
        nickname_entry.pack(padx=10, pady=10)
        password_entry = customtkinter.CTkEntry(window, show="#", font=('roboto', 18), placeholder_text="Password")
        password_entry.pack(padx=10, pady=10)
        login_button = customtkinter.CTkButton(window, text="Login", command=lambda: login(nickname_entry, password_entry)).pack(padx=10, pady=10)
        window.bind("<enter>", login_button)
        
        
        def get_ip():
            try:
                if os.name == 'nt':
                    ip = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', subprocess.check_output("ipconfig | findstr /i IPv4", shell=True, text=True))
                    return ip
                else:
                    ip = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', subprocess.check_output("ip a | findstr /i IPv4", shell=True, text=True))
                    return ip
            except Exception as error:
                print(f"error: {error}")
            finally:
                return ip
        
        def login(nickname_entry, password_entry):
            nickname = nickname_entry.get()
            password = password_entry.get()
            query = f"SELECT * FROM login WHERE nickname = %s AND senha = %s"
            cur.execute(query, (nickname, password))
            result = cur.fetchone()
            if result:
                msg = customtkinter.CTkLabel(window, text="Usuário encontrado no sistema... login realizado.", fg_color="transparent", font=('roboto', 28)).pack(padx=10, pady=10)
                print("Usuário encontrado no sistema... login realizado.")
                print(f"ip: {get_ip()}")
                main()
            else:
                msg = customtkinter.CTkLabel(window, text="Erro... login não realizado.", fg_color="transparent", font=('roboto', 28)).pack(padx=10, pady=10)
                print("Erro... login não realizado.")
        
        
        def main():
            main = customtkinter.CTk()
            main.geometry(f"{1100}x{580}")
            main.title("Main")
            
            main.grid_columnconfigure(0, weight=1)
            main.grid_rowconfigure(0, weight=1)
            
            mainmsg = customtkinter.CTkLabel(master=main, text='Menu de Operações', font=('arial', 28), fg_color='transparent')
            mainmsg.grid(row=0, column=0, padx=10, pady=10, sticky=('N', ))
            
            #sidebar
            sidebarframe = customtkinter.CTkFrame(master=main, width=50, corner_radius=0)
            sidebarframe.grid(row=0, column=0, rowspan=4, sticky='nws')
            sidebarframe.grid_rowconfigure((0,1,2,3), weight=0)
            sidebarframe.grid_columnconfigure((0,1,2,3), weight=1)
            
            #dinamic main content
            def binary():
                val = customtkinter.CTkEntry(master=main, font=('roboto', 18), placeholder_text="Número para conversão")
                val.grid(row=0, column=0, padx=10, pady=10, sticky="")
                
                
                def calcBin(val_entry):
                    binNum = ''
                    result = int(val.get())
                    val = int(val_entry.get())
                    
                    initime = datetime.datetime.now()
                    if(str(val).isdigit()):
                        if (val > 1):
                            print('processing........')
                            while (result != 1):
                                binNum = binNum + str((result % 2))
                                if (result // 2 == 1):
                                    binNum = binNum + str((result // 2))
                                    #print('test1 -> ' + str(result))
                                    break
                                else: 
                                    result = result // 2
                                    #print('test2 -> ' + str(result))
                            print('converted value is: -> ' + str(binNum[::-1]))
                            endtime = datetime.datetime.now()
                            print(f'Time taken: {endtime - initime}')
                        elif (val == 0):
                            print('processing........')
                            binNum = '0'
                            print('converted value is: -> ' + binNum[::-1])
                        elif (val == 1):
                            print('processing........')
                            binNum = '1'
                            print('converted value is: -> ' + binNum[::-1])
                    else: 
                        print('Input invalid.')
                btncalc = customtkinter.CTkButton(master=main, font=("roboto", 18), text="Run")
                btncalc.grid(row=0, column=1, padx=10, pady=10, sticky="", command=lambda: calcBin(val))
                output = customtkinter.CTkEntry(master=main, font=('roboto', 18), placeholder_text="", state='disabled')
                output.grid(row=1, column=0, padx=10, pady=0, sticky="")
                
                
                
                    #end function
            
            
            
            
            
            
            binbut = customtkinter.CTkButton(sidebarframe, text="Binary calculator", command=lambda: binary(), width=200, height=60)
            binbut.grid(row=0, column=0, padx=20, pady=10, sticky="nws")
            
            primebut = customtkinter.CTkButton(sidebarframe, text="Prime Calculator", width=200, height=60)
            primebut.grid(row=1, column=0, padx=20, pady=10, sticky="nws")
            
            p_marbut = customtkinter.CTkButton(sidebarframe, text="Mersenne Prime Calculator", width=200, height=60)
            p_marbut.grid(row=2, column=0, padx=20, pady=10, sticky="nws")
            
            d3but = customtkinter.CTkButton(sidebarframe, text="Three way law Calculator", width=200, height=60)
            d3but.grid(row=3, column=0, padx=20, pady=10, sticky="nws")

    
            window_quit(window)
            main.mainloop()
        
        def window_quit(win):
            win.quit()
            win.destroy()
        
        window.mainloop()
except Exception as error:
    print(f"error: {error}")
finally:
    if conn is not None:
        conn.close()




