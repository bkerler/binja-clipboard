Binary Ninja Clipboard Plugin

## Why

In order to reconstruct or better understand structure, it's sometimes
necessary to copy the current function disasm, llil or mlil to clipboard
for other programs to use (like Notepad++).

## Installation
* You will need a python installation with Tkinter (in every regular python version,
except the binary ninja bundled one)
* Make sure your PYTHONPATH variable points to the python directory, otherwise binary ninja won't start
* See example settings.json files in this repo for python2 and python3 to set up your own python
* Inside your [Binary Ninja plugins folder](https://github.com/Vector35/binaryninja-api/tree/master/python/examples#loading-plugins), run:
```
git clone https://github.com/bkerler/binja-clipboard.git
```

## Usage
* Click into the function you want to disasm/llil/mlil
* Select Tools, - disasm2clipboard - to copy current disassembly to the clipboard
* Select Tools, - llil2clipboard - to copy current llil content to the clipboard
* Select Tools, - mlil2clipboard - to copy current mlil content to the clipboard


## Built on top of
* Binary ninja

```
MIT License

Copyright (c) 2018 B. Kerler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```