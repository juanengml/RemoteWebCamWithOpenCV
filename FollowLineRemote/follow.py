import cv2
import numpy as np
import urllib


LimiarBinarizacao = 125       #este valor eh empirico. Ajuste-o conforme sua necessidade 
AreaContornoLimiteMin = 5000  #este valor eh empirico. Ajuste-o conforme sua necessidade 
url = "http://192.168.100.6:8080/shot.jpg"
imgResp =  urllib.urlopen(url)

def Img():
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    return True,img

def TrataImagem(img):
    height = np.size(img,0)
    width= np.size(img,1)
    QtdeContornos = 0
    DirecaoASerTomada = 0
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    FrameBinarizado = cv2.threshold(gray,LimiarBinarizacao,255,cv2.THRESH_BINARY)[1]
    FrameBinarizado = cv2.dilate(FrameBinarizado,None,iterations=2)
    FrameBinarizado = cv2.bitwise_not(FrameBinarizado)
    _, cnts, _ = cv2.findContours(FrameBinarizado.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,cnts,-1,(255,0,255),3)
    for c in cnts:
      if cv2.contourArea(c) < AreaContornoLimiteMin:
          continue
      QtdeContornos = QtdeContornos + 1
      (x, y, w, h) = cv2.boundingRect(c)
      cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
      CoordenadaXCentroContorno = (x+x+w)/2
      CoordenadaYCentroContorno = (y+y+h)/2
      PontoCentralContorno = (CoordenadaXCentroContorno,CoordenadaYCentroContorno)
      cv2.circle(img, PontoCentralContorno, 1, (0, 0, 0), 5)
      DirecaoASerTomada = CoordenadaXCentroContorno - (width/2)   #em relacao a linha central
    cv2.line(img,(width/2,0),(width/2,height),(255,0,0),2)
    if (QtdeContornos > 0):
        cv2.line(img,PontoCentralContorno,(width/2,CoordenadaYCentroContorno),(0,255,0),1)
    #cv2.imshow('Analise de rota DA OBR',img)
    cv2.waitKey(10)
    return DirecaoASerTomada, QtdeContornos


"""
camera = cv2.VideoCapture("simulacao.mp4")
camera.set(3,320)
camera.set(4,240)
#faz algumas leituras de frames antes de consierar a analise
#motivo: algumas camera podem demorar mais para se "acosumar a luminosidade" quando ligam, capturando frames consecutivos com muita variacao de luminosidade. Para nao levar este efeito ao processamento de imagem, capturas sucessivas sao feitas fora do processamento da imagem, dando tempo para a camera "se acostumar" a luminosidade do ambiente
for i in range(0,20):
    (grabbed, Frame) = camera.read()

"""

while True:
    try:
      (grabbed, Frame) = Img()
      if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      if (grabbed):
          Direcao,QtdeLinhas = TrataImagem(Frame)
          if (QtdeLinhas == 0):
             print ("Nenhuma linha encontrada. O robo ira parar.")
             continue
        
          if (Direcao > 0):
              print ("Distancia da linha de referencia: "+str(abs(Direcao))+" pixels a [DIREITA]")
          if (Direcao < 0):
              print ("Distancia da linha de referencia: "+str(abs(Direcao))+" pixels a [ESQUERDA]")
          if (Direcao == 0):
              print ("Exatamente na linha de referencia!")    
    except (KeyboardInterrupt):
          print ("STOP MODA FOCA")
          break;
exit(1)   
