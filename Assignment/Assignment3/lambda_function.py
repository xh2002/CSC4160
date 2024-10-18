import pickle
import json

# 加载模型
filename = 'iris_model.sav'
model = pickle.load(open(filename, 'rb'))

def predict(features):
    return model.predict(features).tolist()

def lambda_handler(event, context):
    try:
        # 检查'body'字段，如果存在则解析其内容
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
        
        # 将输入值转换为适当的格式
        features = [values]
        
        # 调用预测函数
        prediction = predict(features)
        
        # 返回预测结果
        return {
            'statusCode': 200,
            'body': json.dumps({'prediction': prediction})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
