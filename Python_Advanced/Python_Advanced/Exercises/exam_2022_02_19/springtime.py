def start_spring(**kwargs):
    objects = {}
    result = []

    for name, object_type in kwargs.items():
        if object_type not in objects:
            objects[object_type] = []
        objects[object_type].append(name)

    objects = sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))

    for object_type, names in objects:
        names.sort()
        names_part = '\n-'.join(names)
        result.append(f"{object_type}:\n-{names_part}")

    return '\n'.join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

