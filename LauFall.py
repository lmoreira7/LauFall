from tkinter import*
import math

    # Funções para interação das Janelas #

def QuedaLivre():
    Janela1 = Tk()
    Janela1.title('Queda Livre')
    Janela1.geometry('300x210+300+220')
    Janela1.iconbitmap('arrow.ico')
    Janela1.resizable(False, False)

    lb = Label(Janela1, text='Selecione uma opção:', font='Times 14')
    lb.place(x=60, y=10)

        ## Criação dos Botões ##

    Botao_Altura = Button(Janela1, width=10, text='1. Altura', command=QLAlt)
    Botao_Altura.place(x=5, y=70)

    Botao_AltTorricelli = Button(Janela1, width=10, text='2. Altura\n(por Torricelli)', command=QLAltTorricelli)
    Botao_AltTorricelli.place(x=5, y=110)

    Botao_Vel = Button(Janela1, width=10, text='3. Velocidade', command=QLVel)
    Botao_Vel.place(x=92, y=70)

    Botao_VelTorricelli = Button(Janela1, width=10, text='4. Velocidade\n(por Torricelli)', command=QLVelTorricelli)
    Botao_VelTorricelli.place(x=92, y=110)

    Botao_TempoQueda = Button(Janela1, width=15, text='5. Tempo de Queda', command=QLTempQueda)
    Botao_TempoQueda.place(x=180, y=70)

    Botao_Voltar = Button(Janela1, width=10, text='Voltar', command=Janela1.destroy)
    Botao_Voltar.place(x=104, y=180)


def LancamentoVertical():
    Janela2 = Tk()
    Janela2.title('Lançamento Vertical')
    Janela2.geometry('300x210+1020+220')
    Janela2.iconbitmap('arrow.ico')
    Janela2.resizable(False, False)

    lb = Label(Janela2, text='Selecione uma opção:', font='Times 14')
    lb.place(x=60, y=10)

        ## Criação dos Botões

    Botao_AltMax = Button(Janela2, width=15, text='1. Altura Máxima', command=LVAltMax)
    Botao_AltMax.place(x=20, y=70)

    Botao_VelInicial = Button(Janela2, width=15, text='2. Velocidade Inicial\n(atingar Alt. Máx.)', command=LVVelInicial)
    Botao_VelInicial.place(x=20, y=110)

    Botao_TempoSub = Button(Janela2, width=15, text='3. Tempo de Subida', command=LVTempSub)
    Botao_TempoSub.place(x=170, y=70)

    Botao_TempPerm = Button(Janela2, width=15, text='4. Tempo de\npermanência no ar', command=LVTempPerm)
    Botao_TempPerm.place(x=170, y=110)

    Botao_Voltar = Button(Janela2, width=10, text='Voltar', command=Janela2.destroy)
    Botao_Voltar.place(x=104, y=180)


    # Funcionamento Geral do Programa #

Janela = Tk()
Janela.title('LauFall')
Janela.geometry('300x320+660+220')
Janela.iconbitmap('arrow.ico')
Janela.resizable(False, False)

Botao_QuedaLivre = Button(Janela, width=10, text='1. Queda livre', command=QuedaLivre)
Botao_QuedaLivre.place(x=108, y=200)

Botao_Lancamento = Button(Janela, width=20, text='2. Lançamento vertical', command=LancamentoVertical)
Botao_Lancamento.place(x=75, y=240)

Botao_Encerrar = Button(Janela, width=10, text='Encerrar', command=Janela.destroy)
Botao_Encerrar.place(x=108, y=280)

lb = Label(Janela, text='LauFall', font='Times 25')
lb.place(x=97, y=75)

