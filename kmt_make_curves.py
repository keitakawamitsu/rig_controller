import os
import json
import ast
from maya import cmds as cmds

class Curves:
	def __init__(self,cv_name,cv_distance):
		self.cv_name = cv_name# インスタンス変数で作りたい名前を受け取る
		self.cv_distance = cv_distance# カーブによってはdistanceが異なるため、ここも受け取る

		JSONPATH = os.path.dirname(__file__)+"/curves.json"
		_json_obj = open(JSONPATH)
		self.json_file = json.load(_json_obj)
		
		_id = self.json_file[self.cv_name][0]["ID"]#インスタンス変数で形を受け取る
		self.cv_id = ast.literal_eval(_id)
	
	def make_curves(self):
		if self.cv_name == "circle":
			self.curve_name	= cmds.circle(nr=(0,1,0),n=self.cv_name)
		
		else:
			self.curve_name = cmds.curve(n=self.cv_name,\
										d=self.cv_distance,\
										p=(self.cv_id))# jsonに書かれたカーブIDを元にカーブを生成

		return self.curve_name

	def move_cv(self):
		node = []
		node = cmds.ls(sl=1)

		if node:
			"""選択あったら選ばれてるノードにスナップ。何もなければ原点に作る
			"""
			for i in node:
				cv_name = self.make_curves()
				pos = cmds.xform(i,q=1,t=1,ws=1)
				rot = cmds.xform(i,q=1,ro=1,ws=1)
				cmds.xform(cv_name,t=pos)
				cmds.xform(cv_name,ro=rot)
		else:
			cv_name = self.make_curves()


