import os
import json
import ast

from maya import cmds as cmds


class Curves:
	def __init__(self,cv_name):
		self.cv_name = cv_name# インスタンス変数で作りたい名前を受け取る
		JSONPATH = os.path.dirname(__file__)+"/curves.json"
		_json_obj = open(JSONPATH)
		self.json_file = json.load(_json_obj)
		
		print(JSONPATH)
		_id = self.json_file[self.cv_name][0]["ID"]#インスタンス変数で形を受け取る
		self.cv_id = ast.literal_eval(_id)

		#self.make_curves
		#self.make_cv
	
	def make_curves(self):
		self.cv_point= cmds.curve(d=1,p=(self.cv_id))# jsonに書かれたカーブIDを元にカーブを生成
		return self.cv_point

	def make_cv(self,cv_name):
		
		if self.cv_name == "circle":
			cmds.circle(nr=(0,1,0))

		elif self.cv_name == "cog":
			self.cv_point= cmds.curve(d=3,p=(self.cv_id))

