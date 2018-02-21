# -*- coding: ISO-8859-1 -*-
import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt
soundFile = '../../MATERIAL/HD_02_MATLAB/sound_01.wav'           # Especifica do local e nome do arquivo de �udio

dFa,vtSom = wv.read(soundFile)                                   # Abre arquivo de �udio de um arquivo
# vtSom: amplitude das amostras de som
# dFa: frequ�ncia de amostrasgem do som (amostragem no tempo)

dta = 1/dFa                                                      # Tempo entre amostras
dTFinal = (len(vtSom)-1)*dta                                     # Tempo da �ltima amostra do sinal de �udio
vtTSom = np.arange(0,dTFinal+dta,dta)                            # Eixo temporal do arquivo de �udio
plt.figure(1,[10,7])
plt.plot(vtTSom,vtSom)                                           # Plota gr�fico do �udio

#font = {'family' : 'DejaVu Sans','weight' : 'bold','size': 12}   #Configura a fonte do t�tulo
#plt.rc('font', **font)
plt.title('Sinal de �udio')                                      # Configura t�tulo do gr�fico
plt.ylabel('Amplitude')                                          # Configura eixo X do gr�fico
plt.xlabel('Tempo (s)')                                          # Configura eixo Y do gr�fico
plt.ylim([-32000,25000])
plt.show()

# Reproduz arquivo de �udio
os.system('cvlc --play-and-exit ../../MATERIAL/HD_02_MATLAB/sound_01.wav')           
# Mostra informa��es gerais sobre o arquivo
print('Amostragem:')
print(' Taxa de amostragem = ',dFa,' Hz')
print(' Tempo entre amostras = ',dta,' Segundos')
print(' ')
print('Quantiza�ao e Codifica�ao:')
print(' ')
print('Informa��es gerais do arquivo de �udio:')
print(' N�mero de canais = ',vtSom.shape)  
print(' N�mero de amostras = ',len(vtSom),' amostras')
print(' Dura�ao = ',len(vtSom)*dta,' segundos')