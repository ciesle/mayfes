#include <Servo.h>//サーボのためのライブラリ
Servo left, right;
void setup() {
	left.attach(6);
	right.attach(10);
	left.write(180);
	right.write(12);
}

void loop() {
	left.write(180);
	right.write(12);
	delay(5000);
	left.write(30);
	right.write(42);
	delay(1000);
	left.write(30);
	right.write(12);
	delay(1000);
	left.write(90);
	right.write(42);
	delay(1000);
	left.write(150);
	right.write(102);
	delay(1000);
	left.write(90);
	right.write(102);
	delay(1000);
}