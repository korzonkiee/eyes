class ImgEntity:
    id = 0
    personId = 0
    img = None

    def __init__(self, id, personId, img):
        self.id = id
        self.personId = personId
        self.img = img

    def show_id(self):
        print (self.id)