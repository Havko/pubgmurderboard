import http.client
import json
import boto3
import time
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('player_stats')
    response = table.scan()
    print(response)
    for item in response['Items']:
        user = item['player_id']
        total_kills = 0
        conn = http.client.HTTPConnection("api.pubgtracker.com")
        #Update TRN-Api-Key header with pubgtracker API key
        headers = {
            'TRN-Api-Key': "{INSERT PUBGTRACKER API KEY}",
            'Cache-Control': "no-cache",
            }
        
        conn.request("GET", "/v2/profile/pc/"+user+"?region=agg", headers=headers)
        
        res = conn.getresponse()
        data = res.read()
        
        my_data = data.decode("utf-8")
        my_data = json.loads(my_data)
        print(my_data)
        stats = my_data['Stats']
        
        for mode in stats:
            for reg_stats in mode['stats']:
                if reg_stats['label'] == 'Kills':
                    total_kills += reg_stats['valueInt']
        print(total_kills)
        table.update_item(
            Key={
                'player_id': user
            }, 
            UpdateExpression='SET total_kills = :val1', 
            ExpressionAttributeValues={
                ':val1': total_kills
                
            }
        )
        time.sleep(3)
    
