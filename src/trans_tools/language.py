



class Trans:

    def __init__(self, tmap):
        self.tmap = tmap

    def transliterate(self, text):
        for k, v in self.tmap.items():
            text = text.replace(k, v)

        return text
