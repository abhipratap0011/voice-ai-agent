class Memory:
    def __init__(self, max_turns: int = 10):
        self.max_turns = max_turns
        self.history = []

    def add(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns * 2:]

    def get(self) -> list:
        return self.history

    def clear(self):
        self.history = []