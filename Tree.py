import pygame,string
pygame.init()
infoObject = pygame.display.Info()
display_window_width=1300
display_window_height=700
input_window_width=300
input_window_height=100
#colors--------------------
light_green = (191,248,22)
ligth_grey = (230,230,230)
yellow=(255,245,62)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green = (0,155,0)
grey=(57,89,73)
bkgrnd_color = (0,255,255)
#---------------------------
tree_size = .8
scale_tree_x = int(400*tree_size)
scale_tree_y = int(100*tree_size)
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event.key
    else:
      pass    
def msgtoscrn(display_window,msg,color,y_displace=0,size=25,x_displace=0,font_type = "comicsansms"): #fn() to display any msg on display window
    font = pygame.font.SysFont(font_type,size)
    screen_text = font.render(msg,True,color)
    textrect = screen_text.get_rect()
    textrect.center = (display_window[1]/2) + x_displace,(display_window[2]/2) + y_displace
    display_window[0].blit(screen_text,textrect)
def input_screen(quote):
    global input_window
    input_window = [pygame.display.set_mode((input_window_width,input_window_height)),input_window_width,input_window_height]
    input_window[0].fill(ligth_grey)
    pygame.draw.rect(input_window[0],grey,[input_window_width/15-2,input_window_height/2-2,13*input_window_width/15,input_window_height/4])
    pygame.draw.rect(input_window[0],white,[input_window_width/15,input_window_height/2,13*input_window_width/15,input_window_height/4])
    current_string = []
    msgtoscrn(input_window,quote,grey,-20,20,0,"aachen")
    pygame.display.update()
    condition = True
    pos = 0
    while condition:
        pygame.draw.rect(input_window[0],white,[input_window_width/15,input_window_height/2,13*input_window_width/15,input_window_height/4])
        inkey = get_key()
        if inkey == pygame.K_BACKSPACE and len(current_string)>0 and pos > 0:
            current_string = current_string[:pos-1] + current_string[pos:]
            pos-=1
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_LEFT and pos > 0:
            pos-=1
        elif inkey == pygame.K_RIGHT and pos < len(current_string):
            pos+=1
        elif inkey <= 127 and inkey != pygame.K_BACKSPACE:
            current_string = current_string[:pos] + [chr(inkey)] + current_string[pos:]
            pos+=1
        pygame.draw.rect(input_window[0],white,[input_window_width/15,input_window_height/2,13*input_window_width/15,input_window_height/5])
        msgtoscrn(input_window,string.join(current_string[-27:],""),black,input_window_height/10,15,0)
        if pos <= 27:
            cpos = pos
        else:
            cpos = 27
        pygame.draw.line(input_window[0],black,
                         (input_window_width/2 + int((cpos - len(current_string[-27:])/2.0)*9.35) ,input_window_height/2 + 2),
                         (input_window_width/2 + int((cpos - len(current_string[-27:])/2.0)*9.35) ,input_window_height/2 + input_window_height/4 - 2),1)
        pygame.display.update()
    pygame.display.quit()
    return string.join(current_string,"").replace(',',' ')
class Node(object): #class for each node
    def __init__(self, data=None, next_r_node=None, next_l_node=None):
        self.data = data
        self.next_r_node = next_r_node
        self.next_l_node = next_l_node
    def get_data(self):
        return self.data
    def get_r_next(self):
        return self.next_r_node
    def get_l_next(self):
        return self.next_l_node
    def set_r_next(self, new_r_next):
        self.next_r_node = new_r_next
    def set_l_next(self, new_l_next):
        self.next_l_node = new_l_next      
