import math
class Tree(object):
    def __init__(self):
        self.branches = []
        self.branch_ends = []
        self.iter = 10
        self.angle = 45

    def origin(self,ax):
        x = [0,0]
        y = [0,1]
        branch = (x,y)
        self.branches.append(branch)
        self.ax = ax
        self.l, = ax.plot(x,y)
        self.branch_ends.append(branch)

    def iterate_tree(self,ax):
        ang = math.degrees(self.angle)
        new_ends = []
        for x,y in self.branch_ends:
            proj_vec = [(x[1]-x[0]),(y[1]-y[0])]
            x1_rot = x[1] + proj_vec[0]*math.cos(ang)-proj_vec[1]*math.sin(ang)
            y1_rot = y[1] + proj_vec[0]*math.sin(ang)+proj_vec[1]*math.cos(ang)
            x1 = [x[1],x1_rot]
            y1 = [y[1],y1_rot]

            x2_rot = x[1] + proj_vec[0]*math.cos(-ang)-proj_vec[1]*math.sin(-ang)
            y2_rot = y[1] + proj_vec[0]*math.sin(-ang)+proj_vec[1]*math.cos(-ang)
            x2 = [x[1],x2_rot]
            y2 = [y[1],y2_rot]
            ax.plot(x2)
            ax.plot(y2)
            new_ends.append((x1,y1))
            new_ends.append((x2,y2))


        self.branch_ends = new_ends
