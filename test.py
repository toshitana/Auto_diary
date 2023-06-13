import guidance
import guidance

# set the default language model used to execute guidance programs
guidance.llm = guidance.llms.OpenAI("text-davinci-003")

"""
class Prompt:
    def __init__(self):
        pass

    def make_question(self, txt: str = "") -> str:
        b: str = txt
        return b

    def make_diary(self, *args) -> str:
        return " ".join(args)

"""

instruct = guidance("""
あなたは優秀な日記生成アシスタントAIです。あなたは日記作成のネタとして、3つの質問を行ってください。

$JSON_BLOB = {
    "question1": "質問1",
    "question2": "質問2",
    "question3": "質問3"

}

質問リストjson:{{gen 'result' n=5 temperature=0.9 max_tokens=256}}

""")

instruct_event = guidance("""
あなたは優秀な日記生成アシスタントAIです。あなたは日記作成のネタとして、イベントに沿った質問を3つ作成してください

イベント：{{event}}


$JSON_BLOB = 
{
    "question1": "質問1",
    "question2": "質問2",
    "question3": "質問3"

}

Question list json:{{gen 'result' n=1 temperature=1 max_tokens=256}}

""")

executed_program = instruct()

for thing in executed_program["result"]:
    print(thing)