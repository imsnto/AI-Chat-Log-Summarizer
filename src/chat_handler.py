import os

class ChatHandler:
    def __init__(self):
        self.user_messages = []
        self.ai_messages = []
        self.chat_history = []

    @property
    def ai_message_count(self):
        return len(self.ai_messages)

    @property
    def user_message_count(self):
        return len(self.user_messages)

    @property
    def total_message_count(self):
        return self.ai_message_count + self.user_message_count

    def __call__(self, path=None):

        if not path or not isinstance(path, str):
            raise ValueError("Invalid path: Path must be a non-empty string.")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")

        with open(path, mode='r', encoding='utf-8') as file:
            is_user = True
            for line in file:
                if line.strip().startswith('User:'):
                    is_user = True
                    self.user_messages.append(line[5:-1])
                    self.chat_history.append({
                        'role': 'User',
                        'message': line[5:-1]
                    })
                elif line.strip().startswith('AI:'):
                    is_user = False
                    self.ai_messages.append(line[3:-1])
                    self.chat_history.append({
                        'role': 'AI',
                        'message': line[3:-1]
                    })
                else:
                    if is_user:
                        self.user_messages[-1] += " " + line[:-1]
                        self.chat_history[-1]['message'] += " " + line[:-1]
                    else:
                        self.ai_messages[-1] += " " + line[:-1]
                        self.chat_history[-1]['message'] += " " + line[:-1]
        return self

    def message_statistics(self):
        print("==============Count Messages==============")
        print(f"AI message count: {self.ai_message_count}")
        print(f"User message count: {self.user_message_count}")
        print(f"Total message count: {self.total_message_count}")

        print("===============Messages=====================")
        print(f"User Messages: {self.user_messages}")
        print(f"AI Messages: {self.ai_messages}")
        print(f"Chat history: {self.chat_history}")
