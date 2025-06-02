"""
Código para cargar un vídeo con los componentes electrónicos
y hacer la predicción usando el modelo entrenado
"""

import cv2
from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO(r"C:\Users\elram\OneDrive\Escritorio\electroCom_yolov5m8\weights\best.pt")

# Ruta del video de entrada y salida
entrada = r"C:\Users\elram\OneDrive\Escritorio\Electronic Components Detector YOLO\video_test_2.mp4"
salida = r"C:\Users\elram\OneDrive\Escritorio\Electronic Components Detector YOLO\video_test_2_boxes.mp4"

# Abrir video de entrada
cap = cv2.VideoCapture(entrada)

# Obtener propiedades del video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Crear objeto para guardar el video con las bounding boxes generadas para cada objeto
fourcc = cv2.VideoWriter_fourcc(*'mp4')
out = cv2.VideoWriter(salida, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar las predicciones por frame
    results = model(frame)[0]

    # Dibujar las bounding boxes en el frame
    annotated_frame = results.plot()

    # Escribir el frame anotado sobre el video de salida
    out.write(annotated_frame)

# Liberar los recursos de cv2
cap.release()
out.release()
cv2.destroyAllWindows()
