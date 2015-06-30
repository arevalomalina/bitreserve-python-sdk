import base_model
from bitreserve.models import transaction


class Card(base_model.BaseModel):
    def __init__(self, client, data):
      self.address = None
      super(Card, self).__init__(client, data)

    def get_transactions(self):
      response = self.client.get('/me/cards/%s/transactions' % self.id)
      transactions = []
      for txn_dict in response:
          transactions.append(transaction.Transaction(self.client, txn_dict))

      return transactions
