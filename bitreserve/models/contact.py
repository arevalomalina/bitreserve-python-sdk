import base_model

class Contact(base_model.BaseModel):
    def __init__(self, client, data):
      self.address = None
      super(Card, self).__init__(client, data)
