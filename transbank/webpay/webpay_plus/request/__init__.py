from typing import List, Any, Iterator


class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, amount: float, return_url: str):
        self.buy_order = buy_order
        self.session_id = session_id
        self.amount = amount
        self.return_url = return_url

    def __repr__(self):
        return "TransactionCreateRequest(buy_order: {}, session_id: {}, amount: {}, return_url: {})".format(
            self.buy_order, self.session_id, self.amount, self.return_url)


class TransactionRefundRequest(object):
    def __init__(self, amount: float):
        self.amount = amount

    def __repr__(self):
        return "TransactionRefundRequest(amount: {})".format(self.amount)


class MallDetails(object):
    def __init__(self, amount: float, commerce_code: str, buy_order: str):
        self.amount = amount
        self.commerce_code = commerce_code
        self.buy_order = buy_order

    def __repr__(self):
        return "MallDetails(amount: {}, commerce_code: {}, buy_order: {})".format(
            self.amount, self.commerce_code, self.buy_order)

    def __eq__(self, other) -> bool:
        if type(other) is not MallTransactionCreateDetails:
            return False

        return self.amount == other.amount and self.commerce_code == other.commerce_code \
            and self.buy_order == other.buy_order


class MallTransactionCreateDetails(object):
    __details: List[MallDetails] = []

    def __init__(self, amount: float, commerce_code: str, buy_order: str):
        self.add(amount, commerce_code, buy_order)

    def add(self, amount: float, commerce_code: str, buy_order: str) -> "MallTransactionCreateDetails":
        mall_details = MallDetails(amount, commerce_code, buy_order)
        self.__details.append(mall_details)
        return self

    def remove(self, amount: float, commerce_code: str, buy_order: str) -> None:
        mall_details = MallDetails(amount, commerce_code, buy_order)
        self.__details.remove(mall_details)

    @property
    def details(self) -> Iterator[MallDetails]:
        return tuple(self.__details)


class MallTransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, return_url: str, details: List[MallDetails]):
        self.buy_order = buy_order
        self.session_id = session_id
        self.return_url = return_url
        self.details = details
