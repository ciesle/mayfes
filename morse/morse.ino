// C++ code
//
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(32, 16, 2);

const int SWITCH=2,EXEC=3;
const long BORDER_TIME=200;
const long ENTER_TIME=1000;
bool history[20];
int history_size;
const char morse[][6]={
  {0,1,-1}, //a
  {1,0,0,0,-1}, //b
  {1,0,1,0,-1}, //c
  {1,0,0,-1}, //d
  {0,-1}, //e
  {0,0,1,0,-1}, //f
  {1,1,0,-1}, //g
  {0,0,0,0,-1}, //h
  {0,0,-1}, //i
  {0,1,1,1,-1}, //j
  {1,0,1,-1}, //k
  {0,1,0,0,-1}, //l
  {1,1,-1}, //m
  {1,0,-1}, //n
  {1,1,1,-1}, //o
  {0,1,1,0,-1}, //p
  {1,1,0,1,-1}, //q
  {0,1,0,-1}, //r
  {0,0,0,-1}, //s
  {1,-1}, //t
  {0,0,1,-1}, //u
  {0,0,0,1,-1}, //v
  {0,1,1,-1}, //w
  {1,0,0,1,-1}, //x
  {1,0,1,1,-1}, //y
  {1,1,0,0,-1}, //z
  {1,1,1,1,1,-1}, //0
  {0,1,1,1,1,-1}, //1
  {0,0,1,1,1,-1}, //2
  {0,0,0,1,1,-1}, //3
  {0,0,0,0,1,-1}, //4
  {0,0,0,0,0,-1}, //5
  {1,0,0,0,0,-1}, //6
  {1,1,0,0,0,-1}, //7
  {1,1,1,0,0,-1}, //8
  {1,1,1,1,0,-1}, //9
};
const int CHAR_CNT=36;
char buffer[120];
volatile int buffer_size;

void setup(){
  Serial.begin(9600);
  Wire.begin();
  lcd.init();

  lcd.setCursor(0, 0);
  lcd.clear();
  lcd.backlight();
  lcd.display();
  
  pinMode(SWITCH,INPUT_PULLUP);
  pinMode(EXEC,INPUT_PULLUP);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  for(int i=0x21;i<=0x23;i++){
    Wire.beginTransmission(i);
    Wire.write(0);
    Wire.endTransmission();
  }
  
  //attachInterrupt(digitalPinToInterrupt(RESET),reset,CHANGE);
}
void execute(){
  for(int i=0;i<buffer_size;i++){
    int chip_id=-1;
    int led=-1;
    if('A'<=buffer[i]&&buffer[i]<='H'){
      chip_id=0x21;
      led=1<<(buffer[i]-'A');
    }
    else if('I'<=buffer[i]&&buffer[i]<='P'){
	  chip_id=0x22;
      led=1<<(buffer[i]-'I');
    }
    else if('Q'<=buffer[i]&&buffer[i]<='X'){
	  chip_id=0x23;
      led=1<<(buffer[i]-'Q');
    }
    else if(buffer[i]=='Y'){
	  led=4;
    }
    else if(buffer[i]=='Z'){
	  led=5;
    }
    if(led>=0){
      if(chip_id>=0){
	Wire.beginTransmission(chip_id);
        Wire.write(led);
        Wire.endTransmission();
        Serial.println(chip_id);
        Serial.println(led);
      }
      else{
	digitalWrite(led,HIGH);
      }
      delay(1000);
      if(chip_id>=0){
	Wire.beginTransmission(chip_id);
        Wire.write(0);
        Wire.endTransmission();
      }
      else{
		digitalWrite(led,LOW);
      }
    }
  }
  
  buffer_size=0;
  buffer[buffer_size]=0;
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(buffer);
}

void blink(){
  static long start=0;
  static bool status=false;
  if(!status&&digitalRead(SWITCH)==LOW){
	status=true;
    start=millis();
  }
  if(status&&digitalRead(SWITCH)){
	status=false;
    long now=millis();
    history[history_size++]=(now-start>BORDER_TIME);
  }
}
void enter(){
  for(int i=0;i<history_size;i++){
	Serial.println(history[i]);
  }
  for(int i=0;i<CHAR_CNT;i++){
    bool flag=true;
    for(int j=0;;j++){
      //モースコードの走査完了
      if(morse[i][j]==-1){
        if(history_size!=j)flag=false;
        break;
      }
      //historyが短すぎた
      if(history_size==j){
        flag=false;
        break;
      }
      flag&=((morse[i][j]==1)==history[j]);
    }
    if(flag){
      if(i<26) buffer[buffer_size++]='A'+i;
      else buffer[buffer_size++]='0'+i;
      buffer[buffer_size]=0;
    }
  }
  history_size=0;
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(buffer);
}


void loop(){
  blink();
  static long off_time=0;
  if(digitalRead(SWITCH)&&off_time==0) off_time=millis();
  else if(digitalRead(SWITCH)==LOW) off_time=0;
  for(int i=0;i<history_size;i++){
	if(i<history_size-1) Serial.print(history[i]);
    else Serial.println(history[i]);
  }
  if(history_size&&off_time>0&&millis()-off_time>ENTER_TIME){
	enter();
  }
  if(digitalRead(SWITCH)&&digitalRead(EXEC)==LOW){
	execute();
  }
  delay(10);
}
