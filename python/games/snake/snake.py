from ursina import *
import random


app = Ursina()

window.color = color.black
camera.orthographic = True
camera.fov = 1

SCALE = (.01, .01, .01)
COLLIDER = 'box'
MODEL = 'quad'


class Food(Entity):
    food_eat = False
    _from = None
    
    def __init__(self, **kwags) -> None:
        super().__init__(self, **kwags)
        self.time_of_creation = time.time()

    def set_food_eat(self):
        self.food_eat = True

    def get_food_eat(self):
        return self.food_eat 


class Snack(Entity):
    tail = []
    tail_distance = .02
    time_reset = True
    move_foward = True
    velocity = 0.005
    pause = False

    def __init__(self, **kwags) -> None:
        super().__init__(self, **kwags)
        self.color = hsv(0, 1, 1)
        self.switche_movementations(foward=True)
    
    def set_pause(self):
        self.pause = True
        self.velocity = 0
    
    def switche_movementations(self, foward=False, down=False, right=False, left=False):
        self.move_foward = foward
        self.move_down = down
        self.move_right = right
        self.move_left = left

    def move_snake(self):
        if self.time_reset:
            self.init_time = time.time()
        else:
            pass

        # snacke direction
        if held_keys['w'] or held_keys['up arrow']:
            self.switche_movementations(foward=True)
        elif held_keys['s'] or held_keys['down arrow']:
            self.switche_movementations(down=True)
        elif held_keys['d'] or held_keys['right arrow']:
            self.switche_movementations(right=True)
        elif held_keys['a'] or held_keys['left arrow']:
            self.switche_movementations(left=True)
        
        # snack movimentation
        
        if self.move_foward:
            self.y = self.y + self.velocity
        elif self.move_down:
            self.y = self.y - self.velocity
        elif self.move_right:
            self.x = self.x + self.velocity
        elif self.move_left:
            self.x = self.x - self.velocity

        # screen limiations
        if self.move_foward and self.y >= .5:
            self.y = -.5
        elif self.move_down and self.y <= -.5:
            self.y = .5
        elif self.move_right and self.x >= .9:
            self.x = -.9
        elif self.move_left and self.x <= -.9:
            self.x = .9

        self.move_food(self.pause)
    
    def add_tail(self, food: Food):
        self.tail.append(food)
    
    def enable_tail(self):
        for t in self.tail:
            if t.disable:
                t.disable = False

    def set_tail_piece_position(self, piece):
        _distante = self.tail_distance

        if self.move_foward:
            piece.x = self.x - .0
            piece.y = self.y - _distante
        elif self.move_down:
            piece.x = self.x -.0
            piece.y = self.y + _distante
        elif self.move_right:
            piece.y = self.y - .0
            piece.x = self.x - _distante
        elif self.move_left:
            piece.y = self.y - .0
            piece.x = self.x + _distante
        
        return piece

    def move_food(self, pause):
        if not pause:
            self.time_reset = False
            time_total = time.time() - self.init_time
            if time_total >= 0.1:
                if self.tail:
                    self.time_reset = True
                    ponta: Food = self.tail.pop()
                    if ponta.disable:
                        ponta.disable = False
                    self.tail.insert(0, self.set_tail_piece_position(ponta))
                    


class Game:
    theend = False
    paused = False

    def __init__(self) -> None:
        self.snake = Snack(model=MODEL, scale=SCALE, collider=COLLIDER, speed=0, color=(0, .30, .5)) 
        self.last_food_creation = time.time()
        self.food_list=[Food(model=MODEL, scale=SCALE, collider=COLLIDER, speed=0, x=.3, y=.3)]
        self.paused = False
    
    def create_food(self):
        if time.time() >= self.last_food_creation + 3:
            self.last_food_creation = time.time()
            f = Food(model=MODEL, scale=SCALE, collider=COLLIDER, speed=0, x=random.randint(-6, 6)/10, y=random.randint(-4, 4)/10)
            self.food_list.append(f)

    def instersection_verifier(self):
        for f in self.food_list:
            if f.intersects().hit:
                if not f.food_eat:
                    f.disable = True
                    f.food_eat = True
                    self.snake.add_tail(f)
                elif not f.disable and f.food_eat:
                        self.game_over()

    
    def game_over(self):
        self.paused = True
        self.theend = True
        # stop snack
        self.snake.set_pause()
        # stop tail
        # show text of game over
        pass

    def verify_food_destruction(self):
        to_remove = None
        for f in self.food_list:
            if f is not None and f.food_eat == False and time.time() >= f.time_of_creation + 6:
                to_remove = f
    
        if to_remove:
            self.food_list.remove(to_remove)
            to_remove.disable()

g = Game()

def update():
    g.snake.move_snake()

    g.create_food()
    g.instersection_verifier()
    g.verify_food_destruction()


app.run()
