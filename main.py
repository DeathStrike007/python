from flask import Flask, send_file
import os
import json
app = Flask(__name__)
# подгружаю библиотеку и создаю объект типа фласк.

path = "C:\lol\kek"

# for i in os.listdir(path):
#    print(i)
PATH = "C:\lol"
def is_in_sandbox(path):
        return os.path.commonprefix([PATH, os.path.realpath(path)]) == PATH
print(is_in_sandbox("C:\Rel\kek"));


def getJsonTreeOfDir(path):
	d = {}
	d["name"] = os.path.basename(path) #Program Files (x86)
	d["path"] = path
	if os.path.isdir(path):
		d["ch"] = [getJsonTreeOfDir(os.path.join(path,ch)) for ch in os.listdir(path)]
	return d 



def delDir(path):
	os.rmdir(path)

def makeDir(dirPath):
	os.makedirs(dirPath)

# def fact(number, a):
# 	if number<=0:
# 		return 0
# 	a += number
# 	print(a)
# 	return fact(number-1,a)



# print(getJsonTreeOfDir(path))
# delDir(path)



@app.route("/getJson/<path:subpath>")
def getDir(subpath):
	return json.dumps(getJsonTreeOfDir(subpath))

@app.route("/createFolder/<path:subpath>")
def makeFuckingDir(subpath):
	makeDir(subpath)
	return subpath

@app.route("/deleteFolder/<path:subpath>")
def delFuckingDir(subpath):
	delDir(subpath)
	return subpath +" удалено!!!!!!"


@app.route("/downloadFile/<path:subpath>")
def downloadFuckingFile(subpath):
	return send_file(subpath,as_attachment=True)


# app.run(debug = True)
# поднять сервер

