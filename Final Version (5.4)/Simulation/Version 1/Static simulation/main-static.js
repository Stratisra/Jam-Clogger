// set up canvas
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;

const x_velocity = 1;
const y_velocity = 1;
const display_speed = 200; //1000 = 1 second

const arrow_1_1 = new Image();
arrow_1_1.src = "green_curved1.png";
const arrow_1_2 = new Image();
arrow_1_2.src = "green-L_to_R_H.jpg";

const arrow_2_1 = new Image();
arrow_2_1.src = "green_curved2.png";

const arrow_3_1 = new Image();
arrow_3_1.src = "green_curved3.png";
const arrow_3_2 = new Image();
arrow_3_2.src = "green-R_to_L_H.jpg";

const arrow_4_1 = new Image();
arrow_4_1.src = "green_curved4.png";

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
	ctx.strokeText(LigntNo, x-4, y+5);
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
	  //ctx.strokeText(this.x+"/"+this.y, this.x+500, this.y);
      ctx.beginPath();
      ctx.fillStyle = this.color;
	  if (this.orientation == 0) {
		ctx.fillRect(this.x, this.y, 50,20);
	  }
	  else { 
		ctx.fillRect(this.x, this.y, 20,50);
	  }
      ctx.fill();	  
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

//Create queues
var Cars1 = [];
var Cars2 = [];
var Cars3 = [];
var Cars4 = [];

function drawstate(timestamp) {
	ctx.strokeStyle = "white";
	ctx.lineWidth = 1;
	ctx.font = "16px arial";
	ctx.strokeText("State "+ s + "/" + total_states + ": " + Cars1.length + " - " + Cars2.length + " - "  + Cars3.length + " - "  + Cars4.length, 50, 50);

//Draw Lane 1
i = 1;
   for (const Car of Cars1) {
    Car.draw();
	if (Car.orientation == 0){
//		Car.move_L_to_R();
	 }
	else { 
//		Car.move_U_to_D();
	 }
	 
	 if (Car.x>=860 && i%2==0){
//		 Car.orientation = 1;
	 }
	 
	 if (Car.x>=1400){
//		Cars1.shift(); 
	 }
//	 Car.collisionDetect();
	 i++;
   }
   
//Draw Lane 2
i = 1;
   for (const Car of Cars2) {
    Car.draw();
	 i++;
   }   

//Draw Lane 3
i = 1;
   for (const Car of Cars3) {
    Car.draw();
	 i++;
   }   

//Draw Lane 4
i = 1;
   for (const Car of Cars4) {
    Car.draw();
	 i++;
   }   

} //end of drawstate function


s=0;
(function() {
	// main program to loop the animation
	// Source: http://www.paulirish.com/2011/requestanimationframe-for-smart-animating/
	// shim layer with setTimeout fallback
	window.requestAnimFrame = (function(){
  		return  window.requestAnimationFrame       ||
          window.webkitRequestAnimationFrame ||
          window.mozRequestAnimationFrame    ||
          function( callback ){
            window.setTimeout(callback, 1000 / 60);
          };
	})();

	var lastTime = (new Date()).getTime();
	var displayNode = document.getElementById('display');
	var numSeconds = 0;
	(function timer() {
		requestAnimFrame(timer);
		var currentTime = (new Date()).getTime();

		if (currentTime - lastTime >= display_speed && s < total_states) {

			console.log("Last Time: " + lastTime);
			console.log("Current Time: " + currentTime);

			lastTime = currentTime;
			numSeconds++;

		// ************* Display next State ********************
					
			ctx.clearRect(0, 0, width, height);
			ctx.fillStyle = 'rgba(0, 0, 0, 0.95)';
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
	   
			const State = Traffic_States[s];
			
			if (State.transition>=0 && State.transition <=9 ){
				Traffic_Light(1, 835,520, "lightgreen"); 
				ctx.drawImage(arrow_1_1, 845, 480, 40,40);
				ctx.drawImage(arrow_1_2, 845, 450, 50,50);
			} //light-green or red
			else {Traffic_Light(1, 835,520, "red");}

			if (State.transition>=5 && State.transition <=9 || State.transition>=15 && State.transition <=19){
				Traffic_Light(2, 835,400, "lightgreen");
				ctx.drawImage(arrow_2_1, 845, 400, 40,40);
				} //light-green or red
			else {Traffic_Light(2, 835,400, "red");}

			if (State.transition>=0 && State.transition <=4 || State.transition>=10 && State.transition <=14){
				Traffic_Light(3, 965,285, "lightgreen");
				ctx.drawImage(arrow_3_1, 915, 285, 40,40);
				ctx.drawImage(arrow_3_2, 905, 305, 50,50);
				} //light-green or red
			else {Traffic_Light(3, 965,285, "red");}
			
			if (State.transition>=10 && State.transition <=19 ){
				Traffic_Light(4, 965,400, "lightgreen");
				ctx.drawImage(arrow_4_1, 915, 375, 40,40);
				} //light-green or red
			else {Traffic_Light(4, 965,400, "red");}

			//Lane 1: fill from next State
			while (Cars1.length > 0){Cars1.pop();} // emtpy
			i = 1;
			if (Cars1.length < State.lane1){
				while (Cars1.length < State.lane1) {
				   const size = 60;
				   const Car = new car(
					 835 - i * size, 460, //Lane 1 position
					  x_velocity, y_velocity, randomRGB(),size, 0, "stop", s*i
				   );
				  Cars1.push(Car);
				  i++;
				}
			}

			//Lane 2: fill from next State
			while (Cars2.length > 0){Cars2.pop();} // emtpy
			i = 1
			if (Cars2.length < State.lane2){
				while (Cars2.length < State.lane2) {
				   const size = 60;
				   const Car = new car(
					 835 - i * size, 430, //Lane 2 position
					 x_velocity, y_velocity, randomRGB(), size, 0, "stop", s*i 
				   );

				  Cars2.push(Car);
				  i++;
				}
			}	

			//Lane 3: fill from next State
			while (Cars3.length > 0){Cars3.pop();} // emtpy
			i = 1;
			if (Cars3.length < State.lane3){
				while (Cars3.length < State.lane3) {
				   const size = 60;
				   const Car = new car(
					 910 + i * size, 315, //Lane 3 position
					  x_velocity, y_velocity, randomRGB(),size, 0, "stop", s*i
				   );
				  Cars3.push(Car);
				  i++;
				}
			}

			//Lane 4: fill from next State
			while (Cars4.length > 0){Cars4.pop();} // emtpy
			i = 1;
			if (Cars4.length < State.lane4){
				while (Cars4.length < State.lane4) {
				   const size = 60;
				   const Car = new car(
					 910 + i * size, 350, //Lane 4 position
					  x_velocity, y_velocity, randomRGB(),size, 0, "stop", s*i
				   );
				  Cars4.push(Car);
				  i++;
				}
			}

			drawstate();
			s++;
			
			if (s>=total_states){
					window.clearInterval();
			}
		// ************* Display next frame ********************

		}
	}());
}());


