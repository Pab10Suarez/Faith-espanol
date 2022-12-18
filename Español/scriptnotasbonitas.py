from tkinter import *
def contarlineas(resultado):
   
    nlineas=resultado.count("\r\n")+1 #
    
    print("Total lineas = ",nlineas,"\n En código = ",nlineas+1)
def ponerBonitoElTexto():
    #stringingresada="Padre Garcia,\ñ Por la presente se le ordena que libere a Michael Davies de su custodia y lo devuelva a su casa  inmediatamente.\ñ El Sr. y Sra. Davies ya han sido contactados pornuestra oficina asi que un repesentante de la iglesia está en camino a su casapara discutir una compensacion a cambio de su discrecion. Usted e reunira con nuestro representante alli y lo acompañara de vuelta a Roma.\ñ             -Cardinal Gifford\ñ"
    stringingresada=cuadroTexto.get()
    listaoracionesfinal=[]
    palabras=stringingresada.split()
    i=0
    oracionactual=[]
    saltolinea=False
    for palabra in palabras:  
        palabras[i]=palabra+" "
        palabra=palabra+" "
        oracionactual.append(palabra)
        if(len("".join(oracionactual))<27):
            if(palabra.count("\ñ")==1 ):
                oracionactual[-1]=oracionactual[-1][:-3]
                print("ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ",palabra)
                palabra=palabra[:-3] #borra \\ñ AGUAC 
                print("ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ",palabra)
                palabra="".join(oracionactual)+"\r\n\r\n" #le agrega los 2 saltos 
                listaoracionesfinal.append(palabra) ## agrega a la lista de oraciones final  la oracion
                oracionactual=[]      
            else:
                print(len("".join(oracionactual)),"  ".join(oracionactual))        
        else:
            listaoracionesfinal.append("".join(oracionactual[:-1])+"\r\n")
            oracionactual=oracionactual[-1:] 
            if(palabra.count("\ñ")==1 ):
                oracionactual[-1]=oracionactual[-1][:-3]
                print("Ñ2Ñ2Ñ2"+palabra)
                palabra="".join(oracionactual)+"\r\n\r\n"
                
                listaoracionesfinal.append(palabra) #agrega a la lista final la oracion actual que seria ha sta donde vaya ñ
                print("ELSE","".join(oracionactual)) 
                oracionactual=[]        
             #oracion actual= igual todo menos lo que ya se agregó a la lista de oraciones final
            else:

                print("ELSE","".join(oracionactual))
        print("oracion actual: ",oracionactual)
        i+=1
        
    
    resultado1=repr(("".join(listaoracionesfinal)))
    contarlineas("".join(listaoracionesfinal))
    print("".join(listaoracionesfinal))
   #resultado1.replace("LMAOSANT")
    resultado1= "\""+resultado1[1:-1]+"\""+","#imprime la oracion pero lista para copiar y pegar
    resultado.set(resultado1)
    print(resultado1)
stringoriginal="Padre Garcia,\r\n\r\nPor la presente se le ordena\r\nque libere a Michael Davies\r\nde su custodia y \r\nlo devuelva a su casa\r\ninmediatamente.\r\n              \r\nEl Sr. y Sra. Davies ya han\r\nsido contactados por\r\nnuestra oficina asi que\r\nun repesentante de la iglesia \r\nestá en camino a su casa\r\npara discutir una compe-\r\nnsacion a cambio de su \r\ndiscrecion.\r\nUsted e reunira con nuestro\r\nrepresentante alli y lo aco-\r\nmpañara de vuelta a Roma.\r\n\r\n              \r\n- Cardinal Gifford\r\n"
stringingresada="Padre Garcia,\ñ Por la presente se le ordena que libere a Michael Davies de su custodia y lo devuelva a su casa  inmediatamente.\ñ El Sr. y Sra. Davies ya han sido contactados pornuestra oficina asi que un repesentante de la iglesia está en camino a su casapara discutir una compensacion a cambio de su discrecion. Usted e reunira con nuestro representante alli y lo acompañara de vuelta a Roma.\ñ             -Cardinal Gifford\ñ"
def copiar():
    root.clipboard_append(textorespuesta.get())
root=Tk()
root.title('MORTIS Ñ EDITION')
resultado=StringVar()
Frame=Frame(root,width=700,height=500)
Frame.pack() 



boton=Button(Frame,text="ponerbonito",font=("Arial",15),command=ponerBonitoElTexto,foreground="#F1F1F1",background="#000000")
boton.place(x=100,y=150)
boton=Button(Frame,text="copiar",command=copiar,font=("Arial",15),foreground="#F1F1F1",background="#000000")
boton.place(x=100,y=350)
textorespuesta=Entry(Frame,width=80, textvariable=resultado)
textorespuesta.place(x=50,y=300,)
cuadroTexto=Entry(Frame,width=80)
cuadroTexto.place(x=50,y=100)
label1= Label(text="@ñ= \\\"",font=("Arial",17) ).place(y=150,x=340)
label2= Label(text="\ñ = espacio entre parrafos\n PD: Tambien poner a la ultima linea",font=("Arial",17),foreground="#29BB32").place(y=200,x=330)
stringnota= Label(text="string sin formato" ,font=("Arial",20) ).place(y=50,x=50)
stringnotatraducida= Label(text=" formato: " ,font=("Arial",20) ).place(y=250,x=50)
boton.pack
root.mainloop()#\\\"