from nltk.chat.util import Chat, reflections
pairs = [
            [
                r"Hai",
                ["Hai Juga..."]
            ],

            [ 
                r"saya (.*)",
                ["hai %1. apakabar hari ini ?"]
            ],
            
            [
                r"baik",
                ["Alhamdulillah saya turut senang, ada yang bisa saya bantu ?"]
            ],

            [
                r"lagi sakit hari ini",
                ["Semoga lekas sembuh"]
            ]
        ]

def firstChatbot():
    print("Hai Saya STIKBOTS kamu siapa ?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == '__main__':
    firstChatbot()