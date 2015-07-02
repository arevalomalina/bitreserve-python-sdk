from bitreserve.models import base_model

class Token(base_model.BaseModel):
    def __init__(self, client):
      super(Token, self).__init__(client, data)
