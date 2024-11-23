// Khai báo các chân LED
const int ledPin1 = 2;
const int ledPin2 = 3;
const int ledPin3 = 4;
const int ledPin4 = 5;

void setup() {
  // Cài đặt các chân LED làm đầu ra
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);

  // Bắt đầu giao tiếp Serial với tốc độ 9600
  Serial.begin(9600);
}

void loop() {
  // Kiểm tra nếu có dữ liệu từ Serial
  if (Serial.available() > 0) {
    // Đọc chuỗi lệnh từ Serial
    String command = Serial.readStringUntil('\n');
    command.trim();  // Loại bỏ các khoảng trắng hoặc ký tự xuống dòng

    // Kiểm tra các lệnh nhận được
    if (command == "LED1_ON") {
      digitalWrite(ledPin1, HIGH);
    } else if (command == "LED1_OFF") {
      digitalWrite(ledPin1, LOW);
    } else if (command == "LED2_ON") {
      digitalWrite(ledPin2, HIGH);
    } else if (command == "LED2_OFF") {
      digitalWrite(ledPin2, LOW);
    } else if (command == "LED3_ON") {
      digitalWrite(ledPin3, HIGH);
    } else if (command == "LED3_OFF") {
      digitalWrite(ledPin3, LOW);
    } else if (command == "ALL_LED_ON") {
      // Bật tất cả các LED
      digitalWrite(ledPin1, HIGH);
      digitalWrite(ledPin2, HIGH);
      digitalWrite(ledPin3, HIGH);
      digitalWrite(ledPin4, HIGH);
    } else if (command == "ALL_LED_OFF") {
      // Tắt tất cả các LED
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
      digitalWrite(ledPin3, LOW);
      digitalWrite(ledPin4, LOW);
    }
  }
}
