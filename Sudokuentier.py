import tkinter as tk
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#                                                                                       ENTREE
#                               INTERFACE DU SUDOKU
app = tk.Tk()
app.minsize(1100,915)

app.title('Saisi du Sudoku')

Canvas=tk.Canvas(app, width=910, height=910)

for i in range (0,10):
    if i%3==0 or i==0 :
        Canvas.create_line((5+i*100,5),(5+i*100,905),width=8)
        Canvas.create_line((5,5+i*100),(908,5+i*100),width=8)   
    else:
        Canvas.create_line((5+i*100,5),(5+i*100,905),width=4)
        Canvas.create_line((5,5+i*100),(905,5+i*100),width=4)
        
        
#                               PROGRAMMES 

def dimensionfenetrePE():
    # app.overrideredirect(True)
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
def dimensionfenetreM():
    app.geometry('1100x915')
def dimensionfenetre5():
    app.geometry('2200x1830')

def creation() :  
    tab_val_sud=[]*len(tab_var)
    for i in range (len(tab_var)):
        tab_val_sud[i]=tab_var[i].get()
    print(tab_val_sud)
def execute():
    app.destroy()
    sudoku_saisie=[]
    for i in range (len(tab_var)):
        if tab_var[i].get() == '' or tab_var[i].get() == '1' or tab_var[i].get() == '2' or tab_var[i].get() == '3' or tab_var[i].get() == '4' or tab_var[i].get() == '5' or tab_var[i].get() == '6' or tab_var[i].get() == '7'or tab_var[i].get() == '8'or tab_var[i].get() == '9' :
                if tab_var[i].get() != '' :
                    sudoku_saisie.append(int(tab_var[i].get()))
                else:
                    sudoku_saisie.append(0)
        
        else:
            print('Saisie incorrecte')
    
    t=lignetocaree (sudoku_saisie)
    t=np.transpose(t)
    afficher(t)
    

def lignetocaree(t):
    sortie=[[]]*9
    for i in range(9):
        sortie[i]=t[0+(i*9) : 9*(i+1)]
        
    return(sortie)

                          # ENTREES

tab_var=[]
for a in range (81):
        tab_var.append(tk.StringVar())
b=0
k=0

for i in range (9):

    for j in range(9):
        # tab_var[b]=tk.StringVar()
        
        
        i=tk.Entry(app, width=2, font=('Times', -60), textvariable=tab_var[b])
        i.place(x=15+k*100, y=18+j*100)
        
        # tab_var[b].trace('w',creation)
    
        b+=1
    k+=1

#                       Menu 

mainmenu=tk.Menu(app)
parametre=tk.Menu(mainmenu,tearoff=0)
parametre.add_command(label="Affichage")

dimension=tk.Menu(parametre, tearoff=0 ) 
dimension.add_command(label="Plein écran", command=dimensionfenetrePE)
dimension.add_command(label="50%", command=dimensionfenetre5)
dimension.add_command(label="Minimum", command=dimensionfenetreM)



    

boutonfin=tk.Button(app, text='Sudoku rempli',command=execute, width=15)
boutonquit=tk.Button(app, text='Quitter', command=app.destroy, width=15)


#                       Placement

mainmenu.add_cascade(label="Parametre", menu=parametre)
parametre.add_cascade(label='Fenetre', menu=dimension)

boutonfin.place(x=950,y=410)
boutonquit.place(x=950,y=480)


Canvas.place(x=0, y=0)


app.config(menu=mainmenu)
app.mainloop()

#                                                                                       TRAITEMENT

def grille(n):
    t1=np.full((n,n),1,dtype=int) 
    t2=np.full((n,n),2,dtype=int)
    t3=np.full((n,n),3,dtype=int)
    t4=np.full((n,n),4,dtype=int)
    t5=np.full((n,n),5,dtype=int)
    t6=np.full((n,n),6,dtype=int)
    t7=np.full((n,n),7,dtype=int)
    t8=np.full((n,n),8,dtype=int)
    t9=np.full((n,n),9,dtype=int)
    return(t1,t2,t3,t4,t5,t6,t7,t8,t9,)
    