class Binary_Search_Tree(object): #class for Binary_Search_Tree
    def __init__(self, root=None):
        self.root = root
    def find(self, data): #it finds given data in tree
        if self.root == None: #tree is empty
            return None,None
        if self.root.get_data() == data: #data founds at root
            return None,self.root
        if data < self.root.get_data(): #check data belongs to right or left subtree of root
            ptr = self.root.get_l_next()
        else:
            ptr = self.root.get_r_next()
        save = self.root
        while ptr != None:
            if data == ptr.get_data():
                return save,ptr
            save = ptr
            if data < ptr.get_data():
                ptr = ptr.get_l_next()
            elif data > ptr.get_data():
                ptr = ptr.get_r_next()
            else:
                ptr = None
        return save,None
    def insert(self,data,): #insert data at its justified postion in bst
        display_window[0].fill(bkgrnd_color)
        msgtoscrn(display_window,", ".join(map(str,values)),grey,display_window[2]/2-scale_tree_y/5,scale_tree_x/20,0)
        par,loc = self.find(data) #call find() to know the justified postion of data
        if par == None and loc == None: #tree is empty
            new_node = Node(data)
            self.root = new_node
            print str(data).rjust(5),":\tInserted at root"
            msgtoscrn(display_window,str(data) + " Inserted at root",grey,display_window[2]/2-3*scale_tree_y/5,scale_tree_x/20,0)
        else:
            if loc != None: #it means data already present in tree
                print str(data).rjust(6),":\tItem already present:"
                msgtoscrn(display_window,str(data) + " already presents",grey,display_window[2]/2-3*scale_tree_y/5,scale_tree_x/20,0)
            elif  data < par.get_data(): #it means data has to be inserted as left child of its parent
                new_node = Node(data)
                par.set_l_next(new_node)
                print str(data).rjust(6), ":\tInserted as LEFT child of",par.get_data()
                msgtoscrn(display_window,str(data) + " Inserted as LEFT child of " + str(par.get_data()),grey,display_window[2]/2-3*scale_tree_y/5,scale_tree_x/20,0)
            else: #it means data has to be inserted as right child of its parent
                new_node = Node(data)
                par.set_r_next(new_node)
                print str(data).rjust(6), ":\tInserted as RIGHT child of",par.get_data()
                msgtoscrn(display_window,str(data) + " Inserted as RIGHT child of " + str(par.get_data()),grey,display_window[2]/2-3*scale_tree_y/5,scale_tree_x/20,0)       
    def prnt(self): #it outputs the tree in preorder form 
        print "\nTree in Pre-Order form:\n"
        stack = [None]
        ptr = self.root
        while ptr != None:
            while ptr!=None:
                print ptr.get_data(),
                if ptr.get_r_next()!=None:
                    stack.append(ptr.get_r_next())
                ptr = ptr.get_l_next()
            ptr = stack[-1]
            del stack[-1]        
    def display(self): #it display tree on display window
        stack = [(None,0,0)] #stack to store info of right child if tree
        ptr = self.root
        sx = 0
        sy = -display_window[2]/2 + 30
        i = 1
        p = 1
        msgtoscrn(display_window,str(ptr.get_data()),black,sy,scale_tree_x/20,sx)
        if ptr.get_r_next()!=None:
            stack.append((ptr.get_r_next(),sx,sy,i))
        ptr = ptr.get_l_next()
        if ptr == None:
            ptr = stack[-1][0]
            if ptr != None:
                i = stack[-1][3]
                sx = stack[-1][1]
                p = -1
                sy = stack[-1][2]
            del stack[-1]
        condition = True
        while condition:
            for event in pygame.event.get(): #loop to handle quit event and exit the program when user click on quit
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.display.toggle_fullscreen()
                        condition = False
                        break
            while ptr != None:
                while ptr!=None:
                    x = sx
                    y = sy
                    sx -= p*scale_tree_x/i
                    p = 1
                    sy += scale_tree_y
                    if i < 4:
                        node_size = scale_tree_x/20
                    elif i == 4:
                        node_size = scale_tree_x/25
                    else:
                        node_size = scale_tree_x/30
                    msgtoscrn(display_window,str(ptr.get_data()),black,sy,node_size,sx)
                    pygame.draw.line(display_window[0],grey,(display_window[1]/2+x,display_window[2]/2+y+scale_tree_y/5),(display_window[1]/2+sx,display_window[2]/2+sy-scale_tree_y/5),1)
                    i*=2
                    if ptr.get_r_next()!=None:
                        stack.append((ptr.get_r_next(),sx,sy,i))
                    ptr = ptr.get_l_next()
                    pygame.display.update()
                ptr = stack[-1][0]
                if ptr != None:
                    i = stack[-1][3]
                    sx = stack[-1][1]
                    p = -1
                    sy = stack[-1][2]
                del stack[-1]
            pygame.display.update()
def main(): #main fn() of program which combine it all together  
    global values,display_window
    values = map(int,raw_input("Enter Nodes of Binary Search Tree:").replace(',',' ').split())
    tree = Binary_Search_Tree()
    display_window = [pygame.display.set_mode((display_window_width,display_window_height)),display_window_width,display_window_height] #declare display_window

    for value in values:
        tree.insert(value)
        tree.display()
    tree.prnt()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()                
main() #so here we call main and the story begins













        
    
