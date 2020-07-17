from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)




# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with dirtions to walk
# traversal_path = ['n', 'n']

traversal_path = []
room_cache = {} # keeps a cache of all the visited rooms

def travel(player, dir=''):
    if len(room_cache) == 500: # end function when 500 rooms visited
        return room_cache

    exits = player.current_room.get_exits()
    id = player.current_room.id

    # loop through possible exits. if not in the cache, it gets added to the possible directions to travel
    # 
    for i in exits:
        if id not in room_cache:
            room_cache[id] = {i: '?'}

        elif i not in room_cache[id]:
            room_cache[id][i] = '?'


    # keeps a record of the way to return to the previous room. N becomes S, S becomes N, E becomes W, W becomes E
    if dir == "n" or dir == "s" or dir == "e" or dir == "w":
        back = ""
        if dir == "n":
            back = "s"
        elif dir == "s":
            back = "n"
        elif dir == "e":
            back = "w"
        elif dir == "w":
            back = "e"

        last = player.current_room.get_room_in_direction(back)
        room_cache[id][back] = last.id
    
    # set the default next direction to ?.
    new_dir = '?'

    # loop through possible exits again. If the direction exists in the cache move to that room if it is a valid move.
    for i in exits:
        if room_cache[id][i] == '?':
            new_dir = i
            player.travel(i)
            traversal_path.append(i)
            new_room = player.current_room.id
            room_cache[id][i] = new_room
            travel(player, i)
            
            
    
    # if there is a way to exit without backtracking, use bfs to travel to the next room 
    move_path = []
    q = Queue()

    if new_dir == '?':
        q.enqueue([id])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            current = path[len(path)-1]

            if current not in visited:
                visited.add(current)
                
                if '?' in room_cache[current].values():
                    move_path = path
                    
                else:
                    for k in room_cache[current].values():
                        new_path = list(path)
                        new_path.append(k)
                        q.enqueue(new_path)

    for i in move_path:
        room = player.current_room.id

        for j in room_cache[room].keys():
            if room_cache[room][j] == i:
                player.travel(j)
                traversal_path.append(j)
    
    travel(player)

travel(player)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
#player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
