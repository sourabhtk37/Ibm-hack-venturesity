from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from watson_developer_cloud import ConversationV1


app = Flask(__name__, template_folder="./templates")
GoogleMaps(app)

@app.route("/")
def mapview():
    # creating a map in the view
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Walmart</b></br><p>Tomato : $5</br>Onion: $5</p><button>Chat</button>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Mega Buy</b></br><p>PS4-collective : $499 </br>Xbox-Forza Edition : $599</p><button>chat</button>"

          }
        ]
    )
    #watson()
    #take_message()
    #message()
    return render_template('map.html', sndmap=sndmap)


@app.route("/")
def  watson():
    conversation = ConversationV1(
    username='{<api-key>}',
    password='{api-key}',
    version='2016-09-20'
    )

    # Replace with the context obtained from the initial request
    context = {}

    workspace_id = '<api-key>'

    response = conversation.message(
      workspace_id=workspace_id,
      message_input={'text': 'Buy me a PS4'},
      context=context
    )

    print(json.dumps(response, indent=2))	

@app.route('/', methods=['POST'])
def take_message():
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/')
def message():
    return render_template('message.html', message="Buy me tomato")    

if __name__ == "__main__":
    app.run(debug=True)
