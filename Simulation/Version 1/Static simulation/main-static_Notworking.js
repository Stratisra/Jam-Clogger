// set up canvas
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;

const x_velocity = 1;
const y_velocity = 1;

// function to generate random number
function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// function to generate random RGB color value
function randomRGB() {
  return `rgb(${random(0, 255)},${random(0, 255)},${random(0, 255)})`;
}

// Draw Horizontal line between 2 points
function H_line(x1,y1,x2,y2,w){
	ctx.fillStyle = 'rgba(255, 255, 255, 0.25)';
	ctx.beginPath();
	ctx.moveTo(x1, y1);
	ctx.lineTo(x2, y2);
	ctx.lineTo(x2, y2+w);
	ctx.lineTo(x1, y2+w);
	ctx.fill();	
}
// Draw Vertical line between 2 points
function V_line(x1,y1,x2,y2,w){
	ctx.fillStyle = 'rgba(255, 255, 255, 0.25)';
	ctx.beginPath();
	ctx.moveTo(x1, y1);
	ctx.lineTo(x2, y2);
	ctx.lineTo(x2+w, y2);
	ctx.lineTo(x1+w, y1);
	ctx.fill();	
}

// Draw a colored circle
function Traffic_Light(LigntNo, x,y,color){
	ctx.fillStyle = color;
	ctx.beginPath();
	ctx.arc(x, y, 15, 0, 2 * Math.PI);
	ctx.lineTo(x, y);
	ctx.fill();
	
	ctx.strokeStyle = "black";
	ctx.lineWidth = 1;
	ctx.font = "16px arial";
	ctx.strokeText(LigntNo, x, y);
}

class car {
   constructor(x, y, velX, velY, color, size, orientation, move_stop, id) {
      this.x = x;
      this.y = y;
      this.velX = velX;
      this.velY = velY;
      this.color = color;
      this.size = size;
	  this.orientation = orientation;
	  this.move_stop = move_stop;
	  this.id = id;
   }

   draw() {
      ctx.beginPath();
      ctx.fillStyle = this.color;
	  if (this.orientation == 0) {
		ctx.fillRect(this.x, this.y, 50,20);
	  }
	  else { 
		ctx.fillRect(this.x, this.y, 20,50);
	  }
      ctx.fill();
	  
	  ctx.strokeStyle = "white";
		ctx.lineWidth = 0.2;
		ctx.font = "12px helvetica";
		ctx.strokeText(this.x, this.x, this.y);
		ctx.strokeText(this.y, this.x+10, this.y+30);
		ctx.strokeStyle = "black";
		ctx.lineWidth = 0.8;
		ctx.strokeText(this.id, this.x+10, this.y+15);
   }

   move_L_to_R() {
	  if (this.move_stop == "move") { 
		this.x += this.velX; //move horizontal left->right
	  }
   }

   move_R_to_L() {
      this.x -= this.velX; //move horizontal right->left
   }

   move_D_to_U() {
      this.y -= this.velY; //move vertical Down-->Up
   }

   move_U_to_D() {
      this.y += this.velY; //move vertical Up-->Donw
   }

/*
   collisionDetect() {
      for (const Car of Cars1) {
         if (!(this === Car)) {
            if (this.x > this.size + Car.size + 200) {
				//alert(this.x);
			  Car.move_stop = "stop";
            }
         }
      }
   }
*/

}

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

//Create queues
var Cars1 = [];
var Cars2 = [];

s=1;
function drawstate(timestamp) {

if (s < Traffic_States.length) {
//for (const State of Traffic_States) {
	const State = Traffic_States[s];
	//Lane 1
	i = 1;
	if (Cars1.length < State.lane1){
		while (Cars1.length < State.lane1) {
		   const size = 60;
		   const Car = new car(
			 835 - i * size, 460, //Lane 1 position
			  x_velocity, y_velocity, randomRGB(),size, 0, "stop", s
		   );

		  Cars1.push(Car);
		  i++;
		}
	}
	else {
		while (Cars1.length > State.lane1){
			Cars1.pop(); //Cars1.shift();
			
		}
	}

	i = 1
	if (Cars2.length < State.lane2){
		while (Cars2.length < State.lane2) {
		   const size = 60;
		   const Car = new car(
			 835 - i * size, 430, //Lane 2 position
			 x_velocity, y_velocity, randomRGB(), size, 0, "stop", s 
		   );

		  Cars2.push(Car);
		  i++;
		}
	}	
	else {
		while (Cars2.length > State.lane2){
			Cars2.pop(); //Cars2.shift();
			
		}
	}	




	
   ctx.clearRect(0, 0, width, height);
// black background
   ctx.fillStyle = 'rgba(0, 0, 0, 0.25)';
   ctx.fillRect(0, 0,  width, height);


//Horizontal road
H_line(-10,300,850,300,5);
H_line(950,300,2000,300,5);

H_line(-10,400,850,400,2);
H_line(950,400,2000,400,2);

H_line(-10,500,850,500,5);
H_line(950,500,2000,500,5);

//Vertical road
V_line(850,-10,850,305,3);
V_line(950,-10,950,305,3);

V_line(850,500,850,1300,3);
V_line(950,500,950,1300,3);

Traffic_Light(1, 835,520, "lightgreen"); //light-green or red
Traffic_Light(2, 835,400, "red"); //light-green or red

Traffic_Light(3, 965,285, "lightgreen"); //light-green or red
Traffic_Light(4, 965,400, "red"); //light-green or red


//Draw Lane 1
i = 1;
   for (const Car of Cars1) {
    Car.draw();
	 i++;
   }
   
//Draw Lane 2
i = 1;
   for (const Car of Cars2) {
    Car.draw();
	i++;

   }   

s++;
		

  }
   
   
  requestAnimationFrame(drawstate);

//alert(Cars1.length + " - " + Cars2.length);


}//end of drawstate function





//alert(State.lane1 + " - " + State.lane2 + "    " + Cars1.length + " - " + Cars2.length);

drawstate();
//window.requestAnimationFrame(drawstate);


 //sleep(200);
//setTimeout(() => {  drawstate(); }, 200);

//drawstate();


