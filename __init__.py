import os
import shutil
import time
try:
    # for Python2
    from Tkinter import Tk 
except ImportError:
    # for Python3
    from tkinter import Tk
    
from binaryninja import *

class Funcs(object):
    def addtoclipboard(self,text):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update() # ensures it stays in the clipboard when window closes
        r.destroy()
        
    def disasm(self, bv, addr=0):
        text=""
        print(hex(addr))
        for block in bv.get_functions_containing(addr)[0].basic_blocks:
            for line in block.get_disassembly_text():
                text+=str(line)+"\n"
        self.addtoclipboard(text)
        binaryninja.interaction.show_message_box("Success","Copied Disasm to clipboard")
        
    def llil(self, bv, addr=0):
        text=""
        print(hex(addr))
        for current_llil in bv.get_functions_containing(addr)[0].low_level_il:
            for index in range(len(current_llil)):
                text += str(current_llil[index])+"\n"
        self.addtoclipboard(text)
        binaryninja.interaction.show_message_box("Success","Copied llil to clipboard")
        
    def mlil(self, bv, addr=0):
        text=""
        print(hex(addr))
        for current_mlil in bv.get_functions_containing(addr)[0].medium_level_il:
            for index in range(len(current_mlil)):
                text += str(current_mlil[index])+"\n"
        self.addtoclipboard(text)
        binaryninja.interaction.show_message_box("Success","Copied mlil to clipboard")

f = Funcs()

PluginCommand.register_for_address('- disasm2clipboard -', '', f.disasm)
PluginCommand.register_for_address('- llil2clipboard -', '', f.llil)
PluginCommand.register_for_address('- mlil2clipboard -', '', f.mlil)
