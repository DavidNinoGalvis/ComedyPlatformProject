class Ticket:
    def __init__(self, price, buyerID, category, phase, saleCode, paymentMethod, refundMethod, isActive=True):
        self.price = price
        self.buyerID = buyerID
        self.category = category
        self.phase = phase
        self.saleCode = saleCode
        self.paymentMethod = paymentMethod
        self.refundMethod = refundMethod
        self.isActive = isActive

    def deactivate(self):
        self.isActive = False

    def updatePrice(self, newPrice):
        self.price = newPrice

    def updateBuyerID(self, newBuyerID):
        self.buyerID = newBuyerID

    def updateCategory(self, newCategory):
        self.category = newCategory

    def updatePhase(self, newPhase):
        self.phase = newPhase

    def updateSaleCode(self, newSaleCode):
        self.saleCode = newSaleCode

    def updatePaymentMethod(self, newPaymentMethod):
        self.paymentMethod = newPaymentMethod

    def updateRefundMethod(self, newRefundMethod):
        self.refundMethod = newRefundMethod
