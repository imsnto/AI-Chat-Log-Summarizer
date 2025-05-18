from src import FileReader

def main():
    path = r'../chats/sql.txt'
    fr = FileReader()(path)

    print(fr.chat_history)
    print(fr.user_messages)
    print(fr.ai_messages)

if __name__ == '__main__':
    main()
