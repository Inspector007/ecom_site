from django.test import TestCase

# Create your tests here.

from core.models import Item
cat = ['Shirt', 'Casualwear', 'sport']
label = ['primary','secondary', 'danger']
cat = ['Shirt', 'Outwear', 'Sport wear']
price = [30, 40, 50, 33, 35, 25]
discount = [2,1,3]
catg = ['S','SW','OW']
lab = ['P','S','D']
for i in range(1000000):
    random.shuffle(cat)
    random.shuffle(label)
    random.shuffle(price)
    random.shuffle(discount)
    xt = ['casual.jpeg','party.jpg','shirt.jpg','sport.jpg']
    random.shuffle(xt)
    random.shuffle(catg)
    random.shuffle(lab)
    im = Item(title=cat[1]+str(i),price=price[1],discount_price=discount[1],
    	category=catg[1],label=lab[1],slug=cat[1]+str(i),description='testing',image=xt[1])
    im.save()