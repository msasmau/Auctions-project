from django.contrib import admin

from .models import *

# Register your models here.
class auction(admin.ModelAdmin):
    list_display = ("id" , "user", "active_bool","title" , "desc" , "starting_bid" , "image_url" , "category")

class watchl(admin.ModelAdmin):
    list_display = ("id", "watch_list" , "user")

class bid(admin.ModelAdmin):
    list_display = ("id","user","listingid","bid")

class comme(admin.ModelAdmin):
    list_display = ("id","user", "comment", "listingid")


admin.site.register(auctionlist, auction)
admin.site.register(bids, bid)
admin.site.register(comments, comme)
admin.site.register(watchlist, watchl)
