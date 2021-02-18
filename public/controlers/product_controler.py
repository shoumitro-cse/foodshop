from public.models import Users, Login, Product, ProductInfo, Category, ProductCategory

class ProductData:

    def __init__(self):
        pass

    def getTotalProductByCategory(self):
        category_list = []
        category = Category.objects.all()
        for c_item in category:
            category_dict = {}
            category_dict["category_name"] = c_item.name
            productCategoryObj = ProductCategory.objects.filter(category=c_item)
            product_category_list = []
            for pc_item in productCategoryObj:
                product_category_dict = {}
                product_category_dict["product_category_name"] = pc_item.name
                product = Product.objects.filter(productCategory=pc_item)
                product_dict_list = []
                for item in product:
                    product_dict = {}
                    product_dict['id'] = item.id
                    product_dict['name'] = item.name
                    product_dict['keyword'] = item.keyword
                    product_dict['weight'] = item.weight
                    product_dict['brand'] = item.brand
                    product_dict['stock'] = item.stock
                    product_dict['currentStock'] = item.currentStock
                    product_dict['price'] = item.price
                    product_dict['unitPrice'] = item.unitPrice
                    product_dict['taxed'] = item.taxed
                    productInfo = ProductInfo.objects.filter(product=item)
                    for p_item in productInfo:
                        product_dict['desc1'] = p_item.desc1
                        product_dict['desc2'] = p_item.desc2
                        product_dict['desc3'] = p_item.desc3
                        product_dict['desc4'] = p_item.desc4
                        # product_dict['image1'] = p_item.image1.__str__()
                        product_dict['image1'] = p_item.image1.name
                        product_dict['image2'] = p_item.image2.name
                        product_dict['image3'] = p_item.image3.name
                        product_dict['image4'] = p_item.image4.name
                    product_dict_list.append(product_dict)
                product_category_dict["product_list"] = product_dict_list
                product_category_list.append(product_category_dict)
            category_dict["product_category"] = product_category_list
            category_list.append(category_dict)
        return category_list

    def getProductById(self, id):
        product = Product.objects.filter(pk=id)
        product_dict = {}
        for item in product:
            product_dict['id'] = item.id
            product_dict['name'] = item.name
            product_dict['keyword'] = item.keyword
            product_dict['weight'] = item.weight
            product_dict['brand'] = item.brand
            product_dict['stock'] = item.stock
            product_dict['currentStock'] = item.currentStock
            product_dict['price'] = item.price
            product_dict['unitPrice'] = item.unitPrice
            product_dict['taxed'] = item.taxed
            productInfo = ProductInfo.objects.filter(product=item)
            for p_item in productInfo:
                product_dict['desc1'] = p_item.desc1
                product_dict['desc2'] = p_item.desc2
                product_dict['desc3'] = p_item.desc3
                product_dict['desc4'] = p_item.desc4
                # product_dict['image1'] = p_item.image1.__str__()
                product_dict['image1'] = p_item.image1.name
                product_dict['image2'] = p_item.image2.name
                product_dict['image3'] = p_item.image3.name
                product_dict['image4'] = p_item.image4.name
        return product_dict

    def getTotalProduct(self, page=False):

        product = Product.objects.all()
        # product = Product.objects.db_manager("default").all() #here db=> default from settings.py
        # product = Product.objects.raw("select * from Product") #product from raw sql

        product_dict_list = []
        for item in product:
            product_dict = {}
            product_dict['id'] = item.id
            product_dict['name'] = item.name
            product_dict['keyword'] = item.keyword
            product_dict['weight'] = item.weight
            product_dict['brand'] = item.brand
            product_dict['stock'] = item.stock
            product_dict['currentStock'] = item.currentStock
            product_dict['price'] = item.price
            product_dict['unitPrice'] = item.unitPrice
            product_dict['taxed'] = item.taxed
            productInfo = ProductInfo.objects.filter(product=item)
            for p_item in productInfo:
                product_dict['desc1'] = p_item.desc1
                product_dict['desc2'] = p_item.desc2
                product_dict['desc3'] = p_item.desc3
                product_dict['desc4'] = p_item.desc4
                # product_dict['image1'] = p_item.image1.__str__()
                product_dict['image1'] = p_item.image1.name
                product_dict['image2'] = p_item.image2.name
                product_dict['image3'] = p_item.image3.name
                product_dict['image4'] = p_item.image4.name
            product_dict_list.append(product_dict)
        return product_dict_list