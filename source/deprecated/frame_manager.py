

class Frame_Manager():
    def __init__(self):
        self.frames = {}
    
    def add_frame(self, name, frame):
        self.frames[name] = frame
    
    def show_frame(self, name):
        for key in self.frames:
            self.frames[key].pack_forget()
        self.frames[name].pack(side="right", fill="both", expand=True)