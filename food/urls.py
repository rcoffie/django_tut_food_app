from django.urls import path

from . import views

app_name = "food"
urlpatterns = [
    #/food/ url for ClasBaseView
    path('',views.IndexClassView.as_view(), name='index'),
    #/food/ url for functional base view
    # path("", views.index, name="index"),
    #/food/1
    path("item/", views.item, name="item"),
    #detail view functional base view
    # path("<int:item_id>/", views.detail, name="detail"),
    #detail view classBaseview
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #add item functioal baseView
    # path('add',views.create_item, name='create_item'),
    #add item classBaseview
    path('add',views.CreateItem.as_view(),name='create_item'),
    #edit item_desc
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]
