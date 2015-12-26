#! Python3
import turtle
import tkinter
import tkinter as tk
from tkinter import ttk

#############################  My Turtle is named bob ##################################
x = turtle.Screen()
x.title('Dads walking turtle')
bob = turtle.Turtle()
def _to_number(x):
    if isinstance(x, str):
        if '.' in x:
            x = float(x)
        else:
            x = int(x)
    return x
class RootWindow(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()
        

        self.colorlist=['black','red','yellow','blue','green','brown','orange','yellow','purple','pink','white','gray']
        self.turtle_shape_list=['arrow', 'circle', 'turtle', 'classic', 'square']
        self.n = ttk.Notebook(self)
        n = self.n
        self.tab1 = ttk.Frame(n)
        tab1 = self.tab1
        tab2 = ttk.Frame(n)
        n.add(tab1, text = "Main")
        n.add(tab2, text = "Extras")
        n.pack(fill="both", expand=True)

  
#################################### TAB 1 #############################################     
########################################################################################

        self.fwd_label = ttk.Label(tab1, text='Move forward or back:')
        self.trn_label = ttk.Label(tab1, text='Turn right or left:')
        self.circ_label = ttk.Label(tab1, text='Draw a circle. Give a radius below:')
        self.color_label = ttk.Label(tab1, text='Change the pen color:')
        self.spd_label = ttk.Label(tab1, text='Adjust drawing speed:')
        self.reset_label = ttk.Label(tab1, text='Reset drawing board:')
        self.penup_label = ttk.Label(tab1, text='Raise or lower the pen:')
        self.width_label =ttk.Label(tab1, text='Change the pen size:')
        self.undo_label = ttk.Label(tab1, text='Undo/Reset:')
        self.fwd_entry = ttk.Entry(tab1)
        self.trn_entry = ttk.Entry(tab1)
        self.circ_entry = ttk.Entry(tab1)
        self.color_entry = ttk.Combobox(tab1,state='readonly',values=self.colorlist)

        self.fwd_button = ttk.Button(tab1, text='forward',command=lambda:self.walk_turtle(1))
        self.bck_button = ttk.Button(tab1, text='back',command=lambda:self.walk_turtle(0))
        self.rt_button = ttk.Button(tab1, text='turn right',command=lambda:self.turn_turtle(1))
        self.lt_button = ttk.Button(tab1, text='turn left',command=lambda:self.turn_turtle(0))
        self.circ_button = ttk.Button(tab1, text='draw a circle', width=18,command=self.circle_turtle)
        self.penup_button = ttk.Button(tab1, text='raise pen',command=bob.penup)
        self.pendwn_button = ttk.Button(tab1, text='lower pen',command=bob.pendown)
        self.color_button = ttk.Button(tab1, text='change color')
        self.spd_button = ttk.Button(tab1, text='change speed')
        self.reset_button = ttk.Button(tab1, text='reset')
        self.undo_button1 = ttk.Button(tab1, text='undo', command=bob.undo)
        self.reset_button1 = ttk.Button(tab1, text='reset', command=self.reset_all)
        
        #self.sldr_var = tk.IntVar() ##### Couldn't get this to work! It is supposed to be used by self.sldr_width to store the selected
                                     ##### number from the slider bar.. P.O.S
        self.testing='brian'
        self.spd_sldr = ttk.Scale(tab1, orient='horizontal')
        self.width_sldr = tk.Scale(tab1, orient='horizontal', command=self.change_pen_size, from_=1,to=30)
        self.width_sldr.bind('<<ScaleChanged>>', self.change_pen_size)

        self.fwd_label.grid(column=1,row=1,pady=1,padx=2,sticky='s')
        self.fwd_entry.grid(column=1,row=2,pady=3,padx=2)
        self.fwd_button.grid(column=2,row=2,pady=3,padx=1)
        self.bck_button.grid(column=3,row=2,pady=3,padx=1)
        self.trn_label.grid(column=1,row=3,pady=1,padx=2,sticky='s')
        self.trn_entry.grid(column=1,row=4,pady=3,padx=2)
        self.lt_button.grid(column=2,row=4,pady=3,padx=2)
        self.rt_button.grid(column=3,row=4,pady=3,padx=2)
        self.circ_label.grid(column=1,row=5,pady=1,padx=2)
        self.circ_entry.grid(column=1,row=6,pady=3,padx=2)
        self.circ_button.grid(column=2,row=6,columnspan=2,pady=3,padx=2)
        self.color_label.grid(column=1,row=7,pady=1,padx=0)
        self.color_entry.grid(column=2,row=7,columnspan=3,pady=3,padx=1,sticky='w')
        self.width_label.grid(column=1,row=8,pady=1,padx=2)
        self.width_sldr.grid(column=2,columnspan=2,row=8,pady=3,padx=2,sticky='w')

        self.penup_label.grid(column=1,row=9,pady=1,padx=1)
        self.penup_button.grid(column=2,row=9,pady=3,padx=2)
        self.pendwn_button.grid(column=3,row=9,pady=3,padx=2)
        self.undo_label.grid(column=1, row=10,pady=3, padx=2)
        self.undo_button1.grid(column=2,row=10,pady=2,padx=2)
        self.reset_button1.grid(column=3,row=10,pady=2,padx=2)
        #self.spd_label.grid(column=1,row=9,pady=1,padx=2)
        #self.spd_sldr.grid(column=2,row=9,pady=3,padx=2)

        self.color_entry.bind('<<ComboboxSelected>>', self.turtle_color)
        self.color_entry.configure(state='normal')
        self.color_entry.insert(0,'black')
        self.color_entry.configure(state='readonly')


################################# TAB 2 ############################################
####################################################################################
        self.shape_label = ttk.Label(tab2,text='Select a shape below:')
        self.turtle_shape_label = ttk.Label(tab2,text='Change how bob looks:')
        self.bgcolor_label = ttk.Label(tab2,text='Change the background color:')
        self.dot_label = ttk.Label(tab2,text='Draw a dot with Bob:')
        self.pencolor_label = ttk.Label(tab2,text='Change the pen/fill colors for drawing shapes.\nThis only applies for drawing shapes:')
        
        self.shape_entry = ttk.Combobox(tab2)
        self.shape_button = ttk.Button(tab2,text='draw shape')
        self.pencolor_entry = ttk.Combobox(tab2, values=self.colorlist)
        self.fillcolor_entry = ttk.Combobox(tab2, values=self.colorlist)
        self.dot_entry = ttk.Combobox(tab2)
        self.dot_button = ttk.Button(tab2,text='draw dot',command=self.draw_dot)
        self.turtle_shape_entry = ttk.Combobox(tab2,values=self.turtle_shape_list)
        self.turtle_shape_button = ttk.Button(tab2,text='change Bob',command=self.change_bob_appearance)
        self.stamp_button = ttk.Button(tab2,text='bob stamp', command=bob.stamp)
        self.bgcolor_entry = ttk.Combobox(tab2, values=self.colorlist)


        

        self.pencolor_label.grid(column=1,row=1,columnspan=2,pady=1,padx=2,sticky='s')
        self.pencolor_entry.grid(column=1,row=2,pady=2,padx=2)
        self.fillcolor_entry.grid(column=2,row=2,pady=2,padx=2)
        self.shape_label.grid(column=1,row=3,pady=1,padx=2,sticky='s')
        self.shape_entry.grid(column=1,row=4,pady=2,padx=2)
        self.shape_button.grid(column=2,row=4,pady=2,padx=2,sticky='w')
        self.dot_label.grid(column=1,row=5,pady=2,padx=2,sticky='s')
        self.dot_entry.grid(column=1,row=6,pady=2,padx=2)
        self.dot_button.grid(column=2,row=6,pady=2,padx=2,sticky='w')
        self.turtle_shape_label.grid(column=1,row=7,pady=2,padx=2,sticky='s')
        
        self.turtle_shape_entry.grid(column=1,row=8,pady=2,padx=2)
        self.turtle_shape_button.grid(column=2,row=8,pady=1,padx=2,sticky='w')
        self.stamp_button.grid(column=2,row=8,pady=2,padx=1,sticky='e')
        self.bgcolor_label.grid(column=1,row=9,pady=4,padx=2)
        self.bgcolor_entry.grid(column=2,row=9,pady=4,padx=2)
        self.sunbtn = ttk.Button(tab2,text='draw sun',command=self.sun)
        self.sunbtn.grid(column=2,row=10)
        self.bgcolor_entry.insert(0,'white')
        self.fillcolor_entry.insert(0,'black')
        self.pencolor_entry.insert(0,'black')
        self.pencolor_entry.configure(state='readonly')
        self.fillcolor_entry.configure(state='readonly')
        self.bgcolor_entry.configure(state='readonly')

        self.bgcolor_entry.bind('<<ComboboxSelected>>', self.change_bgcolor)
        self.turtle_shape_entry.bind('<<ComboboxSelected>>', self.change_bob_appearance)
   


##################################### METHODS #####################################
###################################################################################
    def change_pen_size(self, event):
        sel = self.width_sldr.get()
        print('sel ' + str(sel))
        bob.width(int(sel))
    def sun(self):
        bob.speed(10)
        old_color = bob.color()
        print(old_color)
        bob.color('red','yellow')
        bob.begin_fill()
        for i in range(36):
            
            
            bob.forward(200)
            bob.left(170)
           
            
            
        bob.end_fill()
     
        bob.color(old_color[0])

    def walk_turtle(self,var):
        
        steps = self.fwd_entry.get()
        try:
            steps=int(steps)
            if var == 0:
                bob.back(steps)
            elif var == 1:
                bob.forward(steps)
        except Exception as e:
            print(e)

    def turn_turtle(self,var):
        degrees = self.trn_entry.get()
        try:
            degrees=int(degrees)
            if var == 0:
                bob.left(degrees)
            elif var == 1:
                bob.right(degrees)
        except Exception as e:
            print(e)

    def circle_turtle(self):
        radius = self.circ_entry.get()
        try:
            radius=int(radius)
            bob.circle(radius)
        except Exception as e:
            print(e)

    def turtle_color(self,event):
        clr = self.color_entry.get()
        bob.color(clr)

    def draw_dot(self):
        size = self.dot_entry.get()
        try:
            size=int(size)
            bob.dot(size)
        except Exception as e:
            print(e)
    def change_bgcolor(self,event):
        color = self.bgcolor_entry.get()
        x.bgcolor(color)

    def reset_all(self):
        bob.reset()
        #x.reset()
        x.bgcolor('white') 
    
    def change_bob_appearance(self,event):
        shape = self.turtle_shape_entry.get()
        bob.shape(shape)

    def striangle(self,depth,base):
        bob.speed(100)
        bob.pendown()
        if depth == 0:
            bob.begin_fill()
            for i in 0,1,2:
                bob.forward(base)
                bob.left(120)
            bob.end_fill()
        else:
            for i in 0,1,2:
                self.striangle(depth-1,base)
                bob.penup()
                bob.forward(base*2**depth)
                bob.left(120)
                bob.down()
################################################## TESTING CLASS INHERITENCES ###################################3

class LabeledScale(tk.Frame, tk.Scale):
    """A Ttk Scale widget with a Ttk Label widget indicating its
    current value.

    The Ttk Scale can be accessed through instance.scale, and Ttk Label
    can be accessed through instance.label"""

    def __init__(self, master=None, variable=None, from_=0, to=30, **kw):
        """Construct an horizontal LabeledScale with parent master, a
        variable to be associated with the Ttk Scale widget and its range.
        If variable is not specified, a tkinter.IntVar is created.

        WIDGET-SPECIFIC OPTIONS

            compound: 'top' or 'bottom'
                Specifies how to display the label relative to the scale.
                Defaults to 'top'.
        """
        tk.Scale.__init__(self)
        self._label_top = kw.pop('compound', 'top') == 'top'

        tk.Frame.__init__(self, master, **kw)
        #tk.Scale.__init__(self, master, **kw)
        self._variable = variable or tkinter.IntVar(master)
        self._variable.set(from_)
        self._last_valid = from_

        self.label = ttk.Label(self)
        self.scale = BriansScale()
        self.scale.bind('<<RangeChanged>>', self._adjust)

        # position scale and label according to the compound option
        scale_side = 'bottom' if self._label_top else 'top'
        label_side = 'top' if scale_side == 'bottom' else 'bottom'
        self.scale.pack(side=scale_side, fill='x')
        tmp = ttk.Label(self).pack(side=label_side) # place holder
        self.label.place(anchor='n' if label_side == 'top' else 's')

        # update the label as scale or variable changes
        self.__tracecb = self._variable.trace_variable('w', self._adjust)
        self.bind('<Configure>', self._adjust)
        self.bind('<Map>', self._adjust)


    def destroy(self):
        """Destroy this widget and possibly its associated variable."""
        try:
            self._variable.trace_vdelete('w', self.__tracecb)
        except AttributeError:
            # widget has been destroyed already
            pass
        else:
            del self._variable
            tk.Frame.destroy(self)


    def _adjust(self, *args):
        """Adjust the label position according to the scale."""
        def adjust_label():
            self.update_idletasks() # "force" scale redraw

            x, y = self.scale.coords()
            if self._label_top:
                y = self.scale.winfo_y() - self.label.winfo_reqheight()
            else:
                y = self.scale.winfo_reqheight() + self.label.winfo_reqheight()

            self.label.place_configure(x=x, y=y)

        from_ = _to_number(self.scale['from'])
        to = _to_number(self.scale['to'])
        if to < from_:
            from_, to = to, from_
        newval = self._variable.get()
        if not from_ <= newval <= to:
            # value outside range, set value back to the last valid one
            self.value = self._last_valid
            return

        self._last_valid = newval
        self.label['text'] = newval
        self.after_idle(adjust_label)


    def _get_value(self):
        """Return current scale value."""
        return self._variable.get()


    def _set_value(self, val):
        """Set new scale value."""
        self._variable.set(val)


    value = property(_get_value, _set_value)

     
root = RootWindow()
root.title('Dads Turtle')
root.mainloop()

