import base_model
from bitreserve.models import transaction

class Reserve(base_model.BaseModel):
    def __init__(self, client, data):
      super(Reserve, self).__init__(client, data)

    def get_ledger(self):
      response = self.client.get('/reserve/ledger')

      return response

    def get_statistics(self):
      response = self.client.get('/reserve/statistics')

      return response

    def get_transaction_by_id(self, txn_id):
      response = self.client.get('/reserve/transactions/%s' % txn_id )

      return transaction.Transaction(self.client, response)


    def get_transactions(self):
      response = self.client.get('/reserve/transactions')
      transactions = []
      for txn_dict in response:
          transactions.append(transaction.Transaction(self.client, txn_dict))

      return transactions


