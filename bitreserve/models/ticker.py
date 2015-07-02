from bitreserve.models import base_model

class Ticker(base_model.BaseModel):
    def __init__(self, client, data):
      super(Ticker, self).__init__(client, data)
