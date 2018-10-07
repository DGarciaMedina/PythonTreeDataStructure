'''
Author: Diego Garcia Medina
Date: October 2018
Email: diego.garcia.medina@outlook.com
GitHub website: https://github.com/DGarciaMedina

This is a Python class for easy creation of trees by creating the first node 
and add children nodes and add values to each node for any application.

One can also display the tree. An example is shown below:

l1 (3)                                                                  
│                                                                       
├───────────────────────┬───────────────────────┬───────────┐
l11 (7)                 l12 (8)                 l13 (13)    l14 (14)    
│                       │                                               
│                       ├───────────┐                        
l111 (15)               l121 (36)   l122 (42)                           
│                                                                       
├───────────┐                                                
l1111 (102) l1112 (103)                                                 
            │                                                           
            │                                                           
            l11121 (107)    
            
'''

class node:
    def __init__(self,name):
        self.output_nodes = []
        self.value = -1
        self.is_last_node = True
#        self.is_first_node = True
        self.y_pos = 0
        self.name = name
        self.x_pos = 0
        self.extra_breadth_below_node = 0
        self.parent = None
        self.branch_separation = 8
        
    
    def set_children(self,*children):
        self.is_last_node = False
        for i,child in enumerate(children):
            child.y_pos = self.y_pos + 1
            child.x_pos += i + self.x_pos
            self.output_nodes.append(child)
            child.parent = self
        # propagate upwards
        parent_node = child.parent
        parent_node.extra_breadth_below_node += i        
        while parent_node.parent != None:
            parent_node = parent_node.parent
            parent_node.extra_breadth_below_node += i
            
    def set_value(self,value):
        self.value = value
        
    def find_size_of_tree(self,height=0,width=0):
        for child in self.output_nodes:
            if height < child.y_pos:
                height = child.y_pos
            if width < child.x_pos:
                width = child.x_pos
            if not child.is_last_node:
                height,width = child.find_size_of_tree(height,width)
                
        return height, width
    
    def cleanup(self):
        for i,child in enumerate(self.output_nodes):

            if i > 0:
                child.extra_breadth_below_node += self.output_nodes[i-1].extra_breadth_below_node
                child.x_pos += self.output_nodes[i-1].extra_breadth_below_node
            else:
                child.extra_breadth_below_node += (self.x_pos - child.x_pos)
                child.x_pos = self.x_pos

            child.cleanup()
    
    def add_values_to_table(self,display_table):
        x = self.x_pos
        y = self.y_pos
#        display_table[y][x] = "{} ({})".format(self.name,self.value)
        display_table[y][x] = "{}".format(self.name)
        for child in self.output_nodes:
            display_table = child.add_values_to_table(display_table)
            
        return display_table
    
    
    def show_tree(self, display_value = False):
        
        if display_value:
            self.branch_separation += 4
            print("Displaying values at the nodes in brackets:\n")
        
        self.cleanup()
        
        height,width = self.find_size_of_tree()
        empty_display_table = [[""]*(width+1) for i in range(height+1)]
        filled_display_table = self.add_values_to_table(empty_display_table)
        
        can_continue = False
        
        for line_num, level in enumerate(filled_display_table):
            
            previous_line_string = ""
            line_string = ""
            next_line_string = ""
            
            for i,node_string in enumerate(level):
                
                len_name = len(node_string)
                
                if node_string != "":
                    node = eval(node_string)
                    
                    if display_value:
                        str_value = " (" +str(node.value) + ")"
                        len_value = len(str_value)
                    else:
                        str_value = ""
                        len_value = 0
                    
                    line_string += node.name + str_value + " "*(self.branch_separation - len_name - len_value)
                    
                    # sort the 'next_line' ones
                    if not node.is_last_node:
                        next_line_string += "│" + " "*(self.branch_separation - 1)
                    else:
                        next_line_string += " "*self.branch_separation
                        
#                    number_of_siblings = len(node.parent.output_nodes)
#                    
#                    number_of_siblings_left = number_of_siblings
                    
                    if node.is_last_node and len(node.parent.output_nodes)==1:
                        previous_line_string += "│" + " "*(self.branch_separation-1)
                        
                    
                    if node.parent != None:
                        
                        if len(node.parent.output_nodes) == 1 and not node.is_last_node:
                            previous_line_string += "│" + " "*(self.branch_separation-1)
                            
                        if len(node.parent.output_nodes) > 1:
                            if node.parent.output_nodes.index(node) == 0:
                                can_continue = True
                                previous_line_string += "├" + "─"*(self.branch_separation-1)
                            elif node.parent.output_nodes.index(node) == len(node.parent.output_nodes) -1:
                                can_continue = False
                                previous_line_string += "┐"
                            else:
                                previous_line_string += "┬" + "─"*(self.branch_separation-1)
                    
                    
                else:
                    line_string += " "*self.branch_separation
                    next_line_string += " "*self.branch_separation
                    
                    if can_continue == True:
                        previous_line_string += "─"*self.branch_separation
                    else:
                        previous_line_string += " "*self.branch_separation
                    

                
            if line_num > 0:        
                print(previous_line_string)    
            print(line_string)
            print(next_line_string)
        
            
l1 = node("l1")
l11 = node("l11")
l12 = node("l12")
l13 = node("l13")
l14 = node("l14")
l111 = node("l111")
l121 = node("l121")
l122 = node("l122")
l1111 = node("l1111")
l1112 = node("l1112")
l11121 = node("l11121")

l1.set_value(3)
l11.set_value(7)
l12.set_value(8)
l13.set_value(13)
l14.set_value(14)
l111.set_value(15)
l121.set_value(36)
l122.set_value(42)
l1111.set_value(102)
l1112.set_value(103)
l11121.set_value(107)

l1.set_children(l11,l12,l13,l14)
l11.set_children(l111)
l111.set_children(l1111,l1112)
l12.set_children(l121,l122)
l1112.set_children(l11121)

l1.show_tree(True)
