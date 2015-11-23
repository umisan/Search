# -*- coding: utf-8 -*-

class Node():
    def __init__(self):
        self._nodeName = ""
        self._branch = []
        self._heuristic = 0
        self._weight = 0

    def setName(self, name):
        self._nodeName = name

    def setBranch(self, child):
        branch = Branch()
        branch.setParent(self)
        branch.setChild(child)
        self._branch.append(branch)

    def setHeuristic(self, value):
        self._heuristic = value

    def setWeight(self, weight):
        self._weight = weight

    def getName(self):
        return self._nodeName

    def getBranchList(self):
        return self._branch

class Branch():
    def __init__(self):
        self._parent = None
        self._child = None

    def setParent(self, parent):
        self._parent = parent

    def setChild(self, child):
        self._child = child

    def getParent(self):
        return self._parent

    def getChild(self):
        return self._child
