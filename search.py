# -*- coding: utf-8 -*-
import Node
import sys
import xml.etree.ElementTree as ET

def searchNode(nodeList, nodeName):
    for node in nodeList:
        if node.nodeName == nodeName:
            return node
    else:
        return 0

def searchGoalNode(nodeList):
    for node in nodeList:
        if node.goal == 1:
            return node
            break

def branchAndBound(openList, closeList, nodeList):
    #分岐限定法の開始
    #スタートノードの設定
    openList.append(nodeList[0])
    #openlistが空になるまでループ
    while len(openList) != 0:
        node = openList.pop(0)
        if node.goal == 1:
            print u'探索終了'
            print u'総コスト' + str(node.routeCost)
            print u'探索経路'
            while node.parent != None:
                print str(node.nodeName),
                print u" ←",
                node = node.parent
            print node.nodeName
            break
        closeList.append(node)
        #子ノードに対する処理
        for branch in node.childBranch:
            #子ノードの取得
            child = branch.getChild()
            #各リストに子ノードが存在するかの判定
            openHasChild = searchNode(openList, child.nodeName)
            closeHasChild = searchNode(closeList, child.nodeName)
            #コストの計算
            routeCost = node.routeCost + branch.weight
            if openHasChild == 0 and closeHasChild == 0:
                #親ノードとコストの設定
                child.parent = node
                child.routeCost = routeCost
                #openlistに追加
                openList.append(child)
            elif openHasChild != 0:
                if child.routeCost > routeCost:
                    #親ノードとコストの設定
                    child.routeCost = routeCost
                    child.parent = node
        #openlistをソート
        openList.sort(key = lambda node : node.routeCost)

def bestFirst(openList, closeList, nodeList):
    #最優良探索
    #スタートノードの設定
    openList.append(nodeList[0])
    #openlistが空になるまでループ
    while len(openList) != 0:
        node = openList.pop(0)
        if node.goal == 1:
            print u'探索終了'
            print u'総コスト' + str(node.routeCost)
            print u'探索経路'
            while node.parent != None:
                print str(node.nodeName),
                print u' ←',
                node = node.parent
            print node.nodeName
            break
        #ノードをcloseListに追加
        closeList.append(node)
        #子ノードに対する処理
        for branch in node.childBranch:
            #子ノードを取得
            child = branch.getChild()
            #各リストに子ノードが存在するか判定
            openHasChild = searchNode(openList, child.nodeName)
            closeHasChild = searchNode(closeList, child.nodeName)
            #コストの計算
            routeCost = node.routeCost + branch.weight
            if openHasChild == 0 and closeHasChild == 0:
                #コストと親ノードの設定
                child.parent = node
                child.routeCost = routeCost
                #openlistに子ノードを追加
                openList.append(child)
        #openlistをソート
        openList.sort(key = lambda node : node.heuristic )

def Aargorithm(openList, closeList, nodeList):
    #Aアルゴリズム
    #スタートノードの設定
    openList.append(nodeList[0])
    #openlistが空になるまでループ
    while len(openList) != 0:
        node = openList.pop(0)
        if node.goal == 1:
            print u'探索終了'
            print u'総コスト' + str(node.routeCost)
            print u'探索経路'
            while node.parent != None:
                print str(node.nodeName),
                print u' ←',
                node = node.parent
            print node.nodeName
            break
        #ノードをcloseListに追加
        closeList.append(node)
        #子ノードに対する処理
        for branch in node.childBranch:
            #子ノードを取得
            child = branch.getChild()
            #コストを計算
            routeCost = node.routeCost + branch.weight + child.heuristic - node.heuristic
            #各リストに子ノードが存在するか判定
            openHasChild = searchNode(openList, child.nodeName)
            closeHasChild = searchNode(closeList, child.nodeName)
            if openHasChild == 0 and closeHasChild == 0:
                #親ノードと、コストの設定
                child.parent = node
                child.routeCost = routeCost
                #子ノードをopenlistに追加
                openList.append(child)
            elif openHasChild != 0:
                if routeCost < child.routeCost:
                    child.parent = node
                    child.routeCost = routeCost
            elif closeHasChild != 0:
                if routeCost < child.routeCost:
                    child.parent = node
                    child.routeCost = routeCost
                    #子ノードをcloselistから削除し、openlistに追加
                    closeList.remove(child)
                    openList.append(child)
        #openlistをソート
        openList.sort(key = lambda node : node.routeCost)

