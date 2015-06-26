import base_model
import card

class User(base_model.BaseModel):
    def get_card_by_id(self, card_id):
        response = self.client.get('/me/cards/%s' % card_id)
        return card.Card(self.client, response)









