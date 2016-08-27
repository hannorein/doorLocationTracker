activate_this = '/home/rein/git/doorLocationTracker/venv/bin/activate_this.py'
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))
import sys
sys.path.insert(0, '/home/rein/git/doorLocationTracker/')
from recserver import app as application
