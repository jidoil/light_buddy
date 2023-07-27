from maya import cmds
import math
import random


def get_distance(position_1, position_2):
    x1, y1, z1 = position_1
    x2, y2, z2 = position_2

    distance = math.sqrt(
        math.pow(x2 - x1, 2) +
        math.pow(y2 - y1, 2) +
        math.pow(z2 - z1, 2)
    )
    return distance


def make_random_distanced_sphere(count, distance):
    def check(new_position):
        for position in all_position:
            if get_distance(new_position, position) < distance:
                return True
        return False

    all_position = []
    ranges = (-10, 10)
    for c in range(count):
        new_position = (
            random.uniform(*ranges),
            random.uniform(*ranges),
            random.uniform(*ranges)
        )

        if all_position:
            check_count = 0
            while check(new_position):
                new_position = (
                    random.uniform(*ranges),
                    random.uniform(*ranges),
                    random.uniform(*ranges)
                )
                check_count += 1
                if check_count == 100:
                    return

        all_position.append(new_position)
        sp_ = cmds.sphere(radius=0.5)
        cmds.move(*list(new_position) + sp_[:1])


make_random_distanced_sphere(100, 5)
