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

    def get_contacts(self):
        response = self.client.get('/me/contacts')

        contacts = []
        for contact_dict in response:
            contacts.append(contact.Contact(self.client, contact_dict))

        return contacts

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