def zerol(t,l):
    for i in range(len(t)):
        t[l]=0
    return(t)
    
def zeroc(t,c):
    for i in range(len(t)):
        t[i][c]=0
    return(t)
def zerocarre(t,l,c):
    if l<=2 and c<=2:
        for i in range(3):
            for j in range(3):
                t[i][j]=0
    if l<=5 and l>2 and c<=2 :
        for i in range(3):
            for j in range(3):
                t[i+3][j]=0
    if l>5 and c<=2 :
        for i in range(3):
            for j in range(3):
                t[i+6][j]=0
    if l<=2 and c<=5 and c>2 :
        for i in range(3):
            for j in range(3):
                t[i][j+3]=0
    if l<=5 and l>2 and c>2 and c<=5 :
        for i in range(3):
            for j in range(3):
                t[i+3][j+3]=0
    if l>5 and c>2 and c<=5 :
        for i in range(3):
            for j in range(3):
                t[i+6][j+3]=0
    if c>5 and l<=2 :
        for i in range(3):
            for j in range(3):
                t[i][j+6]=0
    if c>5 and l<=5 and l>2 :
        for i in range(3):
            for j in range(3):
                t[i+3][j+6]=0
    if c>5 and l>5 :
        for i in range(3):
            for j in range(3):
                t[i+6][j+6]=0
    return(t)
    
def tri_encombre(t,ti,k):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j]==k:
                ti[i][j]=0
    return(ti)
        

def selection(t):
    (t1,t2,t3,t4,t5,t6,t7,t8,t9)=grille(len(t))
    for i in range (len(t)):
        for j in range (len(t[i])):
            if t[i][j]==1:
                t1=zeroc(t1,j)
                t1=zerol(t1,i)
                t1=zerocarre(t1,i,j)
                t1=tri_encombre(t,t1,1)
            if t[i][j]==2:
                t2=zeroc(t2,j)
                t2=zerol(t2,i)
                t2=zerocarre(t2,i,j)
                t2=tri_encombre(t,t2,2)
            if t[i][j]==3:
                t3=zeroc(t3,j)
                t3=zerol(t3,i)
                t3=zerocarre(t3,i,j)
                t3=tri_encombre(t,t3,3)
            if t[i][j]==4:
                t4=zeroc(t4,j)
                t4=zerol(t4,i)
                t4=zerocarre(t4,i,j)
                t4=tri_encombre(t,t4,4)
            if t[i][j]==5:
                t5=zeroc(t5,j)
                t5=zerol(t5,i)
                t5=zerocarre(t5,i,j)
                t5=tri_encombre(t,t5,5)
            if t[i][j]==6:
                t6=zeroc(t6,j)
                t6=zerol(t6,i)
                t6=zerocarre(t6,i,j)
                t6=tri_encombre(t,t6,6)
            if t[i][j]==7:
                t7=zeroc(t7,j)
                t7=zerol(t7,i)
                t7=zerocarre(t7,i,j)
                t7=tri_encombre(t,t7,7)
            if t[i][j]==8:
                t8=zeroc(t8,j)
                t8=zerol(t8,i)
                t8=zerocarre(t8,i,j)
                t8=tri_encombre(t,t8,8)
            if t[i][j]==9:
                t9=zeroc(t9,j)
                t9=zerol(t9,i)
                t9=zerocarre(t9,i,j)
                t9=tri_encombre(t,t9,9)
    return(t1,t2,t3,t4,t5,t6,t7,t8,t9)



def comptecolonne(t,c,n):
    s=0
    for i in range (len(t)):
        if t[i][c]==n:
            s+=1
    return(s)
