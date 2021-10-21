# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler,
        # this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_list, handler=None, node=None):
        # Similar to our previous example you will want to..
        # recursively add nodes
        # Make sure you assign the handler to only the leaf..
        # (deepest) node of this path
        if node is None:
            node = self.root

        if len(path_list) == 1:
            node.children[path_list[0]] = RouteTrieNode(handler)
            return
        else:
            if not path_list[0] in node.children:
                node.children[path_list[0]] = RouteTrieNode()
            node = node.children[path_list[0]]
            self.insert(path_list[1:], handler, node)

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for i in path_list:
            if node.children.get(i):
                node = node.children[i]
            else:
                return
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode...
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = handler

    def insert(self, path, handler):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found
        # responses as well!
        self.routes = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path="", handler=None):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # Modifiy Root Handler
        if path == "" or path in ["/", "//"] or path is None:
            if handler is None:
                self.routes.root.handler = None
            else:
                self.routes.root.handler = handler
            return
        # Add Custom Roots
        path_list = self.split_path(path)
        self.routes.insert(path_list, handler)

    def lookup(self, path=None):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if path is None or len(path) == 0 or path in ['/', '//']:
            return self.routes.root.handler

        path_list = self.split_path(path)
        handler = self.routes.find(path_list)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path=""):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(path) == 0 or path is None:
            return []

        if path[0] == '/':
            path = path[1:]
        if path[-1] == '/':
            path = path[:-1]

        return path[1:].split('/')


#####     #####
#   Testing   #
#####     #####

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this


# Test Case 1
print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print("Path :", "", "Handler :", router.lookup(""))  # should print 'root handler'
print("Path :", "/", "Handler :", router.lookup("/"))  # should print 'root handler'
print("Path :", "/home", "Handler :", router.lookup("/home"))  # should print 'root handler'
print("Path :", "/home/about", "Handler :", router.lookup("/home/about"))  # should print 'about handler'
print("Path :", "home/about", "Handler :", router.lookup("home/about"))  # should print 'about handler'
print("Path :", "/home/about/", "Handler :", router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print("Path :", "/home/about/me", "Handler :", router.lookup("/home/about/me"))  # should print 'not found handler'

# Test Case 2
print("\n", "#"*8, " - Test Case 2 [Empty/Null Values] - ", "#"*8, "\n")
router.add_handler("", "modified root handler")  # add a route
print("Path :", "", "Handler :", router.lookup(""))  # should print 'modified root handler'
router.add_handler("")  # add a route
print("Path :", "", "Handler :", router.lookup(""))  # should print None becase root handler is not avaliable

# Test Case 3
print("\n", "#"*8, " - Test Case 3 [Trailing Slashes] - ", "#"*8, "\n")
router.add_handler("//", "modified root handler")  # add a route
print("Path :", "//", "Handler :", router.lookup("//"))  # should print 'modified handler'
print("Path :", "/home/about/", "Handler :", router.lookup("/home/about/"))  # should print 'about handler'
