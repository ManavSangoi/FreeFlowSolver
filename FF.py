from pyautogui import sleep


class FreeFlow:
    def __init__(self):
        self.board = []

    def makeboard(self):
        self.row=6
        self.col=6
        for i in range(self.row):
            l=[]
            for j in range(self.col):
                l.append('-')
            self.board.append(l)

    def showboard(self):
        for i in self.board:
            for j in i:
                print(j,end=' ')
            print()
        print()

    def updateboard(self):
        for c in self.color_list:
            pos=self.color_index[c][0]
            self.board[pos[0]][pos[1]]=c
            pos=self.color_index[c][1]
            self.board[pos[0]][pos[1]]=c

    def getcolors(self):
        no_of_colors=5
        self.color_list=['r','g','b','p','o']
        self.color_index={
            'r':[(2,2),(4,4)],
            'g':[(3,3),(4,1)],
            'b': [(5,3), (4,5)],
            'p': [(2,1), (3,5)],
            'o': [(0,5), (4,3)],
        }
        self.updateboard()

    def isvalid(self,move):
        if move[0]>=0 and move[0]<self.row and move[1]>=0 and move[1]<self.col:
            if self.board[move[0]][move[1]]!='-':
                return False
            return True
        return False
    
    def dist(self,move,color):
        end=self.color_index[color][1]
        return abs(move[0]-end[0]) + abs(move[1]-end[1])
    
    def sort_moves(self, move,color):
        for i in range(len(move)):
            for j in range(len(move)-1):
                if self.dist(move[j],color)>self.dist(move[j+1],color):
                    move[j], move[j+1] = move[j+1], move[j]
        
        return move
    
    
    def find_next_moves(self,color,curr):
        moves=[(0,1),(1,0),(0,-1),(-1,0)]
        next=[]
        for i in moves:
            nextmove=(curr[0]+i[0],curr[1]+i[1])
            if nextmove==self.color_index[color][1]:
                next.insert(0,nextmove)
                continue
            if self.isvalid(nextmove):
                next.append(nextmove)
        return self.sort_moves(next,color)
                
                
    def solve(self,number,curr=-1):
        # sleep(1)
        if number==5:
            self.showboard()
            exit(0)
        color=self.color_list[number]
        if curr==-1:
            curr=self.color_index[color][0]
        moves=self.find_next_moves(color,curr)
        # self.showboard()
        for move in moves:
            # print(move,moves)
            if move == self.color_index[color][1]:
                self.solve(number+1)
            else:
                self.board[move[0]][move[1]]=color
                self.solve(number,move)
                self.board[move[0]][move[1]]='-'
        return

    def start(self):
        self.makeboard()
        self.getcolors()
        self.showboard()
        # move=(4,0)
        # print(move == self.colors[self.color[0]][1])
        self.solve(0)


if __name__ == '__main__':
    ff = FreeFlow()
    ff.start()