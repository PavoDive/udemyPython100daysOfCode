# An Online Shop

An eCommerce website with payment processing.

Using what you have learnt by building the blog website using Flask, you're now going to build your own eCommerce website. Your website needs to have a working cart and checkout.

It should be able to display items for sale and take real payment from users.

It should have login/registration authentication features.

Here is an example website:

https://store.waitbutwhy.com/


You should consider using the Stripe API:

https://stripe.com/docs/payments/checkout

# Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ I'll break with Flask, and take this chance to know Django. 😱
+ From the limited knowledge I have of Django I'll try to have 4 apps:
    + Authentication
	+ Display of items
	+ Cart and
	+ Checkout

## Implementation Details

+ Following instructions at https://docs.djangoproject.com/en/5.0/intro/tutorial01/
+ Created a project called "shops"
+ Created an app called "products"
+ created a view for index
+ created the products/urls.py file and started populating the urlpatterns.
+ updated the shop/shop/urls.py
+ Create a model for products
+ Possible fields in models are here: https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types
+ Had to fix the settings MEDIA_ROOT in order to use ImageField in the model
+ There are so many steps, that's easy to get lost and forget whhere in the process I am. Django seems very robust, but it's very intricate.
+ But it is very powerful, when compared to Flask. Even though I'm kind of overwhelmed by the whole process, I'm glad I decided to try Django for this assignment.
+ The authentication is quite a load. I've been reading about allauth for some minutes now, and it seems like a ton of work, parts of which are not compatible with what I've done so far.
+ I finally nailed down the authentication thing, with the help of several blogs and videos. Particularly [this video](https://www.youtube.com/watch?v=RyB_wdEZhOw&t=130s) and [this blog](https://www.digitalocean.com/community/tutorials/how-to-authenticate-django-apps-using-django-allauth).
+ I will skip the aestethic corrections of the app, as I'd have to go and fight bootstrap for a little while, and I'm more concerned about really getting a grasp on Django.
+ This is considerable more difficult and with a lot more things that I considered at first. I not only have to take care of products, users and orders, but also addresses, and I'm very far from ever implementing stripe 😰
+ This project was very difficult for me, and had a lot of scope traps. I ended up scaling it down from what I wanted initially. I didn't even implement the stripe part, as it had some javascript.
    + On the bright side, I learned some Django.
    + On the dark side, I didn't get nearly to have a functional site.
+ Planning is 80% of coding. I jumped right away to start coding, and my plan was very vague and weak. That had a price, and I payed it in time and reprocessing.
