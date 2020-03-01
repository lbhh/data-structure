def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':  #表达式开始
            currentTree.insertLeft('')
            pStack.push(currentTree)  #入栈下降
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:  #操作数
            currentTree.setRootVal(int(i))
            parent = pStack.pop()  #出栈上升，pop出来一个节点
            currentTree = parent
        elif i in ['+','-','*','/']:  #操作符
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':   #表达式结束
            currentTree = pStack.pop() #出栈上升
        else:
            raise ValueError
    return eTree
