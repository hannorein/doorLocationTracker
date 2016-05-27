#import xml.etree.ElementTree as ET
import glob
import os
#import oec_plots
from flask import Flask, abort, render_template, send_from_directory, request, redirect, Response, make_response

class FlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskApp, self).__init__(*args, **kwargs)

app = FlaskApp(__name__)

@app.route('/')
@app.route('/index.html')
def page_planet_redirect():
	cur = """
	<html>
	<body>
	<form method="post" action="/recv/">
        """
        sfilen = "/home/rein/git/doorLocationTracker/status.html"
        sstr0 = "<dd><span class=\"week\">"
        with open(sfilen) as f:
            sf = f.readlines()

        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            status = "tbd"
            for r in sf:
                sstr = sstr0 + day
                if sstr in r:
                    if "tbd" in r:
                        status = "tbd"
                    if "away" in r:
                        status = "away"
                    if "utsc" in r:
                        status = "utsc"
                    if "utsg" in r:
                        status = "utsg"

            cur += """
            <label style="display: inline-block; width: 70px" for='"""+day+"""'>"""+day+""": </label>
            """
            for s in ["away","utsc","utsg","tbd"]:
                if status == s:
                    cur += """<input type="radio" name='"""+day+"""'  value='"""+s+"""' checked="checked">"""+s
                else:
                    cur += """<input type="radio" name='"""+day+"""'  value='"""+s+"""' >"""+s

            cur += """ <br />"""
	cur += """<input type="submit" />
	</form>
	</body>
	</html>
	"""
	return cur


@app.route('/recv/', methods=['POST'])
def hello():
        sfilen = "/home/rein/git/doorLocationTracker/status.html"
        sstr0 = "<dd><span class=\"week\">"
        with open(sfilen) as f:
            sf = f.readlines()

        with open(sfilen,"w") as f:
            for r in sf:
                for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                    sstr = sstr0 + day
                    if sstr in r:
                        r = "<dd><span class=\"week\">"+day+":</span> 		<span class=\""+request.form[day]+"\"></span></dd>\n"
                f.write(r)

        
	return "Saved. Message is now: <br/><br/>"


if __name__ == '__main__':
    app.run(debug=True,threaded=True)
