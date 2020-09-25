import os, sys
import uuid 
import pyqrcode
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, send_file, request
app = Flask(__name__)

@app.route('/')
def qr_gen():
	sourceUrl = request.args.get('sourceUrl')
	sourceName = request.args.get('sourceName')
	sourcrName3 = str(uuid.uuid1())
	imgQR = pyqrcode.create(sourceUrl)
	imgQR.png(sourcrName3 + '.png', scale=6, module_color=(0, 0, 0, 128), background=(0xff, 0xff, 0xff))
	img = Image.open(sourcrName3 + '.png')
	position = (5,5)
	message = sourceName
	color = (255,255,255)
	draw = ImageDraw.Draw(img)
	draw.text(position, message)
	qrname = sourcrName3 + '.png'
	return send_file(qrname, mimetype='image/png')