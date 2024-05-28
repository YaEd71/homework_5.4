class Building:

    total = 0

    def __init__(self):

        Building.total += 1

object = []
object_size = 40
while len(object) < object_size:
    new_Building = Building()
    object.append(new_Building)
print(Building.total)
