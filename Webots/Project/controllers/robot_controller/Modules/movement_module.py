from controller import Robot, Motor
import math

def sign(num):
    return int(math.copysign(1, num))

class Movement():
    robot: Robot = None
    speed: float = 0
        
    right_motor: Motor = None
    left_motor: Motor = None

    def __init__(self, robot: Robot, speed: float):
        self.right_motor = robot.getDevice('right wheel motor')
        self.right_motor.setPosition(float('inf'))
        self.right_motor.setVelocity(0)

        self.left_motor = robot.getDevice('left wheel motor')
        self.left_motor.setPosition(float('inf'))
        self.left_motor.setVelocity(0)

        self.setSpeed(speed)

    def move(self, direction_forward: float, direction_right: float):
        ''' Move the robot in the given direction '''
        # direction_forward and direction_right is alway bewteen -1 and 1

        turnAngle = math.degrees(math.asin(abs(direction_right)))
        turnFactor = turnAngle / 90
        
        if direction_forward != 0:
            if direction_right > 0:
                self.right_motor.setVelocity(self.speed * turnFactor * sign(direction_forward))
                self.left_motor.setVelocity(self.speed * sign(direction_forward))
            elif direction_right < 0:
                self.right_motor.setVelocity(self.speed * sign(direction_forward))
                self.left_motor.setVelocity(self.speed * turnFactor * sign(direction_forward))
            else:
                self.right_motor.setVelocity(self.speed * sign(direction_forward))
                self.left_motor.setVelocity(self.speed * sign(direction_forward))

        else:
            self.right_motor.setVelocity(self.speed * 0.5 * -direction_right)
            self.left_motor.setVelocity(self.speed * 0.5 * direction_right)

    def setSpeed(self, speed: float):
        ''' Set the maximum speed of teh robot '''
        self.speed = speed
