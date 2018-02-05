# History:
# 2018-02-04 - JL - created class tests for Node and singleLinkedList classes
#                 - created test cases for singleLinkedLIst methods: nNodes, printLinkedList, returnValue,
#                                                                    appendNode, insertNode, popLinkedList,
#                                                                    deleteNode

import unittest
import linkedlist as ll

class TestNode(unittest.TestCase):

    def setUp(self):
        self.testNode = ll.node(1)

    def test_initNode(self):
        self.assertEqual(self.testNode.value, 1)
        self.assertEqual(self.testNode.nextNode, None)

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.testSingleLinkedList = ll.singleLinkedList(1)

    def test_printLinkedList(self):
        result = self.testSingleLinkedList.printLinkedList()
        self.assertEqual(result, "[ 1 | 1 ]-->X")

    def test_appendNode(self):
        self.testSingleLinkedList.appendNode(2)
        result = self.testSingleLinkedList.printLinkedList()
        self.assertEqual(result, "[ 1 | 1 ]-->[ 2 | 2 ]-->X")

        self.testSingleLinkedList.appendNode(3)
        result = self.testSingleLinkedList.printLinkedList()
        self.assertEqual(result, "[ 1 | 1 ]-->[ 2 | 2 ]-->[ 3 | 3 ]-->X")

    def test_nNodes(self):
        self.assertEqual(self.testSingleLinkedList.nNodes, 1)

        self.testSingleLinkedList.appendNode(2)
        self.assertEqual(self.testSingleLinkedList.nNodes, 2)

    def test_returnValue(self):
        for k in range(2, 10 + 1):
            self.testSingleLinkedList.appendNode(k)

        self.assertEqual(self.testSingleLinkedList.returnValue(7), 7)
        self.assertEqual(self.testSingleLinkedList.returnValue(11), None)
        self.assertEqual(self.testSingleLinkedList.returnValue(0), None)

    def test_insertNode(self):
        # linked list after inserting value 2 at position 1:
        # [2] -> [1]
        self.testSingleLinkedList.insertNode(2, 1)
        self.assertEqual(self.testSingleLinkedList.returnValue(1), 2)
        self.assertEqual(self.testSingleLinkedList.returnValue(2), 1)

        # linked list after inserting value 4 at position 20:
        # [2] -> [1] -> [4]
        # since 20 is larger than amount of current nodes, will append to end
        self.testSingleLinkedList.insertNode(4, 20)
        self.assertEqual(self.testSingleLinkedList.returnValue(3), 4)

        # linked list after inserting value 6 at position 2:
        # [2] -> [6] -> [1] -> [4]
        self.testSingleLinkedList.insertNode(6, 2)
        self.assertEqual(self.testSingleLinkedList.returnValue(2), 6)
        self.assertEqual(self.testSingleLinkedList.returnValue(3), 1)
        self.assertEqual(self.testSingleLinkedList.returnValue(4), 4)
        self.assertEqual(self.testSingleLinkedList.nNodes, 4)

        # inserting a zero should result in error
        self.testSingleLinkedList.insertNode(10, 0)
        self.assertEqual(self.testSingleLinkedList.nNodes, 4)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 2 ]-->[ 2 | 6 ]-->[ 3 | 1 ]-->[ 4 | 4 ]-->X")

        # inserting a negative should result in error
        self.testSingleLinkedList.insertNode(10, -1)
        self.assertEqual(self.testSingleLinkedList.nNodes, 4)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 2 ]-->[ 2 | 6 ]-->[ 3 | 1 ]-->[ 4 | 4 ]-->X")

    def test_popLinkedList(self):
        self.testSingleLinkedList.appendNode(2)
        self.testSingleLinkedList.appendNode(3)

        self.assertEqual(self.testSingleLinkedList.popLinkedList(), 3)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 2 ]-->X")

    def test_deleteNode(self):
        for k in range(2, 5 + 1):
            self.testSingleLinkedList.appendNode(k)

        # linked list looks like:
        # [1] -> [2] -> [3] -> [4] -> [5] -> X

        # cannot delete not existent node
        self.testSingleLinkedList.deleteNode(20)
        self.assertEqual(self.testSingleLinkedList.nNodes, 5)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 2 ]-->[ 3 | 3 ]-->[ 4 | 4 ]-->[ 5 | 5 ]-->X")

        self.testSingleLinkedList.deleteNode(0)
        self.assertEqual(self.testSingleLinkedList.nNodes, 5)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 2 ]-->[ 3 | 3 ]-->[ 4 | 4 ]-->[ 5 | 5 ]-->X")

        self.testSingleLinkedList.deleteNode(-1)
        self.assertEqual(self.testSingleLinkedList.nNodes, 5)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 2 ]-->[ 3 | 3 ]-->[ 4 | 4 ]-->[ 5 | 5 ]-->X")

        # linked list looks like:
        # [1] -> [2] -> [4] -> [5] -> X
        self.testSingleLinkedList.deleteNode(3)
        self.assertEqual(self.testSingleLinkedList.nNodes, 4)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 2 ]-->[ 3 | 4 ]-->[ 4 | 5 ]-->X")

        # linked list looks like:
        # [2] -> [4] -> [5] -> X
        self.testSingleLinkedList.deleteNode(1)
        self.assertEqual(self.testSingleLinkedList.nNodes, 3)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 2 ]-->[ 2 | 4 ]-->[ 3 | 5 ]-->X")

        # linked list looks like:
        # [2] -> [4] -> X
        self.testSingleLinkedList.deleteNode(self.testSingleLinkedList.nNodes)
        self.assertEqual(self.testSingleLinkedList.nNodes, 2)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 2 ]-->[ 2 | 4 ]-->X")

    def test_deleteValue(self):
        for k in range(2, 5 + 1):
            if k % 2 == 0:
                self.testSingleLinkedList.appendNode(2)
            else:
                self.testSingleLinkedList.appendNode(1)

        # linked list looks like:
        # [1] -> [2] -> [1] -> [2] -> [1] -> [2] -> X
        self.testSingleLinkedList.deleteValue(3)
        self.assertEqual(self.testSingleLinkedList.nNodes, 6)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 2 ]-->[ 3 | 1 ]-->[ 4 | 2 ]-->[ 5 | 1 ]-->[ 6 | 2 ]-->X")

        # linked list looks like:
        # [1] -> [1] -> [1] -> X
        self.testSingleLinkedList.deleteValue(3)
        self.assertEqual(self.testSingleLinkedList.nNodes, 3)
        self.assertEqual(self.testSingleLinkedList.printLinkedList(), "[ 1 | 1 ]-->[ 2 | 1 ]-->[ 3 | 1 ]-->X")

if __name__ == '__main__':
    unittest.main(verbosity = 2)