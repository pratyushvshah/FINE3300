class Bond:
    def __init__(self, coupon_rate, face_value, years_to_maturity):
        self.__coupon_rate = coupon_rate 
        self.__face_value = face_value 
        self.__years_to_maturity = years_to_maturity

    def price(self, market_rate):
        r = market_rate / 2
        n = self.__years_to_maturity * 2
        coupon_pmt = (self.__coupon_rate * self.__face_value) / 2

        if r == 0:
            pv_coupons = coupon_pmt * n
            pv_face = self.__face_value
        else:
            pv_coupons = coupon_pmt * (1 - (1 + r) ** -n) / r
            pv_face = self.__face_value / (1 + r) ** n

        return pv_coupons + pv_face

    def current_yield(self, current_price):
        annual_coupon = self.__coupon_rate * self.__face_value
        return annual_coupon / current_price
    
def main():
    bond = Bond(0.05,100,5)
    price = bond.price(0.12)
    print(f"The price of the bond is: {price}")
    print(f"The current yield of the bond is: {bond.current_yield(price)}")

if __name__ == "__main__":
    main()