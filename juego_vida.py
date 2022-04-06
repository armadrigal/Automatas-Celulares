import numpy as np
import matplotlib.pyplot as plt

N = 100
iter = 1000
estado = np.random.randint(0,2,size=(N+2,N+2))
vecinos = np.zeros((N+2,N+2),dtype=int)
porc_vivos = np.zeros(iter)
porc_muertos = np.zeros(iter)

fig, ax = plt.subplots()

for i in range(iter):

    #Condiciones de frontera
    estado[0,1:N+1] = estado[N,1:N+1]
    estado[N+1,1:N+1] = estado[1,1:N+1]
    estado[1:N+1,0] = estado[1:N+1,N]
    estado[1:N+1,N+1] = estado[1:N+1,1]
    estado[0,0] = estado[N,N]
    estado[0,N+1] = estado[N,1]
    estado[N+1,0] = estado[1,N]
    estado[N+1,N+1] = estado[1,1]

    for j in range(1,N+1):
        for k in range(1,N+1):
            vecinos[j,k] = np.sum(estado[j-1:j+2,k-1:k+2])

    for j in range(1,N+1):
        for k in range(1,N+1):
            if estado[j,k] == 0 and vecinos[j,k] == 3:
                estado[j,k] = 1
            elif estado[j,k] == 1 and (vecinos[j,k] == 3 or vecinos[j,k] == 4):
                estado[j,k] = 1
            else:
                estado[j,k] = 0

    porc_vivos[i] = (np.sum(estado[1:N+1,1:N+1])*100)/N**2
    porc_muertos[i] = 100 - porc_vivos[i]

    ax.cla()
    ax.imshow(estado[1:N+1,1:N+1])
    ax.set_title("Generacion {}".format(i))
    plt.pause(0.0005)
plt.figure()
plt.plot(np.arange(0,iter,1,dtype=int),porc_vivos,label='Vivos')
plt.plot(np.arange(0,iter,1,dtype=int),porc_muertos,label='Muertos')
plt.show()