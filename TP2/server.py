from flask import Flask, request, url_for, redirect, render_template, session
import json

app = Flask(__name__)
app.secret_key ="admin1234"

compteur=0

	
@app.route("/")
def TP1():
    if 'username' in session:
    	username =session['username'] 	
    	return render_template('TP1.html',username=username)
    return render_template('TP1.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
@app.route('/section', methods=['GET', 'POST'])
def section():
    return render_template('section.html')

@app.route('/lister', methods=['GET', 'POST'])
def lister():
    return render_template('lister.html')
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
    	print(request.form)
    	print(request.form.get("user_login"))
    	print(request.form.get("user_pswd"))
    	tabSession={}
    	login=request.form.get("user_login")
    	password = request.form.get("user_pswd")
    	with open('dataLogin.json','r') as my_file:
    	    	data=json.load(my_file)
    	    	
    	
    	tlg = [entry['login'] for entry in data['session']]
    	print(tlg)
    	tpswd = [entry['password'] for entry in data['session']]
    	print(tpswd)
    	x=0
    	for log in tlg:
    		print(log + " earaez")
    		print(str(x)+"eazr")
    		if log==login: 
    			for pwd in tpswd:
    				print(tpswd[x]+"nhnhfd")
    				if password==tpswd[x]:
    					session['username']=request.form['user_login']
    					return redirect(url_for('TP1'))
    		else:		
    		        x=x+1        		
    	return 'Login ou mot de passe incorect<br><a href="/login">Retenter</a>'	
    	
    return render_template('login.html')


@app.route('/register')
def register():
    with open('data.json','w') as my_file:
    	json.dump(t,my_file)    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('TP1'))    

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
        if request.method == 'POST':
        	print(request.form)
        return render_template('inscription.html')

@app.route('/forum', methods=['GET', 'POST'])
def forum():
        if 'username' in session:
                username =session['username'] 
                messages = request.get_json()
                return render_template('forum.html',username = username )	
        return render_template('forum.html')



@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
    	
    	print(request.form)
    	print(request.form.get("user_name"))
    	print(request.form.get("user_message"))
    	
    	tab={}
    	tab["name"]=request.form.get("user_name")
    	tab["msg"] = request.form.get("user_message")  #créer un tableau clé valeur avec le nom et le message 
    	with open('data.json','w') as my_file:
    		json.dump(tab,my_file)		#créer un fichier my_file et ecrit dans le fichier
    	 			#verifie si un fichier my_file n'existe pas
    			
     	
    return render_template('formulaire.html')

if __name__ == '__main__':
	app.run(debug=True)
