# Design a graph problem, given an function getFriend(int user) 
# which returns all the users 1st degree friends, write a function to check:

# 1. whether two users are first-level, second-level and third-level connections
# 2. function that outputs a users 2nd degree and 3rd degree friends

class Node:
    def __init__(self, userId):
        self.userId = userId
        self.connections = []
        self.connectedUserIds = set()

class Graph:
    def getFriend(self, user):
        return user.connections

    def getDegreeOfConnectionOfTwoUsers(self, user1, user2):
        if user2 in user1.connections or user1 in user2.connections: 
            return 1
        
        def checkIfUsersAre2ndOr3rdDegreeConnections(user1, user2, degree):
            if degree>2: return -1
            for connection in user1.connections:
                if user2 in connection.connections: return degree+1
            
            for connection in user2.connections: 
                if user1 in connection.connections: return degree+1
            
            for connection in user1.connections:
                return checkIfUsersAre2ndOr3rdDegreeConnections(connection, user2, degree+1)
            
            for connection in user2.connections: 
                return checkIfUsersAre2ndOr3rdDegreeConnections(connection, user1, degree+1)
        
        return checkIfUsersAre2ndOr3rdDegreeConnections(user1, user2, 1)

def createGraph():
    nodes = [Node(i) for i in range(10)]
    for i in range(10):
        for j in range(i + 1, 10):
            if nodes[j].userId not in nodes[i].connectedUserIds: 
                nodes[i].connections.append(nodes[j])
                nodes[i].connectedUserIds.add(nodes[j].userId)

            if nodes[i].userId not in nodes[j].connectedUserIds: 
                nodes[j].connections.append(nodes[i])
                nodes[j].connectedUserIds.add(nodes[i].userId)

            for k in range(j + 1, 10):
                if nodes[k].userId not in nodes[i].connectedUserIds: 
                    nodes[i].connections.append(nodes[k])
                    nodes[i].connectedUserIds.add(nodes[k].userId)

                if nodes[k].userId not in nodes[j].connectedUserIds: 
                    nodes[j].connections.append(nodes[k])
                    nodes[j].connectedUserIds.add(nodes[k].userId)

                if nodes[i].userId not in nodes[k].connectedUserIds: 
                    nodes[k].connections.append(nodes[i])
                    nodes[k].connectedUserIds.add(nodes[i].userId)
                    
                if nodes[j].userId not in nodes[k].connectedUserIds: 
                    nodes[k].connections.append(nodes[j])
                    nodes[k].connectedUserIds.add(nodes[j].userId)
    return nodes

users = createGraph()
graph = Graph()
# for userId in range(10):
#     connections = graph.getFriend(users[userId])
#     for connection in connections: 
#         print("node = ", user, "connection = ", connection.userId)

for userId in range(0,10,2):
    print(graph.getDegreeOfConnectionOfTwoUsers(users[userId],users[userId+1]), "level connection")

user10 = Node(10)
user11 = Node(11)
user12 = Node(12)
users[0].connections.append(user10)
user10.connections.append(user11)

print()
print(graph.getDegreeOfConnectionOfTwoUsers(users[0], user10), "level connection")
print(graph.getDegreeOfConnectionOfTwoUsers(users[1], user10), "level connection")
print(graph.getDegreeOfConnectionOfTwoUsers(users[6], user10), "level connection")

print()
print(graph.getDegreeOfConnectionOfTwoUsers(users[1], user11), "level connection")
print(graph.getDegreeOfConnectionOfTwoUsers(users[8], user11), "level connection")

print()
print(graph.getDegreeOfConnectionOfTwoUsers(users[1], user12), "level connection")
print(graph.getDegreeOfConnectionOfTwoUsers(users[8], user12), "level connection")
