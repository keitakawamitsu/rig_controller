#kmt_get_curves_info.py
import json
from maya import cmds as cmds

def get_curves_id(cv_name):
	"""選択したカーブのIDをJson書き出し
	"""
	id = cmds.getAttr((cmds.ls(sl=1)[0])+".cv[*]")

	JSONPATH = r"C:\work\script\rig_controller"
	JSONFILE = "test"
	EXT = ".json"

	file = JSONPATH+"/"+JSONFILE+EXT

	data = {cv_name:id}

	with open(file,"w") as f:
		json.dump(data, f)

	return id

if __name__ == "__main__":
	get_curves_id()