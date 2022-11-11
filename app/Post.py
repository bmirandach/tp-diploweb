class Post:
    post_id = 0

    def __init__(self, post_id, title, subtitle, description):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.post_id = post_id
    
    def getTitle(self):
        return self.title
    
    def getSubtitle(self):
        return self.subtitle

    def getDescription(self):
        return self.description

    def getPost_id(self):
        return self.post_id
    
    @classmethod
    def getNewPost_id(cls):
        cls.post_id += 1
        return cls.post_id 