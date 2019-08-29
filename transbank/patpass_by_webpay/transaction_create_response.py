class TransactionCreateResponse(object):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def __str__(self):
        return "token: {}, url: {}".format(self.token, self.url)
