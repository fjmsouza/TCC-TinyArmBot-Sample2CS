// inclui bibilioteca do servomotor
#include <Servo.h>

// define pinos dos servos
#define pinServ1 3
#define pinServ2 5
#define pinServ3 6

// define as portas dos potenciometros
#define intervalo 500

// nomeia os servos
Servo jointBase, jointRight, jointLeft, jointGrip;

// cria as variavies dos angulos de cada motor
int jointGradeBase, jointGradeLeft, jointGradeRight, jointGradeGrip;

void home();
void posicaoSeguranca();

void setup() {

  //inicia o monitor serial
  Serial.begin(9600);

  // atribui pinos dos servos
  jointBase.attach(pinServ1);
  jointRight.attach(pinServ2);
  jointLeft.attach(pinServ3);
  home();
  posicaoSeguranca();

}


void loop() {
 
  if (Serial.available() > 0) {
    char incomingString = Serial.read();
    stateMachine(incomingString);
  }
    
}

void stateMachine(char incomingString){

  switch (incomingString) {
    case '0':
      teclaZero();
      break;
    case '1':
      teclaUm();
      break;
    case '2':
      teclaDois();
      break;
    case '3':
      teclaTres();
      break;
    case '4':
      teclaQuatro();
      break;
    case '5':
      teclaCinco();
      break;
    case '6':
      teclaSeis();
      break;
    case '7':
      teclaSete();
      break;
    case '8':
      teclaOito();
      break;
    case '9':
      teclaNove();
      break;
    case 'G':
      teclaCorrige();
      break;
    case 'C':
      teclaConfirma();
      break;
    case 'H':
      home();
      break;
    case 'S':
      posicaoSeguranca();
      break;
    default:
      break;

  }
}

void home(){

  jointBase.write(88);
  jointRight.write(82);
  jointLeft.write(163);
  delay(intervalo);
}

void posicaoSeguranca(){
  jointBase.write(93);
  jointRight.write(93);
  jointLeft.write(115);
  delay(intervalo);
  
  // jointBase.write(91);
  // jointRight.write(93);
  // jointLeft.write(144);
  // delay(intervalo);
}

void teclaUm(){

  jointBase.write(100);
  jointRight.write(127);
  jointLeft.write(140);
  delay(intervalo);

  jointBase.write(100);
  jointRight.write(127);
  jointLeft.write(117);
  delay(intervalo);

  jointBase.write(100);
  jointRight.write(127);
  jointLeft.write(140);
  delay(intervalo);

}

void teclaDois(){

  jointBase.write(89);
  jointRight.write(127);
  jointLeft.write(140);
  delay(intervalo);

  jointBase.write(89);
  jointRight.write(127);
  jointLeft.write(117);
  delay(intervalo);

  jointBase.write(89);
  jointRight.write(127);
  jointLeft.write(140);
  delay(intervalo);

}

void teclaTres(){

  jointBase.write(79);
  jointRight.write(127);
  jointLeft.write(140);
  delay(intervalo);

  jointBase.write(79);
  jointRight.write(127);
  jointLeft.write(117);
  delay(intervalo);

  jointBase.write(79);
  jointRight.write(127);
  jointLeft.write(140);
  delay(intervalo);

}

void teclaQuatro(){

  jointBase.write(103);
  jointRight.write(115);
  jointLeft.write(128);
  delay(intervalo);

  jointBase.write(103);
  jointRight.write(115);
  jointLeft.write(108);
  delay(intervalo);

  jointBase.write(103);
  jointRight.write(115);
  jointLeft.write(128);
  delay(intervalo);

}

void teclaCinco(){

  jointBase.write(89);
  jointRight.write(115);
  jointLeft.write(128);
  delay(intervalo);

  jointBase.write(89);
  jointRight.write(115);
  jointLeft.write(108);
  delay(intervalo);

  jointBase.write(89);
  jointRight.write(115);
  jointLeft.write(128);
  delay(intervalo);

}

void teclaSeis(){

  jointBase.write(75);
  jointRight.write(115);
  jointLeft.write(128);
  delay(intervalo);

  jointBase.write(75);
  jointRight.write(115);
  jointLeft.write(108);
  delay(intervalo);

  jointBase.write(75);
  jointRight.write(115);
  jointLeft.write(128);
  delay(intervalo);

}

void teclaSete(){

  jointBase.write(105);
  jointRight.write(104);
  jointLeft.write(119);
  delay(intervalo);

  jointBase.write(105);
  jointRight.write(104);
  jointLeft.write(98);
  delay(intervalo);

  jointBase.write(105);
  jointRight.write(104);
  jointLeft.write(119);
  delay(intervalo);

}

void teclaOito(){

  jointBase.write(90);
  jointRight.write(104);
  jointLeft.write(119);
  delay(intervalo);

  jointBase.write(90);
  jointRight.write(104);
  jointLeft.write(98);
  delay(intervalo);

  jointBase.write(90);
  jointRight.write(104);
  jointLeft.write(119);
  delay(intervalo);

}

void teclaNove(){

  jointBase.write(74);
  jointRight.write(104);
  jointLeft.write(119);
  delay(intervalo);

  jointBase.write(74);
  jointRight.write(104);
  jointLeft.write(98);
  delay(intervalo);

  jointBase.write(74);
  jointRight.write(104);
  jointLeft.write(119);
  delay(intervalo);

}

void teclaZero(){

  jointBase.write(93);
  jointRight.write(93);
  jointLeft.write(115);
  delay(intervalo);

  jointBase.write(93);
  jointRight.write(93);
  jointLeft.write(90);
  delay(intervalo);

  jointBase.write(93);
  jointRight.write(93);
  jointLeft.write(115);
  delay(intervalo);

}

void teclaCorrige(){

  jointBase.write(118);
  jointRight.write(93);
  jointLeft.write(115);
  delay(intervalo);

  jointBase.write(118);
  jointRight.write(93);
  jointLeft.write(90);
  delay(intervalo);

  jointBase.write(118);
  jointRight.write(93);
  jointLeft.write(115);
  delay(intervalo);

}

void teclaConfirma(){

  jointBase.write(67);
  jointRight.write(95);
  jointLeft.write(115);
  delay(intervalo);

  jointBase.write(67);
  jointRight.write(95);
  jointLeft.write(90);
  delay(intervalo);

  jointBase.write(67);
  jointRight.write(95);
  jointLeft.write(115);
  delay(intervalo);

}


