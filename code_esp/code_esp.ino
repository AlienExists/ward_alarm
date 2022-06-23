#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
const char* ssid = "SSID"; // SSID WiFi точки
const char* password = "PASSWORD"; // Пароль
const char* host = "192.168.50.253"; 
const char* port = "8888";
String url = "/call/";
// Номер порта кнопки
int button = 2;

void setup() {
  // Подключение кнопки
  pinMode(button, INPUT_PULLUP);
  Serial.begin(115200);
  delay(10);
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  // Режим wifi модуля - клиент
  WiFi.mode(WIFI_STA);
  // Подключение к WiFi точке
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
// Флаг для не нажатой кнопки. Позволяет использовать кнопку с фиксацией либо тумблер, при этом функция сработает один раз или будет работать через установленный интервал времени, когда кнопка зажата
bool flag = false;
// Таймер
uint32_t btnTimer = 0;

void loop() {
  // Логическое состояние кнопки
  bool btnState = !digitalRead(button);
  // При нажатии кнопки
  if (btnState && !flag && millis() - btnTimer > 10000) {
    flag = true;
    btnTimer = millis();
    Serial.print("connecting to ");
    Serial.println(host);
    // Устанавливается TCP соединение с сервером
    WiFiClient client;
    // Порт на котором запущено приложение
    const int httpPort = 8888;
    if (!client.connect(host, httpPort)) {
      Serial.println("connection failed");
      return; }
    // Данные POST. Содержит номер койки и статус (тревога)
    String postData = "bed_id=5&status=alarm";
    HTTPClient http;
    // Отправление HTTP-Запроса на сервер
    http.begin(client, "http://192.168.50.253:8888/call");
    //
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    auto httpCode = http.POST(postData);
    Serial.println(httpCode);
    String payload = http.getString();
    Serial.println(payload);
    http.end();
    Serial.println("closing connection");
  }
  if (!btnState && flag && millis() - btnTimer > 10000) {  // обработчик отпускания
    flag = false;
    btnTimer = millis();
  }
}