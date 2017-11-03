import glob, os
import errno
import shutil
from tkinter import *


from tkinter import Tk, Label, Button, W, ttk, filedialog

nmonth = ['nomonth','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


srcname = ""
dstname = ""

def mkdir_p(path):
        try:
                os.makedirs(path)
        except OSError as exc:  # Python >2.5
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                        pass
                else:
                        raise



class PicPathWindow:

	def __init__(self, proot):
		self.proot = proot
		proot.title("Picture categories")

		width = 450
		height = 150
		x = (proot.winfo_screenwidth() // 2) - (width // 2)
		y = (proot.winfo_screenheight() // 2) - (height // 2)

		proot.geometry('{}x{}+{}+{}'.format(width, height, x, y))

		self.label = Label(proot, text="Select Source Path", font=("Arial",12))
		self.label.grid(row=0,columnspan=2, sticky=W)

		self.greet_button = Button(proot, text="Browse", command=self.srcadd,font=("Arial",12))
		self.greet_button.grid(row=0,column=3)

		self.label = Label(proot, text="Select Destination Path", font=("Arial",12))
		self.label.grid(row=3,columnspan=2, sticky=W)


		self.greet_button = Button(proot, text="Browse", command=self.destadd,font=("Arial",12))
		self.greet_button.grid(row=3,column=3)


		self.close_button = Button(proot, text="OK", command=proot.quit,font=("Arial","14"))
		self.close_button.grid(row=8,column=2)

	def srcadd(self):
		global srcname	
		srcname = filedialog.askdirectory(parent=self.proot,initialdir="/",title='Please select source directory')
		if srcname: 
			try: 
				self.label = Label(self.proot, text='src: '+srcname, font=("Arial",12))
				self.label.grid(row=4,columnspan=2, sticky=W)
			except: 
				tkMessageBox.showerror("Source directory selection Failed !")
		print("Selected src path:",srcname)

	def destadd(self):
		global dstname
		dstname = filedialog.askdirectory(parent=self.proot,initialdir="/",title='Please select Destination directory')
		if dstname: 
			try: 
				self.label = Label(self.proot, text='dst: '+dstname, font=("Arial",12))
				self.label.grid(row=5,columnspan=2, sticky=W)

			except: 
				tkMessageBox.showerror("Destination dir selection Failed !")
		print("Selected dst path:",dstname)



root = Tk()
pic_GUI = PicPathWindow(root)
root.mainloop()
root.destroy()
fcount = 0
count = 0

os.chdir(srcname)

for file in glob.glob("*.jpg"):
	fcount+= 1

stsW = Tk()
stsW.title('Picture Organizer')
stsW.geometry('250x75')
stslabel = Label(stsW, text="Copying...", font=("Arial",12))
stslabel.pack()
mpb = ttk.Progressbar(stsW,orient ="horizontal",length = 200, mode ="determinate")
mpb.pack()
mpb["maximum"] = fcount


for file in glob.glob("*.jpg"):
	year = file[0:4]
	year = dstname+'/'+year
	month = file[4:6]
	month = year+'/' + nmonth[int(month)]
	mkdir_p(month)
	src_f = srcname+'/'+file

	try:
		shutil.copy(src_f, month)
	except IOError as e:
    		print("Unable to copy file. %s" % e)
	except:
    		print("Unexpected error:", sys.exc_info())
	#print(file)
	count+= 1
	mpb["value"] = count
	stsW.update_idletasks()

stsW.quit()



