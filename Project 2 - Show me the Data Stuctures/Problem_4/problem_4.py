class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user == group.get_name():
        return True
    elif user in group.get_users():
        return True
    else:
        for group in group.get_groups():
            return is_user_in_group(user, group)

    return False


#####     #####
#   Testing   #
#####     #####


# Test case 1 / General Working I/O
print("\n",  "#"*10, " - Test Case 1 - ", "#"*10, "\n")


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

child.add_user('vamsi')
parent.add_user('pradeep')

print(is_user_in_group('vamsi', parent))  # True
print(is_user_in_group('pradeep', parent))  # True
print(is_user_in_group('sandy', parent))  # False


# Test case 2 / Searching a user in child group
print("\n",  "#"*10, " - Test Case 2 - ", "#"*10, "\n")
print(is_user_in_group('pradeep', child))  # False Because pradeep exists in parent group


# Test case 3 / Searching a user in empty group
print("\n",  "#"*10, " - Test Case 3 - ", "#"*10, "\n")
print(is_user_in_group('pradeep', Group("parent")))  # False Because parent group is empty
