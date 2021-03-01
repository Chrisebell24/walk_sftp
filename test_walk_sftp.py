import sys
import os
fp = os.path.dirname( os.path.abspath( __file__))
fp = os.path.join(fp, 'src')
sys.path.insert(0, fp)
from walk_sftp import WalkSFTP
from walk_ftp import WalkFTP

def test_exists():
    assert WalkSFTP != None

def test_exists2():
    assert WalkFTP != None