import os
import yt_dlp
import tkinter


class YOUTUBE():
    def __init__(self,default_path):
        self.root = tkinter.Tk()
        self.root.title('YVD')
        self.root.minsize(900,350)
        self.root.configure(bg='#0d0e0f')
        self.default_path = default_path
    def message_box(self,title,message):
        if title == 'ERROR':
            tkinter.messagebox.showerror(title,message)
        else:
            rootm = tkinter.Tk()
            rootm.geometry('450x250')
            rootm.configure(bg='#0d0e0f')
            rootm.title(title)
            tkinter.Label(rootm,text='Download Complete',font=('Helvetica',20,'normal'),bg='#0d0e0f',fg='#cccccc').grid(row=0,padx=10,pady=20,columnspan=2)
            tkinter.Label(rootm,text=message,font=('Helvetica',20,'normal'),bg='#0d0e0f',fg='#cccccc').grid(row=1,padx=10,pady=20,columnspan=2)
            tkinter.Button(rootm,text='OK',font=('Helvetica',20,'normal'),bg='#191b1d',fg='#cccccc',activebackground='#0d0e0f',activeforeground='#FFFFFF',command=lambda:rootm.destroy()).grid(row=2,column=0,pady=20)
            print(self.file_path)
            tkinter.Button(rootm,text='Open',font=('Helvetica',20,'normal'),bg='#191b1d',fg='#cccccc',activebackground='#0d0e0f',activeforeground='#FFFFFF',command=lambda:os.system(f'xdg-open "{self.file_path}"')).grid(row=2,column=1,pady=20)

    def download(self):
        try:
            path = self.Path.get()
            url = self.URL_entry.get()
            if '/' not in path : 
                path = self.default_path

            yt_opts = {
                'format':'best',
                'outtmpl': os.path.join(path,'%(title)s.%(ext)s'),
                'bypass_nsig': True,

            }
            with yt_dlp.YoutubeDL(yt_opts) as vid:
                vid.download([url])
                info = vid.extract_info(url, download=False)
            filesize_approx = info.get('filesize_approx','N/A')
            self.file_path = self.default_path+info.get('title','N/A')+'.'+info.get('ext','mp4')
            self.message_box('Done',f"File size: {filesize_approx/1000000:.3f}MB ({filesize_approx} Bytes)")
        except Exception as ec:
            self.message_box('ERROR',f"ERROR :  {str(ec)}")
    def gui(self):
        tkinter.Label(text='URL',fg='#cccccc',bg='#0d0e0f',font=('Helvetica',25,'normal')).pack(pady=15)
        self.URL_entry = tkinter.Entry(self.root,bg='#191b1d',fg='#cccccc',font=('Helvetica',25,'normal'),width=35)
        self.URL_entry.pack(pady=15)
        tkinter.Label(text='PATH',fg='#cccccc',bg='#0d0e0f',font=('Helvetica',25,'normal')).pack(pady=25)
        self.Path = tkinter.Entry(self.root,bg='#191b1d',fg='#cccccc',width=35,font=('Helvetica',25,'normal'))
        self.Path.pack(pady=15)
        tkinter.Button(text='Download',fg='#cccccc',bg='#191b1d',command=self.download,font=('Helvetica',25,'normal'),padx=20,
            pady=15,activebackground='#0d0e0f',activeforeground='#FFFFFF').pack(pady=20)
        
        self.root.mainloop()
x = YOUTUBE(f'{os.path.expanduser("~")}/FDM/')
x.gui()
