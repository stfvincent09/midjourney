from flask import Flask, request, render_template
import json,time,requests
headers = {
	'Authorization': "Token r8_1Y7xysOyYPtKDdy8Ilw3bmch1MkFOWT3be4U8",
	'Content-Type': "application/json"
}
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        body = json.dumps(
	            {
		              "version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
 		              "input": { "prompt": q }
	            }
        )
        output = requests.post("https://api.replicate.com/v1/predictions", data=body, headers=headers)
        time.sleep(10)
        get_url = output.json()["urls"]["get"]
        get_result = requests.post(get_url,headers=headers).json()["output"]
        return(render_template("index.html",result=get_result[0]))
    else:
        return(render_template("index.html", result="waiting for image request............."))
if __name__ == "__main__":
    app.run()
