import openai
import json

# Step 1, send model the user query and what functions it has access to
def run_conversation():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": "あなたは優秀な日記生成アシスタントAIです。あなたは日記作成のネタとして、3つの質問を行ってください。"}],
        functions=[
            {
                "name": "show_three_questions",
                "description": "日記作成のための3つの質問を表示します",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "question1": {
                            "type": "string",
                            "description": "1つ目の質問"
                        },
                        "question2": {
                            "type": "string",
                            "description": "2つ目の質問"
                        },
                        "question3": {
                            "type": "string",
                            "description": "3つ目の質問"
                        }
                    }
                }
            }
        ],
        function_call="auto",
    )
    print(response)
    print("-------------------------------------")
    message = response["choices"][0]["message"]
    print(json.loads(message["function_call"]["arguments"]))
    print("-------------------------------------")

print(run_conversation())