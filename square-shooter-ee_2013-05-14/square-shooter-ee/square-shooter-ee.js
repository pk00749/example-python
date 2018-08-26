// Square Shooter Enhanced Edition - an abstract Asteroids-like game in HTML5
// 2013-04-25 Felix Pleșoianu <felixp7@yahoo.com>
//
// requestAnimationFrame shim courtesy of the three.js library.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.


var SquareShooter = function () {

"use strict";

var Vector2D = function (x, y) {
	this.x = x;
	this.y = y;
	
	this.incr = function (vector) {
		this.x += vector.x;
		this.y += vector.y;
	}
	
	this.decr = function (vector) {
		this.x -= vector.x;
		this.y -= vector.y;
	}
	
	this.copy = function (vector) {
		this.x = vector.x;
		this.y = vector.y;
	}
};

var Bubble2D = function (radius) {
	this.position = new Vector2D(0, 0);
	this.speed = new Vector2D(0, 0);
	this.radius = radius;
	
	this.update = function (delta_t) {
		this.position.x += this.speed.x * delta_t;
		this.position.y += this.speed.y * delta_t;
	}
	
	this.wrap_around = function () {
		var pos = this.position;
		if (pos.x < 0) pos.x = 1;
		if (pos.y < 0) pos.y = 1;
		if (pos.x > 1) pos.x = 0;
		if (pos.y > 1) pos.y = 0;
	}

	this.is_out = function () {
		var pos = this.position;
		return pos.x < 0 || pos.y < 0 || pos.x > 1 || pos.y > 1;
	}
	
	this.collides_with = function (bubble) {
		var a = Math.abs(this.position.x - bubble.position.x);
		var b = Math.abs(this.position.y - bubble.position.y);
		var distance = Math.sqrt(a * a + b * b);
		return distance < (this.radius + bubble.radius);
	}
};

var random_position = function() {
	return (Math.random() - 0.5) * 3 + 0.5;
};
		
var random_speed = function (magnitude) {
	return (Math.random() * magnitude * 2 - magnitude);
};

var make_bubble = function (type) {
	if (type == "big") {
		var size = 0.1;
		var speed = 0.1;
	} else if (type == "medium") {
		var size = 0.075;
		var speed = 0.15;
	} else if (type == "small") {
		var size = 0.05;
		var speed = 0.25;
	}
	
	var new_bubble = new Bubble2D(size);
	new_bubble.position =
		new Vector2D(random_position(), random_position());
	new_bubble.speed =
		new Vector2D(random_speed(speed), random_speed(speed));
	new_bubble.type = type;
	return new_bubble;
};

var GameWorld = function () {
	this.bubbles = [];
	this.explosions = [];
	this.powerups = [];
	this.bullet = null;
	this.ship = null;
	
	this.accel_x = this.accel_y = 0;
	
	this.move_timer = this.death_timer = this.finish_timer = 0;
	this.ship_shield_timer = this.bullet_shield_timer = 0;
	this.freeze_timer = 0;
	
	this.level = this.score = 0;
	this.high_score = this.max_level = 0;
	this.lives = 0;
		
	var powerup_types = ["shield", "bullet", "freeze"];
	
	this.onrespawn =
		this.onshoot =
		this.onbubblehit
		this.onshiphit =
		this.onpowerup = function () {};

	this.init_level = function (level) {
		this.level = level;
		if (level > this.max_level) this.max_level = level;
		if (this.ship == null) {
			this.ship = new Bubble2D(1 / 25);
			this.onrespawn();
		}
		this.ship.position = new Vector2D(0.5, 0.5);
		this.ship.speed = new Vector2D(0, 0);
		this.bullet = null;
		this.accel_x = this.accel_y = 0;
		this.move_timer = this.death_timer = 0;
		this.finish_timer = 0;
		this.ship_shield_timer = 6;
		this.bullet_shield_timer = 0;
		this.freeze_timer = 0;
		
		this.bubbles.length = 0;
		this.explosions.length = 0;
		this.powerups.length = 0;
		for (var i = 0; i < level; i++) {
			this.bubbles[i] = make_bubble("big");
		}
	};

	this.update = function (delta_t) {
		this.handle_collisions(delta_t);
		
		if (this.explosions.length > 0) {
			if (this.explosions[0].radius > 0.5)
				this.explosions.shift();
		}
		for (var i = 0; i < this.explosions.length; i++) {
			this.explosions[i].radius += delta_t;
		}
		
		if (this.powerups.length > 0) {
			if (this.powerups[0].age > 9)
				this.powerups.shift();
		}
		for (var i = 0; i < this.powerups.length; i++) {
			this.powerups[i].age += delta_t;
		}
		if (this.ship_shield_timer > 0)
			this.ship_shield_timer -= delta_t;
		if (this.bullet_shield_timer > 0)
			this.bullet_shield_timer -= delta_t;
		if (this.freeze_timer > 0)
			this.freeze_timer -= delta_t;
		
		if (this.bubbles.length == 0) {
			if (this.finish_timer > 0) {
				this.finish_timer -= delta_t
			} else {
				this.level++;
				this.lives++;
				this.init_level(this.level);
				return;
			}
		} else if (this.freeze_timer <= 0) {
			for (var i = 0; i < this.bubbles.length; i++) {
				var bubble = this.bubbles[i];
				bubble.update(delta_t);
				bubble.wrap_around();
			}
		}

		if (this.bullet != null) {
			this.bullet.update(delta_t);
			if (this.bullet.is_out()) {
				this.bullet = null;
			}
		}

		if (this.ship == null) {
			if (this.death_timer > 0) {
				this.death_timer -= delta_t;
			} else if (this.lives > 0) {
				this.ship = new Bubble2D(1 / 25);
				this.ship.position = new Vector2D(0.5, 0.5);
				this.ship_shield_timer = 6;
				
				this.onrespawn();
			} else {
				this.level = 0; // Game over
			}
			return;
		}
		
		this.ship.speed.x += this.accel_x;
		this.ship.speed.y += this.accel_y;
		this.ship.speed.x *= 0.99;
		this.ship.speed.y *= 0.99;
		this.ship.update(delta_t);
		this.ship.wrap_around();
	};

	this.handle_collisions = function (delta_t) {
		for (var i = 0; i < this.bubbles.length; i++) {
			var b = this.bubbles[i];
			if (this.bullet != null
					&& b.collides_with(this.bullet)) {
				this.bubbles.splice(i, 1);
				if (this.bullet_shield_timer <= 0) {
					this.bullet = null;
				} else {
					this.bullet.update(delta_t * 5);
				}
				this.spawn_bubbles(b);
				this.spawn_explosion(b);
				this.mark_score(b);
				if (this.bubbles.length == 0) {
					this.finish_timer = 3;
				}
				break;
			} else if (this.ship != null
					&& b.collides_with(this.ship)
					&& this.ship_shield_timer <= 0) {
				this.spawn_explosion(this.ship);
				this.ship = null;
				this.lives--;
				this.death_timer = 3;
				this.onshiphit();
				break;
			}
		}

		if (this.ship == null) return;
		for (var i = 0; i < this.powerups.length; ) {
			var p = this.powerups[i];
			if (p.collides_with(this.ship)) {
				this.apply_powerup(p);
				this.powerups.splice(i, 1);
			} else {
				i++;
			}
		}
	};

	this.spawn_bubbles = function (parent) {
		if (parent.type == "small") {
			if (Math.random() < 0.25)
				this.spawn_powerup(parent);
		} else {
			if (parent.type == "big") {
				var new_type = "medium";
			} else if (parent.type == "medium") {
				var new_type = "small";
			}
			var b = make_bubble(new_type);
			b.position.copy(parent.position);
			this.bubbles.push(b);
			b = make_bubble(new_type);
			b.position.copy(parent.position);
			this.bubbles.push(b);
		}
	};
	
	this.spawn_explosion = function (bubble) {
		var explosion = new Bubble2D(0);
		explosion.position.copy(bubble.position);
		this.explosions.push(explosion);
	};
	
	this.spawn_powerup = function (bubble) {
		var powerup = new Bubble2D(0.03);
		powerup.position.copy(bubble.position);
		powerup.type = powerup_types[Math.floor(Math.random() * 3)];
		powerup.age = 0;
		this.powerups.push(powerup);
	};
	
	this.mark_score = function(bubble) {
		if (bubble.type == "small") {
			this.score += 5;
		} else if (bubble.type == "medium") {
			this.score += 2;
		} else if (bubble.type == "big") {
			this.score += 1;
		}
		if (this.score > this.high_score)
			this.high_score = this.score;
		this.onbubblehit(bubble);
	};
	
	this.apply_powerup = function (powerup) {
		switch (powerup.type) {
			case "shield":
				this.ship_shield_timer += 6;
				break;
			case "bullet":
				this.bullet_shield_timer += 6;
				break;
			case "freeze":
				this.freeze_timer += 6;
				break;
			default:
				throw "Bad powerup type";
		}
		this.score += this.level * 10;
		if (this.score > this.high_score)
			this.high_score = this.score;
		this.onpowerup(powerup);
	};
	
	this.shoot_at = function (x, y) {
		if (this.bullet != null || this.ship == null)
			return;

		x -= this.ship.position.x;
		y -= this.ship.position.y;

		var b = new Bubble2D(0.01);
		b.position.copy(this.ship.position);
		b.speed.x = x * 3;
		b.speed.y = y * 3;

		// Help out the poor sods who click on their
		// own ship and get stuck with a non-moving
		// bullet. (2009-11-14)
		var absx = Math.abs(x);
		var absy = Math.abs(y);
		if (absx < 0.1 && absy < 0.1) {
			b.speed.x *= 30;
			b.speed.y *= 30;
		}
		this.bullet = b;
		
		this.onshoot();
	};
		
	this.thrust_at = function (x, y) {
		if (this.ship == null) return;

		x -= this.ship.position.x;
		y -= this.ship.position.y;
		
		this.accel_x += x * 0.03;
		this.accel_y += y * 0.03;
	};
	
	this.stop_thrust = function () {
		this.accel_x = 0;
		this.accel_y = 0;
	};
};
		

var GameScreen = function (screen, model) {
	this.model = model;
	
	this.screen = screen;

	this.bglayer = document.createElement('canvas');
	this.bglayer.width = screen.width;
	this.bglayer.height = screen.height;

	this.size = Math.min(screen.width, screen.height);
	this.text_size = this.size / 20;
	this.title_size = this.size / 10;

	this.context = screen.getContext('2d');
		
	this.bubble_colors =
		["#ffffcc", "#ffccff", "#ccffff",
		"#ffdddd", "#ddffdd", "#ddddff"];
		
	this.game_paused = false;

	this.render_background = function () {
		var bg = this.bglayer;
		var context = bg.getContext('2d');

		context.fillStyle = "rgb(102, 0, 102)";
		context.fillRect(0, 0, bg.width, bg.height);

		context.fillStyle = "black";
		context.fillRect(0, 0, this.size, this.size);

		context.fillStyle = "#00ff00";
		context.font = this.text_size + "px monospace bold";
		context.textBaseline = "bottom";
		context.textAlign = "left";

		var msg = ["Level:", "Lives:", "Score:"];
		for (var i = 0; i < msg.length; i++) {
			context.fillText(
				msg[i],
				this.text_size,
				bg.height - this.title_size * (i + 1));
		}
	}
	
	this.render_background();
	
	this.recompute_sizes = function () {
		this.bglayer.width = this.screen.width;
		this.bglayer.height = this.screen.height;

		this.size = Math.min(this.screen.width, this.screen.height);
		this.text_size = this.size / 20;
		this.title_size = this.size / 10;
	}

	this.render = function () {
		var ctx = this.context;
		var m = this.model;
		
		ctx.drawImage(this.bglayer, 0, 0);
		
		if (m.level == 0) {
			this.render_title_screen();
		} else {
			this.render_game_world();
			this.render_game_messages();
		}
			
		ctx.fillStyle = "#00ff00";
		ctx.font = this.text_size + "px monospace bold";
		ctx.textBaseline = "bottom";
		ctx.textAlign = "left";
		
		var text_x = this.text_size * 5;
		var h = this.screen.height;

		ctx.fillText(m.level, text_x, h - this.title_size);
		ctx.fillText(m.lives, text_x, h - this.title_size * 2);
		ctx.fillText(m.score, text_x, h - this.title_size * 3);
	}

	this.render_title_screen = function () {
		var ctx = this.context;
		var size = this.size;
		var m = this.model;
		
		ctx.fillStyle = "#00ff00";
		ctx.textAlign = "center";
			
		ctx.font = this.title_size + "px monospace bold";

		ctx.textBaseline = "bottom";
		ctx.fillText("SQUARE", size * 0.5, size * 0.5);
		ctx.textBaseline = "top";
		ctx.fillText("SHOOTER", size * 0.5, size * 0.5);

		ctx.font = this.text_size + "px monospace bold";

		ctx.textBaseline = "bottom";
		ctx.fillText("No Time To Play", size * 0.5, size * 0.25);
		ctx.textBaseline = "top";
		ctx.fillText("presents", size * 0.5, size * 0.25);

		ctx.textBaseline = "bottom";
		ctx.fillText("High score: " + m.high_score,
			size * 0.5, size * 0.75);
		ctx.textBaseline = "top";
		ctx.fillText("Max level: " + m.max_level,
			size * 0.5, size * 0.75);
	}

	this.render_game_world = function () {
		var ctx = this.context;
		var m = this.model;

		ctx.save();
		//ctx.scale(this.size, this.size);
		ctx.beginPath();
		ctx.rect(0, 0, this.size, this.size);
		ctx.clip();
		
		if (m.bullet != null) this.render_bullet();
		if (m.ship != null) this.render_ship();
		
		for (var i = 0; i < m.bubbles.length; i++) {
			var bubble = m.bubbles[i];
			if (!bubble.color) {
				bubble.color = this.bubble_colors[
					Math.floor(Math.random() * 6)];
			}
			this.circle(
				bubble.position.x,
				bubble.position.y,
				bubble.radius,
				bubble.color);
		}
		
		for (var i = 0; i < m.explosions.length; i++) {
			var explosion = m.explosions[i];
			this.circle(
				explosion.position.x,
				explosion.position.y,
				explosion.radius,
				"#ff0000");
		}
		
		for (var i = 0; i < m.powerups.length; i++) {
			this.render_powerup(m.powerups[i]);
		}
		
		ctx.restore();
	}
	
	this.render_ship = function () {
		var ship = this.model.ship;
		var pos = ship.position;
		this.disc(pos.x, pos.y, ship.radius, "#cccccc");
		this.circle(pos.x, pos.y, ship.radius * 0.5, "#000000");
		if (this.model.ship_shield_timer > 0) {
			this.square(pos.x, pos.y, ship.radius, "#cccccc");
		}
	};
	
	this.render_bullet = function () {
		var bullet = this.model.bullet;
		var pos = bullet.position;
		this.disc(pos.x, pos.y, bullet.radius, "#ff0000");
		if (this.model.bullet_shield_timer > 0) {
			this.square(pos.x, pos.y, bullet.radius, "#ff0000");
		}
	};
	
	this.render_powerup = function (powerup) {
		var pos = powerup.position;
		this.square(pos.x, pos.y, powerup.radius, "#ffffff");
		switch (powerup.type) {
			case "shield":
				this.circle(
					pos.x, pos.y,
					powerup.radius,
					"#ffffff");
				break;
			case "bullet":
				this.circle(
					pos.x, pos.y,
					powerup.radius * 0.3,
					"#ffffff");
				break;
			case "freeze":
				this.square(
					pos.x, pos.y,
					powerup.radius * 0.5,
					"#ffffff");
				this.square(
					pos.x, pos.y,
					powerup.radius * 0.25,
					"#ffffff");
				break;
			default:
				throw "Bad power-up type: "
					+ powerup.type;
		}
	};
	
	this.circle = function (x, y, radius, color) {
		var ctx = this.context;
		var s = this.size;

		ctx.strokeStyle = color;
		ctx.beginPath();
		ctx.arc(x * s, y * s, radius * s, 0, Math.PI*2, true);
		ctx.stroke();
	};
	
	this.disc = function (x, y, radius, color) {
		var ctx = this.context;
		var s = this.size;

		ctx.fillStyle = color;
		ctx.beginPath();
		ctx.arc(x * s, y * s, radius * s, 0, Math.PI*2, true);
		ctx.fill();
	};
	
	this.square = function (x, y, radius, color) {
		var ctx = this.context;
		var s = this.size;

		ctx.strokeStyle = color;
		var diameter = radius * 2 * s;
		ctx.strokeRect(
			(x - radius) * s,
			(y - radius) * s,
			diameter, diameter);
	}
	
	this.render_game_messages = function () {
		var ctx = this.context;
		var m = this.model;

		var size = this.size;
		var half = size * 0.5;

		if (m.death_timer > 0 && m.lives == 0) {
			ctx.fillStyle = "#00ff00";
			ctx.textAlign = "center";		
			ctx.font = this.title_size + "px monospace bold";
			ctx.textBaseline = "bottom";
			ctx.fillText("GAME", half, half);
			ctx.textBaseline = "top";
			ctx.fillText("OVER", half, half);
		} else if (this.game_paused) {
			ctx.fillStyle = "#00ff00";
			ctx.textAlign = "center";		
			ctx.font = this.text_size + "px monospace bold";
			ctx.textBaseline = "bottom";
			ctx.fillText("game paused", half, size);
		}
	}
}


var screen = document.createElement('canvas');

var body = document.getElementsByTagName('body')[0];
screen.style.position = 'absolute';
screen.style.top = 0;
screen.style.left = 0;
body.appendChild(screen);

screen.width = window.innerWidth;
screen.height = window.innerHeight;

var model = new GameWorld();
var renderer = new GameScreen(screen, model);

var last_time;

var loop = function (timestamp) {
	if (model.level > 0 && !renderer.game_paused)
		requestAnimationFrame(loop);

	var tick = timestamp - last_time;
	last_time = timestamp;
	
	model.update(tick * 0.001);
	renderer.render();
}

var start = function () {
	model.score = 0;
	model.lives = 1;
	model.init_level(1);

	resume();
};

var resume = function () {
	last_time = Date.now();
	requestAnimationFrame(loop);
	renderer.game_paused = false;
};

var game = {
	model: model,
	renderer: renderer,
	start: start,
	resume: resume,
	muted: false
};

if (Audio) {
	var sounds = {};

	sounds.launch = new Audio("sound/sci-fi-1_2.ogg");
	sounds.laser = [
		new Audio("sound/laser1.ogg"),
		new Audio("sound/laser2.ogg"),
		new Audio("sound/laser3.ogg"),
		new Audio("sound/laser4.ogg"),
		new Audio("sound/laser5.ogg"),
		new Audio("sound/laser6.ogg"),
		new Audio("sound/laser7.ogg"),
		new Audio("sound/laser8.ogg"),
		new Audio("sound/laser9.ogg")];
	sounds.boom = {
		big: new Audio("sound/qubodup-BangLong.ogg"),
		medium: new Audio("sound/qubodup-BangMid.ogg"),
		small: new Audio("sound/qubodup-BangShort.ogg")};
	sounds.dead = new Audio("sound/explodemini.ogg");
	sounds.gameover = new Audio("sound/explode.ogg");
	sounds.powerup = {
		bullet: new Audio("sound/powerUp10.ogg"),
		shield: new Audio("sound/powerUp11.ogg"),
		freeze: new Audio("sound/powerUp12.ogg")};
	
	sounds.launch.volume = 0.6;
	
	model.onrespawn = function () {
		if (!game.muted) sounds.launch.play();
	};
	model.onshoot = function () {
		if (!game.muted)
			sounds.laser[Math.floor(Math.random() * 9)].play();
	};
	model.onbubblehit = function (bubble) {
		if (!game.muted) {
			var boom = sounds.boom[bubble.type].cloneNode();
			boom.volume = 0.5;
			boom.play();
		}
	};
	model.onshiphit = function () {
		if (game.muted)
			return;
		else if (this.lives > 0)
			sounds.dead.play();
		else
			sounds.gameover.play();
	}
	model.onpowerup = function (powerup) {
		if (!game.muted) sounds.powerup[powerup.type].play();
	};
}

renderer.render();

window.addEventListener("resize", function () {
	screen.width = window.innerWidth;
	screen.height = window.innerHeight;

	renderer.recompute_sizes();
	renderer.render_background();
	renderer.render();
}, false);

window.addEventListener("blur", function (event) {
	if (model.level > 0)
		renderer.game_paused = true;
}, false);

screen.addEventListener("click", function (event) {
	if (model.level == 0) {
		start();
	} else if (renderer.game_paused) {
		resume();
	} else {
		var x = event.layerX || event.offsetX;
		var y = event.layerY || event.offsetY;
		var size = renderer.size;
		if (x > size || y > size)
			renderer.game_paused = true;
	}
}, false);

screen.addEventListener("mousedown", function (event) {
	if (model.level > 0 && !renderer.game_paused) {
		var x = event.layerX || event.offsetX;
		var y = event.layerY || event.offsetY;
		var size = renderer.size;
		model.shoot_at(x / size, y / size);
		model.thrust_at(x / size, y / size);
	}
}, false);

screen.addEventListener("mouseup", function (event) {
	if (model.level > 0)
		model.stop_thrust();
}, false);

screen.addEventListener("touchstart", function (event) {
	if (model.level > 0 && !renderer.game_paused) {
		var x = event.touches[0].clientX;
		var y = event.touches[0].clientY;
		var size = renderer.size;
		model.shoot_at(x / size, y / size);
		model.thrust_at(x / size, y / size);
	}
}, false);

screen.addEventListener("touchend", function (event) {
	if (model.level > 0)
		model.stop_thrust();
}, false);

return game;

};


