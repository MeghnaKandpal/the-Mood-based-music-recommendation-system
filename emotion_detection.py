from deepface import DeepFace
import cv2

def detect_emotion_from_face():
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture your emotion.")
    frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image. Exiting...")
            break

        cv2.imshow('Press "q" to capture your emotion', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    try:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = DeepFace.analyze(frame, actions=['emotion'])
        emotion = result['dominant_emotion']
        return emotion
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return "neutral"