def comptecarre(t,l,c,n):
    s=0
    if l<=2 and c<=2:
        for i in range(3):
            for j in range(3):
                if t[i][j]==n:
                    s+=1
    if l<=5 and l>2 and c<=2 :
        for i in range(3):
            for j in range(3):
                if t[i+3][j]==n:
                    s+=1
    if l>5 and c<=2 :
        for i in range(3):
            for j in range(3):
                if t[i+6][j]==n:
                    s+=1
    if l<=2 and c<=5 and c>2 :
        for i in range(3):
            for j in range(3):
                if t[i][j+3]==n:
                    s+=1
    if l<=5 and l>2 and c>2 and c<=5 :
        for i in range(3):
            for j in range(3):
                if t[i+3][j+3]==n:
                    s+=1
    if l>5 and c>2 and c<=5 :
        for i in range(3):
            for j in range(3):
                if t[i+3][j+3]==n:
                    s+=1
    if c>5 and l<=2 :
        for i in range(3):
            for j in range(3):
                if t[i][j+6]==n:
                    s+=1
    if c>5 and l<=5 and l>2 :
        for i in range(3):
            for j in range(3):
                if t[i+3][j+6]==n:
                    s+=1
    if c>5 and l>5 :
        for i in range(3):
            for j in range(3):
                if t[i+6][j+6]==n:
                    s+=1
    return(s)
    

def rempli1(t,ti):
    for i in range(len(ti)):
        for j in range(len(ti)):
            if ti[i][j]!=0 and np.count_nonzero(ti[i]==ti[i][j])==1 and comptecarre(ti,i,j,ti[i][j])==1 and comptecolonne(ti,j,ti[i][j])==1:
                t[i][j]=ti[i][j]
                ti[i][j]=0
    return(t)
def rempli2(t,T):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j]==0:
                valeur=[]
                tableau=[]
                for p in T:
                    if p[i][j]!=0:
                        valeur.append(p[i][j])
                        tableau.append(p)
                if len(valeur)==1:
                    t[i][j]=valeur[0]
                    tableau[0][i][j]=0
                
    return(t)
                

def selection2(t):
    tsorti=[]
    T=selection(t)
    for i in T:
        tsorti=rempli1(t,i)
    tsorti=rempli2(t,T)
    return(tsorti)

def comptezero(t):
    s=0
    for i in range(len(t)):
        for j in t[i]:
            if j==0:
                s+=1
    return(s)

def solution(t):
    T=t.copy()
    while comptezero(T)!=0:
        T=selection2(T)
    return(T)
    
#                                                                                       SORTIE

def grille2():
    image=np.zeros((900,900,3), dtype=np.uint8)
    for i in range(len(image)):
        for j in range (len(image[0])):
            if i<len(image)-10 and j<len(image)-10 and i>10 and j>10:
                image[i][j]=(255,255,255)
            if i==303 or i==603 or j==303 or j==603:
                image[i][j]=(0,0,0)
                image[i-1][j-1]=(0,0,0)
                image[i-2][j-2]=(0,0,0)
            if i==105 or i==205 or i==400 or i==500 or i==695 or i==795 or j==105 or j==205 or j==400 or j==500 or j==695 or j==795:
                image[i][j]=(0,0,0)
    return(image)
    # mpimg.imsave("D:/Document/info/projet/grille", image)
