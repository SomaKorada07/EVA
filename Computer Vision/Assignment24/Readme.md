# ResNet Assignment:

- conda create -n keras-dev python=3.6 pylint rope jupyter
- pip install tensorflow==1.12.0 keras==2.2.4 boto3 pillow

- sls create --template aws-python3 --name resnet50

- sls plugin install -n serverless-python-requirements@4.2.4

- sls invoke local --function resnet50-classify --path event.json
- Create another environment:
  - conda create -n keras-deploy python=3.6
  - pip install tensorflow==1.12.0 keras==2.2.4
  - pip freeze >> requirements.txt
  - sudo sls package

- Check for .requirements.zip file, unzip it and copy tensorflow folder to your kras-example folder

- Copy PIL folder from miniconda3/envs/keras-dev/lib/python3.6/site-packages

- Delete tmp, .requirements.zip, .requirements

- Change requirements.txt to match the versions supported by AWS Lambda

- 
  sudo sls deploy

- sls invoke --function resnet50-classify --path event.json




# Spacy Assignment:

- conda deactivate
- conda create -n spacy-dev python=3.6 pylint rope jupyter

- conda activate spacy-dev

- pip install spacy

- python -m spacy download en_core_web_sm

- sls create --template aws-python3 --name ner-api

- sls plugin install -n serverless-python-requirements@4.2.4


- Add in requirements.txt:
  spacy==2.1.3
  https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz

- sls invoke local --function recognize-named-entities --path event.json

- sudo sls deploy

- sls invoke --function recognize-named-entities --path event.json --log



# Final Static Website:


http://eva-assignment24.s3-website.ap-south-1.amazonaws.com/