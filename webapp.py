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
    return render_template('second.html', nval = getStateOptions(states),yval = getYearOptions(states))
@app.route("/thi")
def render_page3():
    return render_template('third.html', nval = getStateOptions(states))

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
        ind = states.index(count)
        
        return render_template('response.html',nval = getStateOptions(states),yval = getYearOptions(states),name = na, year = ye, ls = str(states[ind]['Metrics']['Legitimacy']['Legitimacy Score']), pl = str(states[ind]['Metrics']['Legitimacy']['Political Legitimacy']), sel = str(states[ind]['Metrics']['Legitimacy']['Security Legitimacy']), el = str(states[ind]['Metrics']['Legitimacy']['Economic Legitimacy']), sl = str(states[ind]['Metrics']['Legitimacy']['Social Legitimacy']), es = str(states[ind]['Metrics']['Effectiveness']['Effectiveness Score']), pe = str(states[ind]['Metrics']['Effectiveness']['Political Effectiveness']), see = str(states[ind]['Metrics']['Effectiveness']['Security Effectiveness']), ee = str(states[ind]['Metrics']['Effectiveness']['Economic Effectiveness']), se = str(states[ind]['Metrics']['Effectiveness']['Social Effectiveness']), sfe = str(states[ind]['Metrics']['State Fragility Index']))
@app.route("/responsetwo")
def render_responsetwo():
        na = request.args['nameof']
        ye = str(request.args['year'])
        count = states[0]
        for i in states:
                if i['Country'] == na and i['Year'] == int(ye):
                        count = i
        ind = states.index(count)
        
        nat = request.args['nameoft']
        yet = str(request.args['yeart'])
        countt = states[0]
        for i in states:
                if i['Country'] == nat and i['Year'] == int(yet):
                        countt = i
        indt = states.index(countt)
        return render_template('responsetwo.html',nval = getStateOptions(states),yval = getYearOptions(states),name = na, year = ye, namet = nat, yeart = yet, ls = str(states[ind]['Metrics']['Legitimacy']['Legitimacy Score']), pl = str(states[ind]['Metrics']['Legitimacy']['Political Legitimacy']), sel = str(states[ind]['Metrics']['Legitimacy']['Security Legitimacy']), el = str(states[ind]['Metrics']['Legitimacy']['Economic Legitimacy']), sl = str(states[ind]['Metrics']['Legitimacy']['Social Legitimacy']), es = str(states[ind]['Metrics']['Effectiveness']['Effectiveness Score']), pe = str(states[ind]['Metrics']['Effectiveness']['Political Effectiveness']), see = str(states[ind]['Metrics']['Effectiveness']['Security Effectiveness']), ee = str(states[ind]['Metrics']['Effectiveness']['Economic Effectiveness']), se = str(states[ind]['Metrics']['Effectiveness']['Social Effectiveness']), sfe = str(states[ind]['Metrics']['State Fragility Index']), lst = str(states[indt]['Metrics']['Legitimacy']['Legitimacy Score']), plt = str(states[indt]['Metrics']['Legitimacy']['Political Legitimacy']), selt = str(states[indt]['Metrics']['Legitimacy']['Security Legitimacy']), elt = str(states[indt]['Metrics']['Legitimacy']['Economic Legitimacy']), slt = str(states[indt]['Metrics']['Legitimacy']['Social Legitimacy']), est = str(states[indt]['Metrics']['Effectiveness']['Effectiveness Score']), pet = str(states[indt]['Metrics']['Effectiveness']['Political Effectiveness']), seet = str(states[indt]['Metrics']['Effectiveness']['Security Effectiveness']), eet = str(states[indt]['Metrics']['Effectiveness']['Economic Effectiveness']), sett = str(states[indt]['Metrics']['Effectiveness']['Social Effectiveness']), sfet = str(states[indt]['Metrics']['State Fragility Index']))
@app.route("/responsethree")
def render_responsethree():
        ret = ""
        na = request.args['nameof']
        count = states[0]
        for i in states:
                if i['Country'] == na
                count = i
        ind = states.index(count)
        for i in states[ind]:
                ret += markup(",[\'" + str(i['year']) + "\'," + str(i['Metrics']['Legitimacy']['Legitimacy Score]') + "," + str(i['Metrics']['Effectiveness']['Effectiveness Score']) + "," + str(i['Metrics'][State Fragility Index]) + "]")
            
        return render_template('responsethree.html',nval = getStateOptions(states),graphVal = ret)
if __name__=="__main__":
    app.run(debug=False, port=54321)
