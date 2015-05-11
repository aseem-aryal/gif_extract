from moviepy.editor import *
import os
from Tkinter import *
import tkMessageBox
import tkFileDialog

def convert(start_time_m,start_time_s,end_time_m,end_time_s,saveas_filename):
	s= float((start_time_m.get()))
	t= float((start_time_s.get()))
	u= float((end_time_m.get()))
	v= float((end_time_s.get()))
	w = saveas_filename.get()		
	file = tkFileDialog.askopenfilename(initialdir='/')
    # Split the filepath to get the directory
    	filename = os.path.split(file)[0]+'/' + os.path.split(file)[1]
	clip = (VideoFileClip(filename)
        .subclip((s,t),(u,v))
        .resize(0.5))
	clip.write_gif(os.path.split(file)[0]+'/' +w + '.gif')

app = Tk()
app.title("Video Extractor")
start_time_m= Entry(app)
start_time_s= Entry(app)
end_time_m = Entry(app)
end_time_s= Entry(app)
saveas_filename = Entry(app)
Label(app, text="Starting Minute").pack(anchor = W)
start_time_m.pack(anchor = W)
Label(app, text="Starting Second and Microsecond").pack(anchor = W)
start_time_s.pack(anchor = W)
Label(app, text="Ending Minute").pack(anchor = W)
end_time_m.pack(anchor = W)
Label(app, text="Ending Second and Microsecond").pack(anchor = W)
end_time_s.pack(anchor = W)
Label(app, text="Output filename").pack(anchor = W)
saveas_filename.pack(anchor = W)
B1 = Button(app, text ="Convert", command = lambda: convert(start_time_m,start_time_s,end_time_m,end_time_s,saveas_filename))
B1.pack()
app.mainloop() 
