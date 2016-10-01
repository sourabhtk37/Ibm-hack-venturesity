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
             'infobox': "<b>Store-1</b></br><button>chat</button>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Store-2</b></br><button>chat</button>"

          }
        ]
    )
    return render_template('map.html', sndmap=sndmap)

@app.route("/")
def  watson():
    conversation = ConversationV1(
    username='{oNPRR3mnN1IZ}',
    password='{4c126ddb-cd75-4151-80f6-2de0dcfcffc6}',
    version='2016-09-20'
    )

    # Replace with the context obtained from the initial request
    context = {}

    workspace_id = '05c6fbdc-15fb-4b64-9098-c92183978b18'

    response = conversation.message(
      workspace_id=workspace_id,
      message_input={'text': 'Turn on the lights'},
      context=context
    )

    print(json.dumps(response, indent=2))	

if __name__ == "__main__":
    app.run(debug=True)
