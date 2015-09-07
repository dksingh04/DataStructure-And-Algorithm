from pythond.basic.stack.Stack import Stack
def infixtoPostFix(infixExpression):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	opStack = Stack()
	postFixList = []
	tokenList = infixExpression.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postFixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ")":
			topToken = opStack.pop()
			while topToken != '(':
				postFixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postFixList.append(opStack.pop())
			
			opStack.push(token)

	while not opStack.isEmpty():
		postFixList.append(opStack.pop())

	return " ".join(postFixList)

print(infixtoPostFix("A * B + C * D"))
print(infixtoPostFix("( A + B ) * C - ( D - E ) * ( F + G )"))
