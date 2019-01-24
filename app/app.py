from flask import Flask , render_template,request
app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])
def index():	  
	return render_template('index.html')
	
@app.route('/product', methods=['GET' , 'POST'])
def product():
	if request.method == 'POST':
		id = request.form['pid']
		name=request.form['pname']
		quant = request.form['quantity']
		pri = request.form['price']
		locat = request.form['location']
		return render_template('product.html', pid=id , pname=name , quantity=quant , price=pri , location=locat)
	  
	return render_template('index.html')
	
@app.route('/about')
def active():
	return render_template('about.html')

@app.route('/storage')
def storage():
	return render_template('storage.html')
	
if __name__ == "__main__":
  app.run();
