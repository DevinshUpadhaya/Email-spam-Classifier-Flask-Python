from flask import Flask,render_template,request #micro web ferame work for python
import pickle # for serializing & deserialixin python object
# render template render html tmplate, request is object from flask 
# contain info about current http
app = Flask(__name__)


pipe = pickle.load(open("Naive_model.pkl","rb")) # loading pre train model

@app.route('/', methods=["GET","POST"]) #request from root
def main_function():
    if request.method == "POST":
        text = request.form
        # print(text)
        #when get request made return html url
        emails = text['email']
        print(emails)
        
        list_email = [emails]
        # print(list_email)
        output = pipe.predict(list_email)[0]
        print(output)


        return render_template("show.html", prediction = output)
    
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)