def QLAlt():
    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def armTemp():
        temp = float(t.get())
        return float(temp)

    def Alt():
        time = armTemp()
        acc = armAcc()
        h = (acc * (time ** 2)) / 2
        lb1['text'] = h

    # Construção da Janela #
    janela3 = Tk()
    janela3.title('Altura')
    janela3.geometry('300x210')
    janela3.iconbitmap('arrow.ico')
    janela3.resizable(False, False)

    lb = Label(janela3, text='Altura em m:')
    lb.place(x=95, y=108)

    lb1 = Label(janela3, text='')
    lb1.place(x=115, y=135)

    # Entrada de Dados #
    text = Label(janela3, text='Tempo (s): ')
    text.grid(row=0, column=0, padx=10, pady=10)
    t = Entry(janela3)
    t.place(x=150, y=11, width=50, height=20)

    text = Label(janela3, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela3)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btT = Button(janela3, width=5, text='OK', command=armTemp)
    btT.place(x=210, y=7)

    btAcc = Button(janela3, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela3, width=10, text='Resolver', command=Alt)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela3, width=5, text='Voltar', command=janela3.destroy)
    botao_voltar.place(x=75, y=180)

def QLAltTorricelli():
    def armv0():
        vI = float(v0.get())
        return float(vI)

    def armVel():
        vel = float(v.get())
        return float(vel)

    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def AltT():
        v0 = armv0()
        acc = armAcc()
        vel = armVel()
        r = (v0 ** 2) - (vel ** 2)
        alt = r / (2 * acc)
        lb1['text'] = alt

    # Construção da Janela #
    janela4 = Tk()
    janela4.title('Altura (por Torricelli)')
    janela4.geometry('300x245')
    janela4.iconbitmap('arrow.ico')
    janela4.resizable(False, False)

    lb = Label(janela4, text='Altura em m:')
    lb.place(x=95, y=135)

    lb1 = Label(janela4, text='')
    lb1.place(x=108, y=162)

    # Entrada de Dados #
    text = Label(janela4, text='Velocidade Inicial (m/s):')
    text.grid(row=0, column=0, padx=10, pady=10)
    v0 = Entry(janela4)
    v0.place(x=150, y=11, width=50, height=20)

    text = Label(janela4, text='Velocidade (m/s):')
    text.grid(row=1, column=0, padx=10, pady=10)
    v = Entry(janela4)
    v.place(x=150, y=52, width=50, height=20)

    text = Label(janela4, text='Aceleração (m/s²):')
    text.grid(row=2, column=0, padx=10, pady=10)
    acc = Entry(janela4)
    acc.place(x=150, y=93, width=50, height=20)

    # Botões Interativos #

    btT = Button(janela4, width=5, text='OK', command=armv0)
    btT.place(x=210, y=7)

    btV = Button(janela4, width=5, text='OK', command=armVel)
    btV.place(x=210, y=48)

    btAcc = Button(janela4, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=89)

    btR = Button(janela4, width=10, text='Resolver', command=AltT)
    btR.place(x=130, y=205)

    botao_voltar = Button(janela4, width=5, text='Voltar', command=janela4.destroy)
    botao_voltar.place(x=75, y=205)

def QLVel():
    def armTemp():
        temp = float(t.get())
        return float(temp)

    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def Vel():
        time = armTemp()
        acc = armAcc()
        v = acc * time
        lb1['text'] = v

    # Construção da Janela #
    janela5 = Tk()
    janela5.title('Velocidade')
    janela5.geometry('300x210')
    janela5.iconbitmap('arrow.ico')
    janela5.resizable(False, False)

    lb = Label(janela5, text='Velocidade em m/s:')
    lb.place(x=90, y=108)

    lb1 = Label(janela5, text='')
    lb1.place(x=132, y=135)

    # Entrada de Dados #
    text = Label(janela5, text='Tempo (s): ')
    text.grid(row=0, column=0, padx=10, pady=10)
    t = Entry(janela5)
    t.place(x=150, y=11, width=50, height=20)

    text = Label(janela5, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela5)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btT = Button(janela5, width=5, text='OK', command=armTemp)
    btT.place(x=210, y=7)

    btAcc = Button(janela5, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela5, width=10, text='Resolver', command=Vel)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela5, width=5, text='Voltar', command=janela5.destroy)
    botao_voltar.place(x=75, y=180)

