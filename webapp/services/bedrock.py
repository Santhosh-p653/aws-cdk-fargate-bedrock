import json
import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)


def invoke_model(prompt: str) -> str:
    """
    Invoke Amazon Bedrock lightweight model.
    """

    model_id = "amazon.nova-micro-v1:0"

    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 512,
            "temperature": 0.5,
            "topP": 0.9
        }
    }

    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    result = json.loads(response["body"].read())

    try:
        return result["output"]["message"]["content"][0]["text"]
    except Exception:
        return str(result)