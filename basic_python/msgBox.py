import tkMessageBox
def TF(a,b):
    if a>b:
        return tkMessageBox.showinfo(title="a>b", message="True")
    else:
        return tkMessageBox.showinfo(title="a<b", message="False")
    
