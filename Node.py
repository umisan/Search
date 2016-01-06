# -*- coding: utf-8 -*-

class Node():
    def __init__(self):
        self.nodeName = ""
        self.childBranch = []
        self.parent = None
        self.heuristic = 0
        self.routeCost = 0
        self.start = 0
        self.goal = 0

    def setChildBranch(self, child, weight):
        branch = Branch()
        branch.setParent(self)
        branch.setChild(child)
        branch.weight = weight
        self.childBranch.append(branch)

class Branch():
    def __init__(self):
        self._parent = None
        self._child = None
        self.weight = 0

    def setParent(self, parent):
        self._parent = parent

    def setChild(self, child):
        self._child = child

    def getParent(self):
        return self._parent

    def getChild(self):
        return self._child
