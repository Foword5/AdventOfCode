import re

class Robot():
    def __init__(self,vel_x, vel_y, room):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.room = room
    
    def move(self, x, y):
        x = (x + self.vel_x) % self.room.width
        y = (y + self.vel_y) % self.room.height
        return x, y
    
    def __str__(self):
        return f'Robot moving at ({self.vel_x}, {self.vel_y})'

class Room():
    @classmethod
    def create_from_file(cls, width, height, file):
        room = cls(width, height)
        with open(file) as f:
            for line in f:
                m =re.match(r'p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line)
                robot = Robot(int(m.group(3)), int(m.group(4)), room)
                room.add_robot(robot, int(m.group(1)), int(m.group(2)))
        return room
        
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robots = [[[] for _ in range(self.width)] for _ in range(self.height)]

    def add_robot(self, robot, x, y):
        self.robots[y][x].append(robot)
        
    def second_pass(self):
        next_robots = [[[] for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                for robot in self.robots[y][x]:
                    m_x, m_y = robot.move(x, y)
                    next_robots[m_y][m_x].append(robot)
        self.robots = next_robots
    
    def get_safety_score(self):
        center_x = self.width // 2
        center_y = self.height // 2
        
        quadrants = [0, 0, 0, 0]
        for x in range(self.width):
            for y in range(self.height):
                if x < center_x and y < center_y:
                    quadrants[0] += len(self.robots[y][x])
                elif x > center_x and y < center_y:
                    quadrants[1] += len(self.robots[y][x])
                elif x < center_x and y > center_y:
                    quadrants[2] += len(self.robots[y][x])
                elif x > center_x and y > center_y:
                    quadrants[3] += len(self.robots[y][x])
                
        return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    
    def look_for_chrismas_tree(self):
        for i in range(self.width):
            for j in range(self.height):
                try :
                    if (self.robots[j][i] and 
                        self.robots[j][i+1] and
                        self.robots[j][i+2] and
                        self.robots[j][i+3] and
                        self.robots[j][i+4] and
                        self.robots[j][i+5] and
                        self.robots[j][i+6] and
                        self.robots[j][i+7]):
                        return True
                except IndexError:
                    pass
        return False
    
    def __str__(self):
        return f'Room of size {self.width, self.height} with {len(self.robots)} robots'
    
    def visualise(self, safe=False):
        center_x = self.width // 2
        center_y = self.height // 2
        
        for y in range(self.height):
            if safe and y == center_y:
                print(' ' * self.width)
                continue
            for x in range(self.width):
                if safe and x == center_x:
                    print(' ', end='')
                    continue
                robot_at_position = self.robots[y][x]
                if robot_at_position:
                    print(len(robot_at_position), end='')
                else:
                    print('.', end='')
            print()
        print()