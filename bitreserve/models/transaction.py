import base_model

class Transaction(base_model.BaseModel):
  def __init__(self, client, data):
    super(Transaction, self).__init__(client, data)

  def commit(self):
    if not self.origin['CardId']:
      raise ValueError('Origin card id is missing from this transaction')
    if self.status != 'pending':
      raise ValueError('This transaction cannot be commited because the current status is %s' % self.status)
    response = self.client.post('/me/cards/%s/transactions/%s/commit' % (self.origin['CardId'], self.id))
    self.update_fields(response)

  def cancel(self):
    if not self.origin['CardId']:
      raise ValueError('Origin card id is missing from this transaction')
    if self.status == 'pending':
      raise ValueError('Unable to cancel uncommited transaction')
    if self.status != 'waiting':
      raise ValueError('This transaction cannot be canceled because the current status is %s' % self.status)
    response = self.client.post('/me/cards/%s/transactions/%s/cancel' % (self.origin['CardId'], self.id))
    self.update_fields(response)

  def resend(self):
    if not self.origin['CardId']:
      raise ValueError('Origin card id is missing from this transaction')
    if self.status != 'waiting':
      raise ValueError('This transaction cannot be resent because the current status is %s' % self.status)
    response = self.client.post('/me/cards/%s/transactions/%s/resend' % (self.origin['CardId'], self.id))
    self.update_fields(response)
