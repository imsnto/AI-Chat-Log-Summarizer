import os
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from src.finetune import get_conversation_topic

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
        return {
            "ai_message_count": self.ai_message_count,
            "user_message_count": self.user_message_count,
            "total_message_count": self.total_message_count
        }

    def extract_keywords(self, top_n=5):
        messages = [dt['message'] for dt in self.chat_history]

        vectorizer = TfidfVectorizer(stop_words='english')
        # vectorizer = CountVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform(messages)

        feature_names = vectorizer.get_feature_names_out()
        sums = vectors.sum(axis=0)

        tfidf_scores = [(feature_names[i], sums[0, i]) for i in range(len(feature_names))]
        sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

        return [kw for kw, score in sorted_scores[:top_n]]

    def topic_of_conversation(self):
        conversation = ""
        for msg in self.chat_history:
            conversation += msg['role'] + " : " + msg['message'] + "\n"
        response = get_conversation_topic(conversation)
        return response

    def summary(self):
        topic = self.topic_of_conversation()
        common_keywords_list = self.extract_keywords()
        common_kw = ", ".join(common_keywords_list)

        print(f"Summary: \n"
              f"- The conversation had {self.total_message_count} exchanges.\n"
              f"- {topic}\n"
              f"- Most common keywords: {common_kw}.\n")