def chiffre(n,t):
    for i in range (15,len(t)-15):
        for j in range (15,len(t)-15):
            t[i][j]=(255,255,255)
    if n==0:
        for i in range (15,len(t)-15):
            for j in range (15,len(t)-15):
                t[i][j]=(255,255,255)
    if n==1:
        for i in range (15,len(t[0])-15):
            for j in range (3):
                t[i][len(t)//2-1+j]=(0,0,0)
            for l in range (15):
                        for k in range(3):
                            t[15+l][len(t)//2-k-l]=(0,0,0)

        return(t)
                            
        # mpimg.imsave("D:/Document/info/projet/1", t)
        
    if n==2:
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)-16+j][len(t)//4+i+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[2*len(t)//3-17+j][len(t)//4+i-2+8]=(0,0,0)
        for l in range (len(t)//3+3):
                    for k in range(3):
                        t[2*len(t)//3-15-l][len(t)//4-k+len(t)//3+6]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+6]=(0,0,0) 
        return(t)
                
        # mpimg.imsave("D:/Document/info/projet/2", t)
        
    if n==3 :
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)-16+j][len(t)//4+i+8]=(0,0,0)
        for i in range (len(t)//3-5):
            for j in range (3):
                t[2*len(t)//3-17+j][len(t)//4+i-2+13]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
                        t[2*len(t)//3-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+8]=(0,0,0)  
        return(t)
                
        # mpimg.imsave("D:/Document/info/projet/3", t)
        
    if n==4:
        for l in range (len(t)//3+3):
                    for k in range(3):
                        t[2*len(t)//3-15-l][len(t)//4-k+8]=(0,0,0)

        for i in range (len(t)//3):
            for j in range (3):
                t[2*len(t)//3-17+j][len(t)//4+i-2+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
                        t[2*len(t)//3-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
        return(t)

            
        # mpimg.imsave("D:/Document/info/projet/4", t)

    if n==5:
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)-16+j][len(t)//4+i+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[2*len(t)//3-14-l][len(t)//4-k+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[2*len(t)//3-16+j][len(t)//4+i-2+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+7]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+6]=(0,0,0)
            
        return(t)
            
        # mpimg.imsave("D:/Document/info/projet/5", t)

    if n==6:
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)-16+j][len(t)//4+i+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[2*len(t)//3-14-l][len(t)//4-k+8]=(0,0,0)
                        t[len(t)-14-l][len(t)//4-k+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[2*len(t)//3-16+j][len(t)//4+i-2+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+8]=(0,0,0)        

        return(t)
            
        # mpimg.imsave("D:/Document/info/projet/6", t)

    if n==7:
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
                        t[2*len(t)//3-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+8]=(0,0,0)        
        return(t)
        # mpimg.imsave("D:/Document/info/projet/7", t)
    
    if n==8:
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)-16+j][len(t)//4+i+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[2*len(t)//3-14-l][len(t)//4-k+8]=(0,0,0)
                        t[len(t)-14-l][len(t)//4-k+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[2*len(t)//3-17+j][len(t)//4+i-2+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
                        t[2*len(t)//3-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+8]=(0,0,0)        

        return(t)
            
        # mpimg.imsave("D:/Document/info/projet/8", t)

    if n==9:
        for i in range (len(t)//3):
            for j in range (3):
                t[len(t)-16+j][len(t)//4+i+8]=(0,0,0)
        for l in range (len(t)//3+3):
                    for k in range(3):
                        t[2*len(t)//3-15-l][len(t)//4-k+8]=(0,0,0)
        for i in range (len(t)//3):
            for j in range (3):
                t[2*len(t)//3-17+j][len(t)//4+i-2+8]=(0,0,0)
        for l in range (len(t)//3+4):
                    for k in range(3):
                        t[len(t)-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
                        t[2*len(t)//3-14-l][len(t)//4-k+len(t)//3+8]=(0,0,0)
        for i in range (len(t)//3+3):
            for j in range (3):
                t[len(t)//3-17+j][len(t)//4-i+len(t)//3+8]=(0,0,0)        
        return(t)
            
        # mpimg.imsave("D:/Document/info/projet/9", t)
    
def remplissage(t):
    t_copy=t.copy()
    image=grille2()
    compte0=0
    for i in range (len(t_copy)):
        for j in range (len(t_copy[i])):
            if t_copy[i][j]!=0:
                image[i*100:100+i*100,j*100:j*100+100]= chiffre(t_copy[i][j],image[i*100:100+i*100,j*100:j*100+100])
            else:
                compte0+=1
    if compte0==0:
        mpimg.imsave("D:/Document/info/projet/Solution",image)
    else:
        mpimg.imsave("D:/Document/info/projet/NonResolu",image)
   
def afficher(t):
    remplissage(t)
    
    remplissage(solution(t))
    
    
    fenetre = tk.Tk()
    fenetre.wm_state(newstate="zoomed")
    
    PhotoSolution = tk.PhotoImage(file='../Solution.png')
    PhotoNonresolu = tk.PhotoImage(file='../NonResolu.png')
    
    label1 = tk.Label(fenetre, image=PhotoSolution)
    label2 = tk.Label(fenetre, image=PhotoNonresolu)
    boutonquitte= tk.Button(fenetre, command=fenetre.destroy, width=20, text='Quitter')
    
    label1.place(x=1015, y=0)
    label2.place(x=0, y=0)
    boutonquitte.place(x=875, y=950)
    
    fenetre.mainloop()