// requestAnimationFrame shim courtesy of the three.js library.

// http://paulirish.com/2011/requestanimationframe-for-smart-animating/
// http://my.opera.com/emoller/blog/2011/12/20/requestanimationframe-for-smart-er-animating

// requestAnimationFrame polyfill by Erik Möller
// fixes from Paul Irish and Tino Zijdel

(function () {
	var lastTime = 0;
	var vendors = [ 'ms', 'moz', 'webkit', 'o' ];

	for (var x=0; x<vendors.length && !window.requestAnimationFrame; ++x) {
		window.requestAnimationFrame =
			window[ vendors[x] + 'RequestAnimationFrame' ];
		window.cancelAnimationFrame =
			window[ vendors[x] + 'CancelAnimationFrame' ]
			|| window[ vendors[x] + 'CancelRequestAnimationFrame' ];

	}

	if (window.requestAnimationFrame === undefined) {
		window.requestAnimationFrame = function (callback, element) {
			var currTime = Date.now();
			var timeToCall =
				Math.max(0, 16 - (currTime - lastTime));
			var id = window.setTimeout(
				function () { callback(currTime+timeToCall); },
				timeToCall);
			lastTime = currTime + timeToCall;
			return id;
		};
	}

	window.cancelAnimationFrame =
		window.cancelAnimationFrame
			|| function (id) { window.clearTimeout(id) };
}());
