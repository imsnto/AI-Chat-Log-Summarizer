from src import ChatHandler, extract_keywords


def main():
    path = r'../chats/sql.txt'
    ch = ChatHandler()(path)
    ch.message_statistics()

    top_5_keywords = extract_keywords(ch.chat_history)

    print(top_5_keywords)


if __name__ == '__main__':
    main()
