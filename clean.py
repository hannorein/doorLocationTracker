sfilen = "/home/rein/git/doorLocationTracker/status.html"
sfilen2 = "/home/rein/git/doorLocationTracker/status_base.html"
sstr0 = "<dd><span class=\"week\">"
with open(sfilen) as f:
    sf = f.readlines()

with open(sfilen,"w") as f:
    for r in sf:
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            sstr = sstr0 + day
            if sstr in r:
                r = "<dd><span class=\"week\">"+day+":</span> 		<span class=\"tbd\"></span></dd>\n"
        f.write(r)
with open(sfilen2,"w") as f:
    for r in sf:
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            sstr = sstr0 + day
            if sstr in r:
                r = "<dd><span class=\"week\">"+day+":</span> 		<span class=\"tbd\"></span></dd>\n"
        f.write(r)
