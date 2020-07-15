import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Add friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
    
    def get_friendships(self, user):
        friends = []
        for i in self.friendships:
            for j in self.friendships[i]:
                if j == user:
                    friends.append(i)
        return friends
    
    def get_path(self, starting_vertex, destination_vertex):
        path = []
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last_vert = path[-1]
            
            if last_vert not in visited:
                if last_vert == destination_vertex:
                    return path

                else:
                    visited.add(last_vert)

                for neighbor in self.get_friendships(last_vert):
                    copypath = path.copy()
                    copypath.append(neighbor)
                    q.enqueue(copypath)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
          # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        network = []
        q1 = Queue()
        q1visited = set()
        q1.enqueue(user_id)
        while q1.size() > 0:
            v = q1.dequeue()
            if v not in q1visited:
                q1visited.add(v)
                q1.enqueue(v)
                network.append(v)
                for next_vert in self.get_friendships(v):
                    q1.enqueue(next_vert)
        for friend in network:
            print(f"Network from User {user_id} to User {friend}: {self.get_path(user_id, friend)}")
        

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)


# Find all users in the specified user's extended network
# find path to each user
