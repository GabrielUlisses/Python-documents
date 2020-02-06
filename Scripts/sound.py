import winsound as ws
import time

for i in range(0,2):
    ws.Beep(500,1000)
    time.sleep(2)

#ws.PlaySound('audio.mp3',winsound.SND_FILENAME) puxando audio pelo nome
#ws.PlaySound('audio.mp3',winsound.SND_ALIAS + winsound.SND_FILENAME) 
'''
"SystemAsterisk"
"SystemExclamation"
"SystemExit"
"SystemHand"
"SystemQuestion"
'''
#SND_LOOP - toca o som repetidamente
#SND_PURGE - para todas as instâncias do som
#SND_NODEFAULT - não toca o som default em caso de excessão
#SND_NOSTOP - não interrompe o som tocado
#SND_ASYNC - permite o som tocar de fundo
#SND_LOOP

ws.MessageBeep(ws.MB_ICONEXCLAMATION)
#MB_ICONASTERISK
#MB_ICONHAND
#MB_ICONQUESTION
#MB_OK
