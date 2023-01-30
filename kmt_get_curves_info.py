# aa
import json
from maya import cmds as cmds

class Curve():
	def __init__(self):
		pass

	def get_curves_id(self,cv_name):
		"""選択したカーブのIDをJson書き出し
		"""
		id = cmds.getAttr((cmds.ls(sl=1)[0])+".cv[*]")

		#JSONPATH = r"C:\work\script\rig_controller"
		#JSONFILE = "test"
		#EXT = ".json"

		#file = JSONPATH+"/"+JSONFILE+EXT

		data = {cv_name:id}

		#with open(file,"w") as f:
		#	json.dump(data, f)

		return data
