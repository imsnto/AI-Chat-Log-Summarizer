from src import ChatHandler

def message_statistics(ch: ChatHandler):
    print("==============Count Messages==============")
    print(f"AI message count: {ch.ai_message_count}")
    print(f"User message count: {ch.user_message_count}")
    print(f"Total message count: {ch.total_message_count}")

    print("===============Messages=====================")
    print(f"User Messages: {ch.user_messages}")
    print(f"AI Messages: {ch.ai_messages}")
    print(f"Chat history: {ch.chat_history}")


def main():
    path = r'../chats/sql.txt'
    ch = ChatHandler()(path)

    message_statistics(ch)


if __name__ == '__main__':
    main()
