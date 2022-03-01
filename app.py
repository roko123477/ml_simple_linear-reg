
from flask import Flask,render_template, request
import pickle


app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub",methods=["POST"])
def submit():
    if(request.method=="POST"):
        area=request.form["username"]
        prediction=model.predict([[area]])
        output = round(prediction[0], 2)

    return render_template("sub.html", n=output)



if __name__=="__main__":
    app.run(debug=True)

