import cv2
from pyzbar.pyzbar import decode
from warnings import filterwarnings

filterwarnings(action='ignore')

def qr_code_scanner():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            continue

        try:
            decoded_objects = decode(frame)
        except Exception as e:
            print("Error:", e)
            continue

        cv2.imshow("QR Code Scanner", frame)

        if decoded_objects:

            for obj in decoded_objects:

                qr_data = obj.data.decode()

                print("QR Code Detected:")
                print(qr_data)

                cap.release()
                cv2.destroyAllWindows()

                return qr_data

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    qr_code_scanner()
