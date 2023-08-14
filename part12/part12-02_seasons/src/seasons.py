# Write your solution here:
def order_by_season(item):
    return item["seasons"]

def sort_by_seasons(items: list):
    return sorted(items, key=order_by_season)