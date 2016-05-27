activate_this = '/home/rein/git/doorLocationTracker/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, '/home/rein/git/doorLocationTracker/')
from recserver import app as application
