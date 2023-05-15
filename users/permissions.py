STAFF = [
    'add_product', 
    'change_product',
    'view_product', 
    'delete_product', 

    'add_brand', 
    'change_brand', 
    'view_brand', 
    'delete_brand',

    'add_user', 
    'change_user', 
    'view_user',
    'delete_user', 

    'view_group'
]

STAFF_PERMS = [
    'auth.view_group',
    'auth.add_user',
    'auth.change_user',
    'auth.delete_user',
    'auth.view_user',
    'products.add_brand',
    'products.change_brand',
    'products.delete_brand',
    'products.view_brand',
    'products.add_product',
    'products.change_product',
    'products.delete_product',
    'products.view_product'
]

CLIENT = [
    'change_product',
    'view_product', 

    'view_brand', 

    'add_cart', 
    'change_cart', 
    'view_cart',

    'add_order', 
    'change_order',
    'view_order',
    'delete_order', 

    'change_user', 
    'view_user',
]

CLIENT_PERMS = [
    'products.change_product',
    'products.view_product', 

    'products.view_brand', 

    'shopping.add_cart', 
    'shopping.change_cart', 
    'shopping.view_cart',

    'shopping.add_order', 
    'shopping.change_order',
    'shopping.view_order',
    'shopping.delete_order', 

    'auth.change_user', 
    'auth.view_user',
]