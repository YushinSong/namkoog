import json
from obstacle import Obstacle

def create_obstacles():
    obstacle_state_table = {
        "SQUARE": Obstacle.SQUARE,
        "TRIANGLE": Obstacle.TRIANGLE,
        "HALF_SQUARE": Obstacle.HALF_SQUARE,
        "SPIKE": Obstacle.SPIKE,
        "NONE_WALL": Obstacle.NONE_WALL,
        "UP_LEFT_RIGHT": Obstacle.UP_LEFT_RIGHT,
        "UP_LEFT": Obstacle.UP_LEFT,
        "LEFT_RIGHT": Obstacle.LEFT_RIGHT,
        "UP_RIGHT": Obstacle.UP_RIGHT,
        "UP": Obstacle.UP,
        "LEFT": Obstacle.LEFT,
        "RIGHT": Obstacle.RIGHT
    }
    obstacle_data_file = open('ob_data\\obstacle_data.txt', 'r')
    obstacle_data = json.load(obstacle_data_file)
    obstacle_data_file.close()

    obstacle = [][10]
    count = 0
    i = 0
    for name in obstacle_data:
        ob = Obstacle()
        ob.name = name
        ob.x = obstacle_data[name]['x'] - 00
        ob.y = obstacle_data[name]['y']
        ob.shape = obstacle_state_table[obstacle_data[name]['StartState']]
        if ob.x
        obstacle[0][count].append(ob)
        count += 1

    return obstacle