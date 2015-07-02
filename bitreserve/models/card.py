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

    def create_transaction(self, destination, amount, currency):
      txn_dict = {'destination':destination,
                  'denomination':{'amount':amount, 'currency':currency}}
      response = self.client.post('/me/cards/%s/transactions' % self.id, txn_dict)


      return transaction.Transaction(self.client, response)

    def update(self, params):
      response = self.client.patch('/me/cards/%s' % self.id, params)
      self.update_fields(response)

      return self
