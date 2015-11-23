# -*- coding: utf-8 -*-
import Node
import xml.etree.ElementTree as ET

def searchNode(nodeList, nodeName):
    for node in nodeList:
        if node.getName() == nodeName:
            return node
            break

def main():
    #オープンリストとクローズリスト、ノードリストの宣言
    openList = []
    closeList = []
    nodeList = []

    #xmlから状態空間を読み込む
    tree = ET.parse('state.xml')
    root = tree.getroot()

    #状態空間からノードの生成
    for node in root.findall('node'):
        current = Node.Node()
        name = node.get('name')
        current.setName(name)
        nodeList.append(current)

    #親子関係の設定
    index = 0
    for node in root.findall('node'):
        current = nodeList[index]
        for child in node.findall('child'):
            childName = child.text
            childNode = searchNode(nodeList, childName)
            current.setBranch(childNode)
        index += 1

    for node in nodeList:
        branchList = node.getBranchList()
        print "parent: " + node.getName()
        for branch in branchList:
            print "child: " + branch.getChild().getName()

if __name__ == '__main__':
    main()