def QLVelTorricelli():
    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def armAlt():
        a = float(alt.get())
        return float(a)

    def VelT():
        at = armAlt()
        acc = armAcc()
        m = 2 * acc * at
        v = math.sqrt(m)
        lb1['text'] = v

    # Construção da Janela #
    janela6 = Tk()
    janela6.title('Velocidade (por Torricelli)')
    janela6.geometry('300x210')
    janela6.iconbitmap('arrow.ico')
    janela6.resizable(False, False)

    lb = Label(janela6, text='Velocidade em m/s:')
    lb.place(x=90, y=108)

    lb1 = Label(janela6, text='')
    lb1.place(x=100, y=135)

    # Entrada de Dados #
    text = Label(janela6, text='Altura em m: ')
    text.grid(row=0, column=0, padx=10, pady=10)
    alt = Entry(janela6)
    alt.place(x=150, y=11, width=50, height=20)

    text = Label(janela6, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela6)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btH = Button(janela6, width=5, text='OK', command=armAlt)
    btH.place(x=210, y=7)

    btAcc = Button(janela6, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela6, width=10, text='Resolver', command=VelT)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela6, width=5, text='Voltar', command=janela6.destroy)
    botao_voltar.place(x=75, y=180)

def QLTempQueda():
    def armPos0():
        s0 = float(si.get())
        return float(s0)

    def armPosF():
        sF = float(sf.get())
        return float(sF)

    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def TempQueda():
        ace = armAcc()
        s0 = armPos0()
        sf = armPosF()
        r = (s0-sf)/(ace/2)
        t = math.sqrt(r)
        lb1['text'] = t

    # Construção da Janela #
    janela9 = Tk()
    janela9.title('Tempo de Queda')
    janela9.geometry('300x245')
    janela9.iconbitmap('arrow.ico')
    janela9.resizable(False, False)

    lb = Label(janela9, text='Tempo de Queda em s:')
    lb.place(x=80, y=135)

    lb1 = Label(janela9, text='')
    lb1.place(x=86, y=162)

    # Entrada de Dados #
    text = Label(janela9, text='Posição Inicial (m):')
    text.grid(row=0, column=0, padx=10, pady=10)
    si = Entry(janela9)
    si.place(x=150, y=11, width=50, height=20)

    text = Label(janela9, text='Posição Final (m):')
    text.grid(row=1, column=0, padx=10, pady=10)
    sf = Entry(janela9)
    sf.place(x=150, y=52, width=50, height=20)

    text = Label(janela9, text='Aceleração (m/s²):')
    text.grid(row=2, column=0, padx=10, pady=10)
    acc = Entry(janela9)
    acc.place(x=150, y=93, width=50, height=20)

    # Botões Interativos #

    btSI = Button(janela9, width=5, text='OK', command=armPos0)
    btSI.place(x=210, y=7)

    btSF = Button(janela9, width=5, text='OK', command=armPosF)
    btSF.place(x=210, y=48)

    btAcc = Button(janela9, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=89)

    btR = Button(janela9, width=10, text='Resolver', command=TempQueda)
    btR.place(x=130, y=205)

    botao_voltar = Button(janela9, width=5, text='Voltar', command=janela9.destroy)
    botao_voltar.place(x=75, y=205)

def LVAltMax():
    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def armv0():
        vI = float(v0.get())
        return float(vI)

    def AltMax():
        v0 = armv0()
        acc = armAcc()
        alt = (v0 ** 2) / (2 * acc)
        lb1['text'] = alt

    # Construção da Janela #
    janela7 = Tk()
    janela7.title('Altura Máxima')
    janela7.geometry('300x210')
    janela7.iconbitmap('arrow.ico')
    janela7.resizable(False, False)

    lb = Label(janela7, text='Altura Máxima em m:')
    lb.place(x=90, y=108)

    lb1 = Label(janela7, text='')
    lb1.place(x=95, y=135)

    # Entrada de Dados #
    text = Label(janela7, text='Velocidade Inicial (m/s): ')
    text.grid(row=0, column=0, padx=10, pady=10)
    v0 = Entry(janela7)
    v0.place(x=150, y=11, width=50, height=20)

    text = Label(janela7, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela7)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btv0 = Button(janela7, width=5, text='OK', command=armv0)
    btv0.place(x=210, y=7)

    btAcc = Button(janela7, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela7, width=10, text='Resolver', command=AltMax)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela7, width=5, text='Voltar', command=janela7.destroy)
    botao_voltar.place(x=75, y=180)

