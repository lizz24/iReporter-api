class Incident:
  
    def __init__(self, *args):
        self.id = args[0]
        self.createdOn = args[1]
        self.createdBy = args[2]
        self.type = args[3]
        self.location = args[4]
        self.status = args[5]
        self.Images = args[6]
        self.Videos = args[7]
        self.comment = args[8]

    def get_incident(self):
        return {
            "id": self.id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "type": self.type,
            "location": self.location,
            "status": self.status,
            "Images": self.Images,
            "Videos": self.Videos,
            "comment": self.comment
        }
