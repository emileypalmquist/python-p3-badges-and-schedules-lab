def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def room_maker(name, room):
    return f"Hello, {name}! You'll be assigned to room {room}!"


def assign_rooms(names):
    return [room_maker(name, index + 1) for index, name in enumerate(names)]


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for room_assignment in assign_rooms(names):
        print(room_assignment)
