from flask import Flask, redirect, url_for, render_template, request, session, flash
from itertools import chain, combinations
import ast 
import pandas 
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

app = Flask(__name__)
app.secret_key = 'bigchungus'
rules = pandas.read_csv("mil_rules.csv", header=0)
rules_electrical = pandas.read_csv("mil_rules_electrical.csv", header=0)

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "POST":
        items = request.form.get("item")
        added = request.form.get("add_quote")
        re = request.form.get("reset")
        rec = request.form.get("rec")
        
        if rec:
            if rec not in session['item']:
                temp = session['item']
                temp.append(rec.replace("~"," "))
                session['item'] = temp
            sets = list(powerset(session['item'][-4:]))
            sets = list(map(set, sets))
            cons = []

            for index, row in rules.iterrows():
                if set(ast.literal_eval(row['antecedent'])) in sets and ast.literal_eval(row['consequent'])[0] not in cons and ast.literal_eval(row['consequent'])[0] not in session['item']:
                    cons.append(ast.literal_eval(row['consequent']))
                if len(cons) > 2:
                    break;
            cons_stripped = []
            for string in cons:
                cons_stripped.append(string[0].replace(" ","~"))
            return render_template("item_select.html",  i = session['item'], last_items = cons, last_items_stripped = cons_stripped)
        
        if added and items:
            if 'item' in session:
                if items not in session['item']:
                    temp = session['item']
                    temp.append(items)
                    session['item'] = temp
            else:
                session['item'] = [items]
            sets = list(powerset(session['item'][-4:]))
            sets = list(map(set, sets))
            cons = []

            for index, row in rules.iterrows():
                if set(ast.literal_eval(row['antecedent'])) in sets and ast.literal_eval(row['consequent'])[0] not in cons and ast.literal_eval(row['consequent'])[0] not in session['item']:
                    cons.append(ast.literal_eval(row['consequent']))
                if len(cons) > 2:
                    break;
            cons_stripped = []
            for string in cons:
                cons_stripped.append(string[0].replace(" ","~"))
            return render_template("item_select.html",  i = session['item'], last_items = cons, last_items_stripped = cons_stripped)
        elif re:
            session.pop('item', None)
            return render_template("item_select.html", i = "")
        else:
            return render_template("item_select.html", i = "")
    else:
        return render_template("item_select.html", i = "")

@app.route("/electrical", methods = ["POST","GET"])
def electrical():
    if request.method == "POST":
        items = request.form.get("item")
        added = request.form.get("add_quote")
        re = request.form.get("reset")
        rec = request.form.get("rec")
        
        if rec:
            if rec not in session['item_electrical']:
                temp = session['item_electrical']
                temp.append(rec.replace("~"," "))
                session['item_electrical'] = temp
            sets = list(powerset(session['item_electrical'][-4:]))
            sets = list(map(set, sets))
            cons = []

            for index, row in rules_electrical.iterrows():
                if set(ast.literal_eval(row['antecedent'])) in sets and ast.literal_eval(row['consequent']) not in cons and ast.literal_eval(row['consequent'])[0] not in session['item_electrical']:
                    cons.append(ast.literal_eval(row['consequent']))
                if len(cons) > 2:
                    break;
            cons_stripped = []
            for string in cons:
                cons_stripped.append(string[0].replace(" ","~"))
            return render_template("electric_item_select.html",  i = session['item_electrical'], last_items = cons, last_items_stripped = cons_stripped)
        
        if added and items:
            if 'item_electrical' in session:
                if items not in session['item_electrical']:
                    temp = session['item_electrical']
                    temp.append(items)
                    session['item_electrical'] = temp
            else:
                session['item_electrical'] = [items]
            sets = list(powerset(session['item_electrical'][-4:]))
            sets = list(map(set, sets))
            cons = []

            for index, row in rules_electrical.iterrows():
                if set(ast.literal_eval(row['antecedent'])) in sets and ast.literal_eval(row['consequent']) not in cons and ast.literal_eval(row['consequent'])[0] not in session['item_electrical']:
                    cons.append(ast.literal_eval(row['consequent']))
                if len(cons) > 2:
                    break;
            cons_stripped = []
            for string in cons:
                cons_stripped.append(string[0].replace(" ","~"))
            return render_template("electric_item_select.html",  i = session['item_electrical'], last_items = cons, last_items_stripped = cons_stripped)
        elif re:
            session.pop('item_electrical', None)
            return render_template("electric_item_select.html", i = "")
        else:
            return render_template("electric_item_select.html", i = "")
    else:
        return render_template("electric_item_select.html")
if __name__ == "__main__":
    app.run(debug = True)
