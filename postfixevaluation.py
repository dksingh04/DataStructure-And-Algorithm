from pythond.basic.stack.Stack import Stack
def postFixEvaluation(postfixExpression):
	opStack = Stack()
	tokenList = postfixExpression.split()
	for token in tokenList:
		if token not in "*+-/==":
			opStack.push(int(token))
		else:
			operand2 = opStack.pop()
			operand1 = opStack.pop()
			result = doMath(token, operand1, operand2)
			opStack.push(result)

	return opStack.pop()

def doMath(token, operand1, operand2):
	if token == "*":
		return operand1 * operand2
	elif token == "/":
		return operand1 / operand2
	elif token == "+":
		return operand1 + operand2
	elif token == "-":
		return operand1 - operand2

print(postFixEvaluation('7 8 + 3 2 + /'))
print(postFixEvaluation('10 3 5 * 16 4 - / +'))
print(postFixEvaluation('17 10 + 3 * 9 /'))

