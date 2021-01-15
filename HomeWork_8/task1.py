class KeyValueStorage:
    def __init__(self, filename):
        self.filename = filename
        self.inner_dict = {}
        with open(filename, "r") as file:
            for line in file:
                key, value = line.split("=")
                if key.isdigit():
                    raise ValueError("Key is digit")
                if value[-1] == "\n":
                    value = value[:-1]
                if value.isdigit():
                    value = int(value)

                self.inner_dict[key] = value

    def __getattr__(self, key):
        if key in self.inner_dict.keys():
            return self.inner_dict[key]
        return None

    def __getitem__(self, item):
        if item in self.inner_dict.keys():
            return self.inner_dict[item]
        return None
