# History:
# 2018-02-04 - JL - create node class
#                 - create singleLinkedList class
#                 - create singleLinkedLIst methods: nNodes, printLinkedList, returnValue, appendNode, insertNode
#                                                    popLinkedList, deleteNode, __reachLinkedListPos

class node:
	
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

class singleLinkedList:

	def __init__(self, value):
		self.__startNode = node(value)
		self.__nNodes = 1

	@property
	def nNodes(self):
		nNodes = self.__nNodes
		return nNodes

	def printLinkedList(self):
		# set current node and position to be beginning of linked list
		currentNode = self.__startNode
		currentPos = 1

		nodeStr = ""

		# loop through all nodes by printing out the value of the current node
		# set current node to be the next node
		while currentNode != None:
			currentStr = "[ " + str(currentPos) + " | " + str(currentNode.value) + " ]-->"
			nodeStr = nodeStr + currentStr

			currentPos += 1
			currentNode = currentNode.nextNode

		nodeStr = nodeStr + "X"
		return nodeStr

	def returnValue(self, pos):
		if (pos > self.__nNodes) | (pos < 1):
			print("Supplied position not defined in linked list.")
			return
		else:
			# loop through nodes until position supplied matches position in linked list
			# return node value
			currentNode, _ = self.__reachLinkedListPos(pos)

			return currentNode.value

	def appendNode(self, value):
		# append a new node to the end of the linked list

		# create a new node
		newNode = node(value)

		if self.__nNodes == 0:
			self.__startNode = node(value)
		else:
			# loop through list until reach end of linked list
			endNode, _ = self.__reachLinkedListPos(self.__nNodes)

			# link last node to new node and increment number of nodes by 1
			endNode.nextNode = newNode
		self.__nNodes += 1

		return

	def insertNode(self, value, pos):
		# create new node
		newNode = node(value)

		# if position = 1, add to beginning
		# if 1 < position < nNodes, add to position
		# if position >= nNodes, add to end
		# if position is negative or zero, break the program
		if pos == 1:
			newNode.nextNode = self.__startNode
			self.__startNode = newNode

			# increment number of nodes by 1
			self.__nNodes += 1

		elif 1 < pos < self.__nNodes:
			# get the current node in the position argument
			currentNode, previousNode = self.__reachLinkedListPos(pos)

			# insert new node that that position
			previousNode.nextNode = newNode
			newNode.nextNode = currentNode

			# increment number of nodes by 1
			self.__nNodes += 1

		elif pos < 1:
			print("Position cannot be less than 1")
			return

		else:
			if pos > self.__nNodes:
				print("Position to insert new node exceeds number of nodes in the linked list. Appending to end instead.")

			self.appendNode(value)

		return

	def popLinkedList(self):
		# reach end of linked list
		currentNode = self.__startNode

		while currentNode.nextNode != None:
			previousNode = currentNode
			currentNode = previousNode.nextNode

		# remove connection between previous node and current node
		# output current node's value
		previousNode.nextNode = None
		return currentNode.value

	def deleteNode(self, pos):
		# if position not defined in linked list, return error
		# if position is first, delete start node
		# if position is not first, delete node at position and set connections accordingly

		if (pos > self.__nNodes) | (pos < 1):
			print("Node position has to be defined ")
			return

		elif pos == 1:
			currentNode, _ = self.__reachLinkedListPos(2)
			self.__startNode = currentNode

		else:
			currentNode, previousNode =  self.__reachLinkedListPos(pos)

			# if current node is end of linked list, set previous node's next node to be none
			# else set previous node's next node to be current node's next node
			if currentNode == None:
				previousNode.nextNode = None

			else:
				_, nextNode =  self.__reachLinkedListPos(pos + 1)
				previousNode.nextNode = currentNode.nextNode

		# decrement number of nodes by 1
		self.__nNodes -= 1
		return

	def deleteValue(self, value):
		currentPos = 1
		currentNode = self.__startNode

		# if node #1's value is equal to the value to be deleted, set node #2 to be the start the of the linked list
		# if node n's value is equal to the value to be deleted, remove that node and link the previous node to the next node
		# if end node's value is equal to the value to be deleted, set the second to last node to be the end of the linked list
		while currentNode != None:
			if currentNode.value == value:
				self.deleteNode(currentPos)
				
				if currentPos == 1:
					currentNode = self.__startNode
			else:
				currentNode = currentNode.nextNode
				currentPos += 1

		return

	def __reachLinkedListPos(self, pos):
		# start at beginning of linked list
		currentPos = 1
		currentNode = self.__startNode
		previousNode = None

		# loop through nodes until current node is equal to position to insert into
		while currentPos != pos:
			previousNode = currentNode
			currentNode = previousNode.nextNode
			currentPos += 1

		return currentNode, previousNode