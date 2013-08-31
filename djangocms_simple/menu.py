from menus.base import NavigationNode


class Node(NavigationNode):
    _uid_counter = 0
    def __init__(self, title, url, uid=None, parent=None, attr=None, visible=True):
        if uid is None:
            Node._uid_counter += 1
            uid = Node._uid_counter
        super(Node, self).__init__(title, url, uid, parent.id if parent else None, None, attr, visible)
        self._children = []

    def add_child(self, title, url, uid=None, attr=None, visible=True):
        child = Node(title, url, uid, self, attr, visible)
        self._children.append(child)
        return child

    def _as_list(self):
        nodes = []
        nodes.append(self)
        for child in self._children:
            nodes.extend(child._as_list())
        return nodes

