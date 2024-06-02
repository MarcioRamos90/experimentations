
const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext('2d');

const CANVAS_WIDTH = canvas.width = window.innerWidth;
const CANVAS_HEIGHT = canvas.height = window.innerHeight;

window.addEventListener('resize', function() {
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
})


class Player {
    constructor(x) {  // Constructor
        this.x = x;
        this.y = 30;
        this.speed = 10;
    }

    draw() {
        ctx.fillRect(this.x, this.y, 5, 20);
        ctx.fill();
    }

    up() {
        if (this.y > 0) {
            this.y -= this.speed;
        }
    }

    down() {
        if (this.y < CANVAS_HEIGHT - 20) {
            this.y += this.speed;
        }
    }

    left() {
        this.x -= this.speed;
    }

    right() {
        this.x += this.speed;
    }
}

p1 = new Player(10 - 5);
p2 = new Player(CANVAS_WIDTH - 10);

function animate() {
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    p1.draw();
    p2.draw();
    requestAnimationFrame(animate);
}

animate()


document.addEventListener('keydown', function(e) {
    switch (e.key) {
        case "ArrowUp":
            p1.up();
            break;
        case "ArrowDown":
            p1.down();
            break;
        case "ArrowLeft":
            p1.left()
            break;
        case "ArrowRight":
            p1.right()
            break;
    }
    switch (e.key) {
        case "w":
            p2.up();
            break;
        case "s":
            p2.down();
            break;
        case "a":
            p2.left()
            break;
        case "d":
            p2.right()
            break;
    }
});