def hillCliming(nodeList):
    #山登り法
    node = nodeList[0]
    temp = Node.Node()
    while node.goal != 1:
        heuristic = node.childBranch[0].getChild().heuristic
        for branch in node.childBranch:
            child = branch.getChild()
            routeCost = node.routeCost + branch.weight
            if child.heuristic <= heuristic:
                heuristic = child.heuristic
                child.parent = node
                child.routeCost = routeCost
                temp = child
        node = temp
    print u'探索終了'
    print u'総コスト' + str(node.routeCost)
    print u'探索経路'
    while node.parent != None:
        print str(node.nodeName),
        print u' ←',
        node = node.parent
    print node.nodeName

def breadthFirst(openList, closeList, nodeList):
    #横形探索
    #スタートノードの設定
    openList.append(nodeList[0])
    #openlistが空になるまでループ
    while len(openList) != 0:
        node = openList.pop(0)
        if node.goal == 1:
            print u'探索終了'
            print u'総コスト' + str(node.routeCost)
            print u'探索経路'
            while node.parent != None:
                print str(node.nodeName),
                print u' ←',
                node = node.parent
            print node.nodeName
            break
        #親ノードをcloselistに追加
        closeList.append(node)
        for branch in node.childBranch:
            #子ノードの取得
            child = branch.getChild()
            #各リストに子ノードが存在しないか判定
            openHasChild = searchNode(openList, child.nodeName)
            closeHasChild = searchNode(closeList, child.nodeName)
            #コストの計算
            routeCost = node.routeCost + branch.weight
            if openHasChild == 0 and closeHasChild == 0:
                #親ノードとコストの設定
                child.parent = node
                child.routeCost = routeCost
                #ゴールならば先頭、違う場合は末尾に追加
                if child.goal != 1:
                    openList.append(child)
                else:
                    openList.insert(0, child)

def depthFirst(openList, closeList, nodeList):
    #縦形探索
    #スタートノードの設定
    openList.append(nodeList[0])
    #openlistが空になるまでループ
    while len(openList) != 0:
        node = openList.pop(0)
        if node.goal == 1:
            print u'探索終了'
            print u'総コスト' + str(node.routeCost)
            print u'探索経路'
            while node.parent != None:
                print str(node.nodeName),
                print u' ←',
                node = node.parent
            print node.nodeName
            break
        #親ノードをcloselistに追加
        closeList.append(node)
        #子ノードに対する処理
        for branch in node.childBranch:
            #子ノードを取得
            child = branch.getChild()
            #各リストに子ノードが存在するか判定
            openHasChild = searchNode(openList, child.nodeName)
            closeHasChild = searchNode(closeList, child.nodeName)
            #コストの計算
            routeCost = node.routeCost + branch.weight
            if openHasChild == 0 and closeHasChild == 0:
                #親ノードとコストを設定
                child.parent = node
                child.routeCost = routeCost
                #先頭に子ノードを追加
                openList.insert(0, child)
                #ゴールの場合は探索終了
                if child.goal == 1:
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
        attrib = node.attrib
        if 'property' in attrib:
            if attrib['property'] == 'start':
                current.start = 1
            if attrib['property'] == 'goal':
                current.goal = 1
        current.heuristic = int(attrib['heuristic'])
        current.nodeName = name
        nodeList.append(current)

    #親子関係の設定
    index = 0
    for node in root.findall('node'):
        current = nodeList[index]
        for child in node.findall('child'):
            childName = child.text
            childNode = searchNode(nodeList, childName)
            weight = child.attrib
            current.setChildBranch(childNode, int(weight['weight']))
        index += 1

    #分岐限定法の開始
    #branchAndBound(openList, closeList, nodeList)

    #最優良探索
    #bestFirst(openList, closeList, nodeList)

    #Aアルゴリズム
    #Aargorithm(openList, closeList, nodeList)

    #山登り法
    #hillCliming(nodeList)

    #横形探索
    #breadthFirst(openList, closeList, nodeList)

    #縦形探索
    depthFirst(openList, closeList, nodeList)

    print u'最終的なcloselist'
    for node in closeList:
        print node.nodeName

    print u'最終的なopenList'
    for node in openList:
        print node.nodeName



if __name__ == '__main__':
    main()
