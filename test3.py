import speech_recognition
import pyttsx3
import serial  # Thư viện giao tiếp Serial
import time

class VirtualAssistant:
    def __init__(self):
        # Khởi tạo các đối tượng cho nhận diện giọng nói và phát âm
        self.robot_ear = speech_recognition.Recognizer()
        self.robot_mouth = pyttsx3.init()
        self.robot_brain = ""

        # Biến trạng thái LED
        self.led_states = {"LED 1": False, "LED 2": False, "LED 3": False, "LED 4": False}

        # Kết nối với Arduino
        try:
            self.arduino = serial.Serial('COM3', 9600, timeout=1)  # Thay 'COM3' bằng cổng kết nối Arduino
            time.sleep(2)  # Chờ Arduino khởi động
            print("Kết nối Arduino thành công!")
        except serial.SerialException:
            self.arduino = None
            print("Không thể kết nối với Arduino. Kiểm tra lại cổng kết nối.")

    def listen_voice(self):
        while True:
            with speech_recognition.Microphone() as mic:
                # Điều chỉnh theo tiếng ồn môi trường
                self.robot_ear.adjust_for_ambient_noise(mic, duration=1)
                print("Trợ lý ảo: I'm listening...")

                try:
                    audio = self.robot_ear.listen(mic, timeout=10, phrase_time_limit=7)
                    print("Trợ lý ảo: Đang nhận diện...")
                    you = self.robot_ear.recognize_google(audio, language="en-US").lower()
                    print(f"You: {you}")
                except speech_recognition.WaitTimeoutError:
                    print("Trợ lý ảo: Không nghe thấy gì, thử lại.")
                    continue
                except speech_recognition.UnknownValueError:
                    print("Trợ lý ảo: Không nghe rõ, thử lại.")
                    continue
                except speech_recognition.RequestError:
                    print("Lỗi: Không thể kết nối đến dịch vụ nhận diện.")
                    continue

                # Xử lý lệnh giọng nói
                self.handle_voice_command(you)

    def handle_voice_command(self, you):
        if "turn on light one" in you:
            self.led_states["LED 1"] = True
            self.robot_brain = "LED one has been turned on"
            self.send_command_to_arduino("LED1_ON")
        elif "turn off light one" in you:
            self.led_states["LED 1"] = False
            self.robot_brain = "LED one has been turned off"
            self.send_command_to_arduino("LED1_OFF")
        elif "turn on light two" in you:
            self.led_states["LED 2"] = True
            self.robot_brain = "LED two has been turned on"
            self.send_command_to_arduino("LED2_ON")
        elif "turn off light two" in you:
            self.led_states["LED 2"] = False
            self.robot_brain = "LED two has been turned off"
            self.send_command_to_arduino("LED2_OFF")
        elif "turn on light three" in you:
            self.led_states["LED 3"] = True
            self.robot_brain = "LED three has been turned on"
            self.send_command_to_arduino("LED3_ON")
        elif "turn light led three" in you:
            self.led_states["LED 3"] = False
            self.robot_brain = "LED three has been turned off"
            self.send_command_to_arduino("LED3_OFF")
        elif "turn on all light" in you:
            self.led_states = {key: True for key in self.led_states}
            self.robot_brain = "All LEDs have been turned on"
            self.send_command_to_arduino("ALL_LED_ON")
        elif "turn off all light" in you:
            self.led_states = {key: False for key in self.led_states}
            self.robot_brain = "All LEDs have been turned off"
            self.send_command_to_arduino("ALL_LED_OFF")
        else:
            self.robot_brain = "I can't hear you, please try again"

        # Hiển thị trạng thái LED và nói
        self.update_status()

    def send_command_to_arduino(self, command):
        """Gửi lệnh điều khiển đến Arduino."""
        if self.arduino:
            try:
                self.arduino.write(f"{command}\n".encode('utf-8'))
                print(f"Đã gửi lệnh tới Arduino: {command}")
            except serial.SerialException:
                print("Lỗi: Không thể gửi lệnh tới Arduino.")

    def update_status(self):
        print(f"Trợ lý ảo: {self.robot_brain}")
        print(f"Trạng thái LED: {self.led_states}")
        self.speak(self.robot_brain)

    def speak(self, text):
        self.robot_mouth.say(text)
        self.robot_mouth.runAndWait()

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.listen_voice()
