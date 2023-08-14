# TEE RATKAISUSI TÄHÄN:
def order_by_rating(item):
    return item["rating"]

def sort_by_ratings(items: list):
    return sorted(items, key=order_by_rating, reverse=True)