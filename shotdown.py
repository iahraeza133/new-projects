import os
def shotdown():
    if os.name=="nt":
        return os.system("shutdown /s /t 0")
    
    os.system("sudo shutdown -h now")
    
shotdown()