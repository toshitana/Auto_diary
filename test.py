import guidance
import guidance

# set the default language model used to execute guidance programs
guidance.llm = guidance.llms.OpenAI("text-davinci-003")

# define a guidance program that adapts a proverb
program = guidance("""Tweak this proverb to apply to model instructions instead.

{{proverb}}
- {{book}} {{chapter}}:{{verse}}

UPDATED
Where there is no guidance{{gen 'rewrite' stop="\\n-"}}
- GPT {{#select 'chapter'}}9{{or}}10{{or}}11{{/select}}:{{gen 'verse'}}""")

# execute the program on a specific proverb
executed_program = program(
    proverb="Where there is no guidance, a people falls,\nbut in an abundance of counselors there is safety.",
    book="Proverbs",
    chapter=11,
    verse=14
)
print(executed_program)
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

program1 = guidance("""
あなたは優秀な日記生成アシスタントAIです。あなたは日記を作成するために3つの質問を行ってください。

イベントが与えられたら、イベントに沿った質問を3つの内1つ加えてください。
{{event}}

""")

program2 = guidance("""
質問と回答のペアが3つあります。これらは日記作成のためにサンプルされました。
これらの質問と回答のペアを用いて日記を作成してください。
Data:{{date}}

question:{{question}}
answer:{{answer}}

question:{{question}}
answer:{{answer}}

question:{{question}}
answer:{{answer}}
""")