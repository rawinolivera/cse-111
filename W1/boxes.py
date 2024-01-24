import math

man_items = int(input("Tell the number of manufactured items: "))
items_per_box = int(input("Number of items per box: "))

num_boxes = math.ceil(man_items / items_per_box)

print(f"You need {num_boxes} of boxes.")