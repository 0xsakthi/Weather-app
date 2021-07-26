from flask import Flask, render_template, request
import pyowm
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST','GET'])
def send(sum=sum):
    city = request.form['city'].upper()
    zipc = request.form['zipcode']
    owm =  pyowm.OWM('1afed1bcc62bc124f1824838273eed19')
    mgr = owm.weather_manager()
    obs = mgr.weather_at_zip_code('{}'.format(zipc),'IN')
    weather = obs.weather
    temperature = weather.temperature(unit='celsius')['temp']
    res1 = f'The Temperature : {temperature} degrees celsius.'
    res2 = 'The Current weather Of {}'.format(city)
    humidity = weather.humidity
    res3 = f'Humidity : {humidity}'
    current = weather.detailed_status
    res4 = f'Currently : {current}'
    return render_template('index.html',res1=res1, res2=res2,res3=res3,res4=res4)
