#import xml.etree.ElementTree as ET
import glob
import os
from shutil import copyfile
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
        sfilen = "/home/rein/git/doorLocationTracker/status_base.html"
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
            for s in ["utsc","utsg","tbd","away"]:
                if status == s:
                    cur += """<input type="radio" name='"""+day+"""'  value='"""+s+"""' checked="checked">"""+s
                else:
                    cur += """<input type="radio" name='"""+day+"""'  value='"""+s+"""' >"""+s

            cur += """ <br />"""
        sfilen = "/home/rein/git/doorLocationTracker/status.html"
        with open(sfilen) as f:
            sf = f.readlines()

        text = ""
        for r in sf:
            if "<h1>" in r:
                text = (r[4:])[:-6]
        if text == "Hanno Rein":
            text = ""

        cur += """ <br />"""
        cur += "Manual text: <input type=\"text\" name=\"text\" value=\""+text+"\"><br>"
        cur += """ <br />"""
        cur += """ <br />"""
        cur += """ Check e-mails: """
        if os.path.isfile("./checkmail.txt"):
            cur += """<input type="radio" name="email"  value="on" checked="checked"> on"""
            cur += """<input type="radio" name="email"  value="off"> off"""
        else:
            cur += """<input type="radio" name="email"  value="on"> on"""
            cur += """<input type="radio" name="email"  value="off" checked="checked"> off"""
        cur += """ <br />"""
        cur += """ <br />"""
        cur += """<input type="submit" />
        </form>
        </body>
        </html>
        """
        return cur


@app.route('/recv/', methods=['POST'])
def hello():
        sfilen = "/home/rein/git/doorLocationTracker/status_base.html"
        sfilen2 = "/home/rein/git/doorLocationTracker/status.html"
        sfilen3 = "/home/rein/git/doorLocationTracker/dnd.html"
        sstr0 = "<dd><span class=\"week\">"
        with open(sfilen) as f:
            sf = f.readlines()

        with open(sfilen2,"w") as f:
            for r in sf:
                for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                    sstr = sstr0 + day
                    if sstr in r:
                        r = "<dd><span class=\"week\">"+day+":</span>               <span class=\""+request.form[day]+"\"></span></dd>\n"
                f.write(r)
        copyfile(sfilen2, sfilen)
        if len(request.form["text"])>0:
            # Manual text 
            with open(sfilen3) as f:
                sf = f.readlines()

            with open(sfilen2,"w") as f:
                for r in sf:
                    if "<h1>" in r:
                        r = "<h1>"+request.form["text"]+"</h1>\n"
                    f.write(r)

        return "Saved. <br/><br/>"


if __name__ == '__main__':
    app.run(debug=True,threaded=True)
