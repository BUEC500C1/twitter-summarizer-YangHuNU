import os
from google.cloud import vision

def google_vision(image_uri):

	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'linear-pointer-266422-c333968edede.json'

	# image_uri = 'gs://cloud-samples-data/vision/label/wakeupcat.jpg'

	client = vision.ImageAnnotatorClient()
	image = vision.types.Image()
	image.source.image_uri = image_uri

	response = client.label_detection(image=image)

	result = 'Labels (and confidence score):\n'
	for label in response.label_annotations:
	    result+=f'{label.description} ({label.score*100.:.2f}%)\n'
	return result