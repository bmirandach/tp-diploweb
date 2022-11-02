class Post:
    post_id = 0

    def __init__(self, post_id, title, description):
        self.title = title
        self.description = description
        self.post_id = post_id
    
    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description

    def getPost_id(self):
        return self.post_id
    
    @classmethod
    def getNuevoPost_id(cls):
        cls.post_id += 1
        return cls.post_id 