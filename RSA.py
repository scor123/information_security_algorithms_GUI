from tkinter import *        
import string 


def get_n(p,q):
    return p*q;

def get_tn(p,q):
    return (p-1)*(q-1);

def gcd(x,y):
    if y==0:
        return x;
    else:
        return gcd(y,x%y);

def get_e(tn):
    e=2 
    
    while gcd(tn,e)!=1:
      e=e+1;
    return e; 

def get_d(e, tn):
  n=1 
  while (tn*n+1) % e !=0:
       n=n+1  
  d=(tn*n+1)/e
  return d

def rsa(M, key_ed, n):
  return_data = 1 
  M = M % n
  
  while key_ed != 0:
    if key_ed % 2 == 1:
      return_data = (return_data * M) % n      
    M = (M * M) % n
    key_ed = key_ed / 2

  return return_data

  


def submitclick_encrypt():
  plaintext = entryvalue.get()
  tn=get_tn(2357,1733);
  n=get_n(2357,1733);
  e=get_e(tn);
  d=get_d(e, tn);

  print( "Plaintext:",plaintext)
  print ("Public Key:(",e,",",n,")")
  print ("Private Key:(",d,",",n,")")
 

  plaintext1=string.atoi(plaintext)
  ciphertext=rsa(plaintext1,e,n);

  print ('Ciphertext: %s' % ciphertext)
  listbox.insert(0,ciphertext)




def submitclick_decrypt():
  ciphertext = entryvalue2.get()

  tn=get_tn(2357,1733);
  n=get_n(2357,1733);
  e=get_e(tn);
  d=get_d(e, tn);

  print ("Ciphertext:",ciphertext)
  print ("Public Key:(",e,",",n,")")
  print ("Private Key:(",d,",",n,")")

  ciphertext=string.atoi(ciphertext)
  plaintext=rsa(ciphertext,d,n);

  print ('Plaintext: %s' % plaintext)
  listbox2.insert(0,plaintext)










root = Tk()    
root.title('RSA')   

l = Label(root,text='Input the plaintext')
l.pack() 

entryvalue = Entry(root) 
entryvalue.pack()

button = Button(root,text="Encrypt",command=submitclick_encrypt) 
button.pack()

show = Label(root,text='Show Ciphertext:')
show.pack() 
listbox  = Listbox(root,height = 1, width = 40)        
listbox.pack() 





label = Label(root,text='Input the ciphertext')
label.pack() 

entryvalue2 = Entry(root) 
entryvalue2.pack()

button2 = Button(root,text="Decrypt",command=submitclick_decrypt) 
button2.pack()

show2 = Label(root,text='Show Plaintext:')
show2.pack() 
listbox2  = Listbox(root,height = 1, width = 40)         
listbox2.pack() 


root.mainloop()                 

