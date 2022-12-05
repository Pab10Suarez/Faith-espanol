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
        
        if(palabra.count("\ñ")==1 and len("".join(oracionactual))<=28):
            print("ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ",palabra)
            palabra=palabra[:-3] #borra //ñ
            print("ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ",palabra)
            palabra="".join(oracionactual)+palabra+"\r\n\r\n" #le agrega los 2 saltos 
            listaoracionesfinal.append(palabra) ## agrega a la lista de oraciones final  la oracion
            oracionactual=[]
            
            saltolinea=True
        elif(not saltolinea):  
            if(len("".join(oracionactual))<=26):
                oracionactual.append(palabra)
                print("".join(oracionactual))
            else:
                listaoracionesfinal.append("".join(oracionactual[:-1])+"\r\n")
                oracionactual=oracionactual[-1:] #oracion actual= igual todo menos lo que ya se agregó a la lista de oraciones final
                 #agrega la palabra actual 
                if(palabra.count("\ñ")==1 ):
                    palabra=palabra[:-2]  
                oracionactual.append(palabra)
                
                print("ELSE","".join(oracionactual))
        saltolinea=False
        print("ciclo palabra ",oracionactual)
        i+=1
        
    contarlineas("".join(listaoracionesfinal))
    resultado1=repr(("".join(listaoracionesfinal)))
    
   #resultado1.replace("LMAOSANT")
    resultado1= "\""+resultado1[1:-1]+"\""+","#imprime la oracion pero lista para copiar y pegar
    resultado.set(resultado1)
    print(resultado1)
stringoriginal="Padre Garcia,\r\n\r\nPor la presente se le ordena\r\nque libere a Michael Davies\r\nde su custodia y \r\nlo devuelva a su casa\r\ninmediatamente.\r\n              \r\nEl Sr. y Sra. Davies ya han\r\nsido contactados por\r\nnuestra oficina asi que\r\nun repesentante de la iglesia \r\nestá en camino a su casa\r\npara discutir una compe-\r\nnsacion a cambio de su \r\ndiscrecion.\r\nUsted e reunira con nuestro\r\nrepresentante alli y lo aco-\r\nmpañara de vuelta a Roma.\r\n\r\n              \r\n- Cardinal Gifford\r\n"
stringingresada="Padre Garcia,\ñ Por la presente se le ordena que libere a Michael Davies de su custodia y lo devuelva a su casa  inmediatamente.\ñ El Sr. y Sra. Davies ya han sido contactados pornuestra oficina asi que un repesentante de la iglesia está en camino a su casapara discutir una compensacion a cambio de su discrecion. Usted e reunira con nuestro representante alli y lo acompañara de vuelta a Roma.\ñ             -Cardinal Gifford\ñ"
def copiar():
    root.clipboard_append(textorespuesta.get())
root=Tk()
resultado=StringVar()
Frame=Frame(root,width=700,height=500)
Frame.pack() 



boton=Button(Frame,text="ponerbonito",command=ponerBonitoElTexto)
boton.place(x=100,y=150)
boton=Button(Frame,text="copiar",command=copiar)
boton.place(x=200,y=150)
textorespuesta=Entry(Frame,width=150, textvariable=resultado)
textorespuesta.place(x=50,y=300,relheight=0.3)
cuadroTexto=Entry(Frame,width=300)
cuadroTexto.place(x=50,y=100)

boton.pack
# imagenbacan=PhotoImage(file="coso.png")
# Label(Frame,image=imagenbacan).place(x=100,y=200)
root.mainloop()