def LVTempSub():
    def armv0():
        vI = float(v0.get())
        return float(vI)

    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def TempSub():
        v0 = armv0()
        acc = armAcc()
        temp = v0 / acc
        lb1['text'] = temp

    # Construção da Janela #
    janela8 = Tk()
    janela8.title('Tempo de Subida')
    janela8.geometry('300x210')
    janela8.iconbitmap('arrow.ico')
    janela8.resizable(False, False)

    lb = Label(janela8, text='Tempo de subida em s:')
    lb.place(x=90, y=108)

    lb1 = Label(janela8, text='')
    lb1.place(x=95, y=135)

    # Entrada de Dados #
    text = Label(janela8, text='Velocidade Inicial (m/s): ')
    text.grid(row=0, column=0, padx=10, pady=10)
    v0 = Entry(janela8)
    v0.place(x=150, y=11, width=50, height=20)

    text = Label(janela8, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela8)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btv0 = Button(janela8, width=5, text='OK', command=armv0)
    btv0.place(x=210, y=7)

    btAcc = Button(janela8, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela8, width=10, text='Resolver', command=TempSub)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela8, width=5, text='Voltar', command=janela8.destroy)
    botao_voltar.place(x=75, y=180)

def LVVelInicial():
    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def armAlt():
        a = float(alt.get())
        return float(a)

    def VelInicial():
        h = armAlt()
        g = armAcc()
        r = 2*g*h
        v0 = math.sqrt(r)
        lb1['text'] = v0

    # Construção da Janela #
    janela10 = Tk()
    janela10.title('Velocidade Inicial (atingir Alt. Máx.)')
    janela10.geometry('300x210')
    janela10.iconbitmap('arrow.ico')
    janela10.resizable(False, False)

    lb = Label(janela10, text='Velocidade Inicial em m/s:')
    lb.place(x=78, y=108)

    lb1 = Label(janela10, text='')
    lb1.place(x=95, y=135)

    # Entrada de Dados #
    text = Label(janela10, text='Altura (m): ')
    text.grid(row=0, column=0, padx=10, pady=10)
    alt = Entry(janela10)
    alt.place(x=150, y=11, width=50, height=20)

    text = Label(janela10, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela10)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btH = Button(janela10, width=5, text='OK', command=armAlt)
    btH.place(x=210, y=7)

    btAcc = Button(janela10, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela10, width=10, text='Resolver', command=VelInicial)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela10, width=5, text='Voltar', command=janela10.destroy)
    botao_voltar.place(x=75, y=180)

def LVTempPerm():
    def armv0():
        vI = float(v0.get())
        return float(vI)

    def armAcc():
        ace = float(acc.get())
        return float(ace)

    def tempperm():
        v0 = armv0()
        acc = armAcc()
        temp = 2*(v0 / acc)
        lb1['text'] = temp

    # Construção da Janela #
    janela11 = Tk()
    janela11.title('Tempo de perm. no ar')
    janela11.geometry('300x210')
    janela11.iconbitmap('arrow.ico')
    janela11.resizable(False, False)

    lb = Label(janela11, text='Tempo de perm. no ar em s:')
    lb.place(x=70, y=108)

    lb1 = Label(janela11, text='')
    lb1.place(x=100, y=135)

    # Entrada de Dados #
    text = Label(janela11, text='Velocidade Inicial (m/s): ')
    text.grid(row=0, column=0, padx=10, pady=10)
    v0 = Entry(janela11)
    v0.place(x=150, y=11, width=50, height=20)

    text = Label(janela11, text='Aceleração (m/s²):')
    text.grid(row=1, column=0, padx=10, pady=10)
    acc = Entry(janela11)
    acc.place(x=150, y=52, width=50, height=20)

    # Botões Interativos #

    btv0 = Button(janela11, width=5, text='OK', command=armv0)
    btv0.place(x=210, y=7)

    btAcc = Button(janela11, width=5, text='OK', command=armAcc)
    btAcc.place(x=210, y=48)

    btR = Button(janela11, width=10, text='Resolver', command=tempperm)
    btR.place(x=130, y=180)

    botao_voltar = Button(janela11, width=5, text='Voltar', command=janela11.destroy)
    botao_voltar.place(x=75, y=180)

Janela.mainloop()