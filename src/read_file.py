
class FileReader:
    def __init__(self):
        self.user_messages = []
        self.ai_messages = []
        self.chat_history = []

    def __call__(self, path=None):
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