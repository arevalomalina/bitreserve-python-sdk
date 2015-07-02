from bitreserve.models import base_model
from bitreserve.models import card
from bitreserve.models import contact

class User(base_model.BaseModel):
    def get_card_by_id(self, card_id):
      response = self.client.get('/me/cards/%s' % card_id)
      return card.Card(self.client, response)

    def get_cards(self):
      response = self.client.get('/me/cards')

      cards = []
      for card_dict in response:
          cards.append(card.Card(self.client, card_dict))

      return cards

    def get_cards_by_currency(currency):
      response = self.client.get('/me/cards/')
      self.update_fields(response)
      cards = []
      for card_dict in response:
        if card_dict['currency'] == currency:
          cards.append(card.Card(self.client, card_dict))

      return cards

    def get_contacts(self):
        response = self.client.get('/me/contacts')

        contacts = []
        for contact_dict in response:
            contacts.append(contact.Contact(self.client, contact_dict))

        return contacts

    def get_balances(self):
      response = self.client.get('/me')
      self.update_fields(response)

      return self.balances['currencies']

    def get_balance_by_currency(self, currency):
      response = self.client.get('/me')
      self.update_fields(response)
      for balance in self.balances['currencies']:
        if balance['currency'] == currency:

          return balance['currency']

    def get_phones(self):
      response = self.client.get('/me/phones')
      self.phones = response

      return self.phones

    def get_settings(self):
      response = self.client.get('/me')
      self.update_fields(response)

      return self.settings

    def get_total_balance(self):
      response = self.client.get('/me')
      self.update_fields(response)
      balance_dict = {'amount':self.balances['total'],
                      'currency':self.settings['currency']}

      return balance_dict

    def get_transactions(self):
      response = self.client.get('/me/transactions')
      transactions = []
      for txn_dict in response:
          transactions.append(transaction.Transaction(self.client, txn_dict))

      return transactions

    def create_card(self, label, currency):
      response = self.client.post('/me/cards', {'label':label, 'currency':currency})

      return card.Card(self.client, response)

    def update(self):
      response = self.client.get('/me')
      self.update_fields(response)

      return self



    def __init__(self, client, data):
      self.country = None
      self.email = None
      self.first_name = None
      self.last_name = None
      self.name = None
      self.settings = None
      self.state = None
      self.status = None
      self.username = None
      super(User, self).__init__(client, data)

    def get_email(self):
      return self.email

    def get_first_name(self):
      return self.first_name

    def get_last_name(self):
      return self.last_name

    def get_name(self):
      return self.name

    def get_settings(self):
      return self.settings

    def get_state(self):
      return self.state

    def get_status(self):
      return self.status

    def get_username(self):
      return self.username
