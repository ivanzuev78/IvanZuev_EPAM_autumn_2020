from collections import defaultdict


class KeyValueStorage(defaultdict):
    def __init__(self, filename):
        super().__init__()
        with open(filename, "r") as file:
            for line in file:
                key, value = line.split("=")
                if key.isdigit():
                    raise ValueError("Key is digit")
                if value[-1] == "\n":
                    value = value[:-1]
                if value.isdigit():
                    value = int(value)

                self[key] = value

    def __repr__(self):
        return super().__repr__()[:16] + super().__repr__()[22:]

    def __str__(self):
        return super().__repr__()[22:-1]
