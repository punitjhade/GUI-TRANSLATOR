пер
from tkinter import *
from tkinter import ttk
from deep translator import GoogleTranslator
class GradientFrame (Canvas):
Canvas. init (self, parent, **kwargs)
def init (self, parent, colorl, color2, **kwargs): self.bind("<Configure>", self._draw_gradient)
self.colorl colorl
self.color2 color2
def draw gradient (self, event=None):
self.delete("gradient") width self.winfo width() height self.winfo height() (rl, gl, bl) self.winfo_rgb(self.colorl) (r2, g2, b2) self.winfo_rgh(self.color2) r_ratio float (r2r1) / limit
limit height
g_ratio float (g2 gl) / limit
bratio float (b2bl) / limit.
for i in range (limit):
nrint (rl+ (r ratio 1))
ngint (g1+ (g ratio 1))
nbint (bl+ (b ratio + i))
color f"(nr//256:02x){ng//256:02x)(nb//256:02x)" self.create line (0, i, width, i, tags("gradient",), fill=color)
self.lower("gradient")
Class SearchableCombobox(ttk.Combobox):
def init (self, master=None, **kwargs):
super(). init (master, **kwargs)
self._original_values list (self ['values']) self.bind('<KeyRelease>', self. filter_list)
def filter list (self, event):
typed self.get().lower()
if typed":
data self._original_values
else: data [item for item in self. original values if item.lower().startswith(typed)]
self['values'] = data
If data:
self.event generate('<Down>')
