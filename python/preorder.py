import queue


class Solution:
    def preorderTraversal(self, root):
        pass


if __name__ == '__main__':

    l = [3, 4, 2, 1]
    l.sort()
    print(l)
    q1 = queue.Queue()
    q1.put(1)
    q1.put(2)
    print(q1.get())
    print(q1.get())
