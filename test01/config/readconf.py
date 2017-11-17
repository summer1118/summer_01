# coding=utf-8
import os, ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__)) #获取当前文件所在上级目录
config_path = os.path.join(cur_path,'my_config') #获取配置文件所在绝对路径
con = ConfigParser.ConfigParser() #实例化读取配置文件类
con.read(config_path)#读取配置文件路径
index_url = con.get('url','index_url')#读取url



