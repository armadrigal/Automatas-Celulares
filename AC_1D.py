import numpy as np
import matplotlib.pyplot as plt

N = 400
iter = 200
regla = 30

regla_bin = np.array([0,0,0,0,0,0,0,0],dtype=int)
estados = np.zeros((iter+1,N+2),dtype=int)

#Estado inicial
estados[0,int(N/2)] = 1

vecinos = np.array([[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]],dtype=int)

for i in range(7,-1,-1):
    if regla % 2 == 1:
        regla_bin[i] = 1
    elif regla % 2 == 0:
        regla_bin[i] = 0
    regla = int(regla/2)

print(regla_bin)

fig, ax = plt.subplots()

for i in range(iter):
    for j in range(1,N+1):
        estado_ = estados[i,j-1:j+2]
        for k in range(8):
            if (estado_ == vecinos[k,:]).all():
                estados[i+1,j] = regla_bin[k] 
                break

    #Condiciones de frontera periodicas
    estados[i+1,0] = estados[i+1,N]
    estados[i+1,N+1] = estados[i+1,1]

    ax.cla()
    ax.imshow(estados[:,1:N]*0.5)
    ax.set_title("Generación {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)
plt.show()


