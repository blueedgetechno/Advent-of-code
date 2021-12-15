class PriorityQueueNode:
    def __init__(self, value, pr):
        self.val = value
        self.pr = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front == None else False

    def push(self, value, pr):
        if self.isEmpty() == True:
            self.front = PriorityQueueNode(value, pr)
        else:
            newNode = PriorityQueueNode(value, pr)
            if self.front.pr > pr:
                newNode.next = self.front
                self.front = newNode
            else:
                temp = self.front
                while temp.next:
                    if pr <= temp.next.pr:
                        break
                    temp = temp.next

                newNode.next = temp.next
                temp.next = newNode

    def update(self, value, pr):
        temp = self.front
        if temp and temp.val == value:
            self.front = temp.next
        elif temp:
            while temp.next and temp.next.val != value:
                temp = temp.next

            nxtNode = temp.next
            if nxtNode:
                temp.next = nxtNode.next

        self.push(value, pr)

    def pop(self):
        val = self.front.val
        self.front = self.front.next
        return val

    def traverse(self):
        temp = self.front
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

        print()
