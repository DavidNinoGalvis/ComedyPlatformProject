class DashboardManager:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        if key not in self.data:
            self.data[key] = value
        else:
            raise KeyError(f"Key {key} already exists.")

    def read(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError(f"Key {key} not found.")

