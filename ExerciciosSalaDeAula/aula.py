import cv2

#img = cv2.imread("media\escola2.png")
#cv2.imshow("Nome da Janela",img)
#print("Iniciando um projeto Python")

# Subindo o vídeo
VIDEO_PATH = r"media\race.mp4"
cap = cv2.VideoCapture(VIDEO_PATH)

#Mostrar o vídeo
if not cap.isOpened():
    raise FileNotFoundError(f"Não foi possível carregar o vídeo:{VIDEO_PATH}")

while True:
    ok, frame = cap.read()

    if not ok:
        cap.release()
        raise RuntimeError ("Falha ao carregar o primeiro frame")
        break

    cv2.imshow("Video",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)