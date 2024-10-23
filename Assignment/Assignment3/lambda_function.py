import pickle
import json

# load file
filename = 'iris_model.sav'
model = pickle.load(open(filename, 'rb'))

def predict(features):
    return model.predict(features).tolist()

def lambda_handler(event, context):
    try:
        # check body
        if 'body' in event:
            body = json.loads(event['body'])
            values = body.get('values', None)
        else:
            values = event.get('values', None)
        
        if values is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Missing input values.')
            }
        
        # get proper result
        features = values
        
        # run predict func
        prediction = predict(features)
        
        # Return result
        return {
            'statusCode': 200,
            'body': json.dumps({'prediction': prediction})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
