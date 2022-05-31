from distutils.core import setup
import py2exe
#import sqlalchemy

setup( windows=[{"script" : "main.py"}], options={"py2exe" : {"packages": ["sqlalchemy.dialects.sqlite"] }})