import requests

def stock_info():
    
    stock_syb = input("Enter Sybol ---> ").capitalize()

    url =f'https://api.freeapi.app/api/v1/public/stocks/{stock_syb}'

    respons =requests.get(url)
    objects = respons.json()

    if objects["success"] and "data" in objects:
        stock_data = objects["data"]
        # data = stock_data['data']
        name =stock_data["Name"]
        listing_date =stock_data["ListingDate"]
        marckte_cap =stock_data["MarketCap"]
        curent_price =stock_data["CurrentPrice"]
        high_low =stock_data["HighLow"]
        book_value = stock_data["BookValue"]
        face_vaule =stock_data["FaceValue"]
        roe = stock_data["ROE"]

        return  name, listing_date ,marckte_cap ,curent_price ,high_low ,book_value,face_vaule,roe
        

    else:
        raise Exception("Api not fecth")


def main():
    try:
        name ,listing_date ,maracket_cap , currnt_price ,high_low ,book_value,face_value, roe = stock_info()
        print(f"Name {name}")
        print(f"ListingDate {listing_date}")
        print(f"MarketCap {maracket_cap}")
        print(f"CurrentPrice {currnt_price}")
        print(f"HighLow {high_low}")
        print(f"BookValue {book_value}")
        print(f"FaceValue {face_value}")
        print(f"ROE {roe}")
        

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()