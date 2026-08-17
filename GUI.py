
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

                      
root Tk()
root.title("Premium Translator")
root.geometry ("530x760")
root.resizable (False, False)
bg Gradient Frame(root, "navy", "deep sky blue") bg.pack(fill-"both", expand=True)
title_label Label (bg, text=" UNI Translator", font ("Segoe UI Black", 36, "bold"), bg="navy", fg="white")
title_label.place ( x = 100 y = 40 )
separator Canvas (bg, width=330, height 3, bg="white", highlightthickness-0) separator.place ( x = 100 , y = 100 )
src_label Label (bg, text="Enter Text", font("Segoe UI Semibold", 18), bg="navy", fg="white")
src_label.place ( x = 200 y = 130 )
sor_txt Text (bg, font=("Segoe UI", 14), wrap=WORD, bg="white", fg="black",
relief-FLAT,bd = 61)
sor_txt.place ( x + 40 y = 170 height 160, width=450)

languages GoogleTranslator().get_supported_languages ()
style ttk.Style()
style.theme use("clam")
style.configure("TCombobox",
fieldbackground="white",
background="white",
bordercolor="black",
foreground "black",
padding=5)

comb_sor SearchableCombobox (bg, values languages, font=("Segoe UI", 12))
comb_sor.place( x = 40 y = 360 height=40, width=200)
comb_sor.set("english")
comb dest SearchableCombobox (bg, values-languages, font=("Segoe UI", 12))
comb dest.place ( x = 290 y = 360 height=40, width=200)
comb_dest.set("hindi")

def translate_text():
src comb_sor.get()
dest comb_dest.get()
text sor_txt.get("1.0", END)
try:
translated GoogleTranslator (source=src, target=dest).translate (text)
dest_txt.delete("1.0", END)
dest txt.insert (END, translated)
except Exception as e:
dest_txt.delete("1.0", END)
dest_txt.insert (END, "Error: " + str(e))                      
                      
