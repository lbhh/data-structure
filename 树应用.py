import operator

from pythonds.basic.stack import Stack
def evaluate(parseTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC)) #递归调用
    else:
        return parseTree.getRootVal()


def buildParseTree(fpliset):

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
