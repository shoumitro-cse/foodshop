from public.models import Cart, CartItem, Product, Users


class Shopping:

    def __init__(self):
        pass

    def cart(self):
        pass

    def cartItem(self):
        pass

    def addCartItem(self, product_id, cart_obj, user_obj):
        product_check_list = Product.objects.filter(pk=product_id)
        if product_check_list:
            product_obj = Product.objects.filter(pk=product_id)[0]
            checkCart = CartItem.objects.filter(product=product_obj, user=user_obj)
            if not checkCart:
                # update cart
                cart_obj.totalItem += 1;
                cart_obj.totalCost += product_obj.price;
                cart_obj.save()

                p_quantity = 1
                totalCost = 0.0
                p_totalCost = totalCost + product_obj.price

                cart_item = CartItem(quantity=p_quantity, totalCost=p_totalCost, cart=cart_obj, product=product_obj, user=user_obj)
                cart_item.save()
                print("******Insert CartItem******")
            else:
                print("Product already exist in CartItem Table")
        else:
            print("Product is not exist")

    def addTocart(self, product_id, user_email):
        user_check_list = Users.objects.filter(email=user_email)
        if user_check_list:
            user_obj = user_check_list[0]
            cart_user_list = Cart.objects.filter(user=user_obj)
            if cart_user_list:
                # cart_obj = Cart.objects.order_by("-id")[0:1][0]
                cart_obj = cart_user_list[0]
                self.addCartItem(product_id, cart_obj, user_obj)
            else:
                cart = Cart(totalItem=0, totalTaxed=0.0, discount=0.0, deliveryCost=0.0, totalCost=0.0, user=user_obj)
                cart.save()
                cart_obj = cart
                self.addCartItem(product_id, cart_obj, user_obj)
        else:
            print('User Not Exist')

    def getCart(self, user_obj):
        cart_list = Cart.objects.filter(user=user_obj)
        if cart_list:
            return cart_list[0]
        else:
            return None

    def getCartProduct(self, user_obj):
        cart_list = self.getCart(user_obj)
        pass




