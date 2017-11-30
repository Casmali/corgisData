from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open("state_fragility.json") as fragility_data:
        states = json.load(fragility_data)

@app.route("/")
def render_main():
    return render_template('index.html')
@app.route("/fir")
def render_page1():
    return render_template('first.html',nval = getStateOptions(states),yval = getYearOptions(states))
@app.route("/sec")
def render_page2():
    return render_template('second.html')
@app.route("/thi")
def render_page3():
    return render_template('third.html')

def getStateOptions(states):
    ret = ""
    lis = {"doestmantter":True}
    for i in states:
        if not(i["Country"] in lis):
            ret += Markup("<option value=\"" + i['Country'] + "\">" + i['Country'] + "</option>")
            lis[i["Country"]] = True
    return ret
def getYearOptions(states):
    ret = ""
    lis = {"doestmantter":True}
    for i in states:
        if not(str(i["Year"]) in lis):
            ret += Markup("<option value=\"" + str(i['Year']) + "\">" + str(i['Year']) + "</option>")
            lis[str(i['Year'])] = True
    return ret

@app.route("/response")
def render_response():
        na = request.args['nameof']
        ye = str(request.args['year'])
        count = states[0]
        for i in states:
                if i['Country'] == na and i['Year'] == int(ye):
                        count = i
        ind = states.index(i)
        
        return render_template('response.html',nval = getStateOptions(states),yval = getYearOptions(states),name = na, year = ye, ls = str(states[i]['Metrics']['Legitimacy']['Legitimacy Score']), pl = str(states[i]['Metrics']['Legitimacy']['Political Legitimacy']), sel = str(states[i]['Metrics']['Legitimacy']['Security Legitimacy']), el = str(states[i]['Metrics']['Legitimacy']['Economic Legitimacy']), sl = str(states[i]['Metrics']['Legitimacy']['Social Legitimacy']), es = str(states[i]['Metrics']['Effectiveness']['Effectiveness Score']), pe = str(states[i]['Metrics']['Effectiveness']['Political Effectiveness']), see = str(states[i]['Metrics']['Effectiveness']['Security Effectiveness']), ee = str(states[i]['Metrics']['Effectiveness']['Economic Effectiveness']), se = str(states[i]['Metrics']['Effectiveness']['Social Effectiveness']), sfe = str(states[i]['Metrics']['State Fragility Index"]))
@app.route("/responsetwo")
def render_responsetwo():
        
        return render_template('responsetwo.html', their = request.args['inches'], response = res)
@app.route("/responsethree")
def render_responsethree():
        ins = float(request.args['miles'])
        #The request object stores information that was sent by the client to the server.
        #the args is a multidict
        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
        res = str(ins*63360)
        return render_template('responsethree.html', their = request.args['miles'], response = res)
if __name__=="__main__":
    app.run(debug=False, port=54321)
