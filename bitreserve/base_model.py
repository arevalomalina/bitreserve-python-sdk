class BaseModel(object):

    def __init__(self, client, data):
        self.client = client
        self.update_fields(data)

    def update_fields(self, data):
      for key in data:
        setattr(self, key, data[key])

    def get_client(self):
      return self.client
