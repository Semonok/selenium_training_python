

def test_delete_items_in_shopping_cart(app):
    items = 2
    app.add_items_in_shopping_cart(items)
    assert app.quantity_item_in_shopping_cart_on_main_page() == items
    app.remove_all_items_in_shopping_cart()
    assert app.text_when_shopping_cart_list_is_empty() == "There are no items in your cart."