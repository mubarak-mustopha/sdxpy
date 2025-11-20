import math

def density(thing, weight):
    return weight / call(thing, "area")

def shape_new(name):
    return {
            "name": name,
            "_class": Shape
    }

Shape = {
    "density": density,
    "_classname": "Shape",
    "_parent": None,
    "_new": shape_new,
}

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

def square_larger(thing, size):
    return call(thing, "area") > size

def square_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Square 
    }

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "larger": square_larger,
    "_classname": "Square",
    "_parent": Shape,
    "_new": square_new
}

def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return math.pi * thing["radius"] ** 2

def circle_larger(thing, size):
    return call(thing, "area") > size

def circle_new(name, radius):
    return make(Shape, name) | {
        "radius": radius,
        "_class": Circle
    }

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "larger": circle_larger,
    "_classname": "Circle ",
    "_parent": Shape, 
    "_new": circle_new
}

def call(thing, method_name, *args, **kwargs):
    method = find(thing["_class"], method_name)
    return method(thing, *args, **kwargs)

def make(cls, *args, **kwargs):
    return cls["_new"](*args, **kwargs)

def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError(method_name)


examples = [square_new("sq", 3), circle_new("ci", 2)]
for ex in examples:
    n = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex, "area")
    c = ex["_class"]["_classname"]
    d = call(ex, "density", 5)
    print(f"{n} is a {c}: {p:.2f} {a:.2f} with density {d:.2f}")
    result = call(ex, "larger", 10)
    print(f"is {ex['name']} larger? {result}")
