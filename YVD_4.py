import os
import yt_dlp
import tkinter
import tkinter.messagebox


class YOUTUBE():
    def __init__(self, default_path):
        self.mediatype = "mp4" 
        self.root = tkinter.Tk()
        self.root.title('YVD')
        self.root.minsize(900, 350)
        self.root.configure(bg='#101010')
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.default_path = default_path
        
        self.mp4checked = tkinter.BooleanVar(value=True)  
        self.mp3checked = tkinter.BooleanVar(value=False)

    def message_box(self, title, message):
        if title == 'ERROR':
            tkinter.messagebox.showerror(title, message)
        else:
            rootm = tkinter.Tk()
            rootm.geometry('450x250')
            rootm.configure(bg='#101010')
            rootm.title(title)
            tkinter.Label(rootm, text='Download Complete', font=('Helvetica', 20, 'normal'), bg='#101010', fg='#cccccc').grid(row=0, padx=10, pady=20, columnspan=2)
            tkinter.Label(rootm, text=message, font=('Helvetica', 20, 'normal'), bg='#101010', fg='#cccccc').grid(row=1, padx=10, pady=20, columnspan=2)
            tkinter.Button(rootm, text='OK', font=('Helvetica', 20, 'normal'), bg='#191b1d', fg='#cccccc', activebackground='#101010', activeforeground='#FFFFFF', command=lambda: rootm.destroy()).grid(row=2, column=0, pady=20)
            tkinter.Button(rootm, text='Open', font=('Helvetica', 20, 'normal'), bg='#191b1d', fg='#cccccc', activebackground='#101010', activeforeground='#FFFFFF', command=lambda: os.system(f'xdg-open "{self.file_path}"')).grid(row=2, column=1, pady=20)

    def update_mediatype(self):
        if self.mp4checked.get():
            self.mediatype = "mp4"
            self.mp3checked.set(False)
        else:
            self.mediatype = "mp3"
            self.mp4checked.set(False)

    def download(self):
        try:
            path = self.Path.get()
            url = self.URL_entry.get()
            if '/' not in path: 
                path = self.default_path
            
            if self.mediatype == "mp4":
                yt_opts = {
                    'format': 'bestvideo+bestaudio/best',  
                    'merge_output_format': 'mp4',
                    'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                    'bypass_nsig': True,
                }
            elif self.mediatype == "mp3":
                yt_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                    'bypass_nsig': True,
                }

            with yt_dlp.YoutubeDL(yt_opts) as vid:
                vid.download([url])
                info = vid.extract_info(url, download=False)
            filesize_approx = info.get('filesize_approx', 'N/A')
            
            if self.mediatype == "mp4":
                self.file_path = os.path.join(path, f"{info.get('title', 'N/A')}.mp4")
            else:
                self.file_path = os.path.join(path, f"{info.get('title', 'N/A')}.mp3")
                
            if self.mediatype == "mp3":
                os.system(f"cd '{path}'"+' && for file in *.mp4; do ffmpeg -i "$file" "${file%.mp4}.mp3" && rm -r "$file"; done ')
            
            print("\033c" + str(filesize_approx))
            self.message_box('Done', f"File size: {filesize_approx/1000000:.3f}MB ({filesize_approx} Bytes)")
        except Exception as ec:
            self.message_box('ERROR', f"ERROR: {str(ec)}")

    def gui(self):
        tkinter.Label(text='URL', fg='#cccccc', bg='#101010', font=('Helvetica', 25, 'normal')).grid(row=0, column=1, pady=15)
        self.URL_entry = tkinter.Entry(self.root, bg='#191b1d', fg='#cccccc', font=('Helvetica', 25, 'normal'), width=35)
        self.URL_entry.grid(row=1, column=1, pady=15)
        
        tkinter.Label(text='PATH', fg='#cccccc', bg='#101010', font=('Helvetica', 25, 'normal')).grid(row=2, column=1, pady=25)
        self.Path = tkinter.Entry(self.root, bg='#191b1d', fg='#cccccc', width=35, font=('Helvetica', 25, 'normal'))
        self.Path.grid(row=3, column=1, pady=15)
        
        checkbox_frame = tkinter.Frame(self.root, bg='#101010')
        checkbox_frame.grid(row=4, column=1, pady=10)
         
        mp4_checkbox = tkinter.Checkbutton(
            checkbox_frame, 
            text='MP4 (Video)', 
            variable=self.mp4checked,
            command=lambda: [self.mp3checked.set(False), self.update_mediatype()],
            bg='#101010', 
            fg='#cccccc',
            selectcolor='#191b1d',
            activebackground='#101010',
            activeforeground='#FFFFFF',
            font=('Helvetica', 16, 'normal')
        )
        mp4_checkbox.grid(row=0, column=0, padx=20)
        
        mp3_checkbox = tkinter.Checkbutton(
            checkbox_frame, 
            text='MP3 (Audio)', 
            variable=self.mp3checked,
            command=lambda: [self.mp4checked.set(False), self.update_mediatype()],
            bg='#101010', 
            fg='#cccccc',
            selectcolor='#191b1d',
            activebackground='#101010',
            activeforeground='#FFFFFF',
            font=('Helvetica', 16, 'normal')
        )
        mp3_checkbox.grid(row=0, column=1, padx=20)
        
        tkinter.Button(
            text='Download',
            fg='#cccccc',
            bg='#191b1d',
            command=self.download,
            font=('Helvetica', 25, 'normal'),
            padx=20,
            pady=15,
            activebackground='#101010',
            activeforeground='#FFFFFF'
        ).grid(row=5, column=1, pady=20)
        
        self.root.mainloop()

# Create the application
x = YOUTUBE(f'{os.path.expanduser("~")}/FDM/')
x.gui()
