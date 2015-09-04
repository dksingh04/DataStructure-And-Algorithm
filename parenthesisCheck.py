from pythond.basic.stack.Stack import Stack

def paraenthesisCheck(parenthesisSympbol):
	s = Stack()
	matched = True
	index = 0
	while index < len(parenthesisSympbol) and matched:
		symbol = parenthesisSympbol[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				matched = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					matched = False
					
		index = index + 1

	if matched and s.isEmpty():
		return True
	else:
		return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(paraenthesisCheck('((()))'))
print(paraenthesisCheck('(()'))
print(paraenthesisCheck('{{([][])}()}'))
print(paraenthesisCheck('[{()]'))


