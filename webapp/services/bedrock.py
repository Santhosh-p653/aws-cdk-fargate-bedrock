import json
import boto3

client = boto3.client("bedrock-runtime")


def invoke_model(prompt: str) -> str:
    """
    Invoke an Amazon Bedrock model.
    """

    model_id = "amazon.nova-lite-v1:0"

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
        ]
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