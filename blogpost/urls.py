from django.urls import path
from . import views
from .views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate, Excel, AllList, AllUpdate
from .views import SRMList, SRMDetail, SRMUpdate, SRMCreate, SRM_opupdate, Top, St_List, St_Create, St_Update, SRM_OpList, Options, St_Opupdate, St_Oplist, Word_List, Word_Update, St_Opcreate, Word_Create
from .views import signupview, loginview, logoutview ,SRMglaph

urlpatterns = [
    path('top/', Top.as_view(), name='Top'),

    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),

    path('SRM/SRMlist/', SRMList.as_view(), name='SRMlist'),
    path('SRM/SRMglaph/', SRMList.as_view(), name='SRMglaph'),
    path('SRM/SRMdetail/<str:pk>/', SRMDetail.as_view(), name='SRMdetail'),
    path('SRM/SRMupdate/<str:pk>/', SRMUpdate.as_view(), name='SRMupdate'),
    path('SRM/SRMcreate/', SRMCreate.as_view(), name='SRMcreate'),
    
    path('stpoint/st_list/', St_List.as_view(), name='St_list'),
    path('stpoint/st_create/', St_Create.as_view(), name='St_create'),
    path('stpoint/st_update/<str:pk>/', St_Update.as_view(), name='St_update'),
    
    path('options/op_list/', Options.as_view(), name='Options'),
    path('options/SRM_oplist/', SRM_OpList.as_view(), name='SRM_oplist'),
    path('options/SRM_opupdate/<str:pk>', SRM_opupdate.as_view(), name='SRM_opupdate'),
    path('options/st_oplist', St_Oplist.as_view(), name='St_oplist'),
    path('options/st_opcreate', St_Opcreate.as_view(), name='St_Opcreate'),
    path('options/st_opupdate/<str:pk>', St_Opupdate.as_view(), name='St_opupdate'),
    path('options/word_list', Word_List.as_view(), name='Word_list'),
    path('options/word_create', Word_Create.as_view(), name='Word_Create'),
    path('options/word_update/<str:pk>', Word_Update.as_view(), name='Word_update'),
    
    path('SRMglaph/', views.get_svg, name='glaph1'),
    
    #以下不使用　paiza用
    path('list/', BlogList.as_view(),name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(),name='detail'),
    path('create/', BlogCreate.as_view(),name='create'),
    path('delete/<int:pk>/', BlogDelete.as_view(),name='delete'),
    path('update/<int:pk>/', BlogUpdate.as_view(),name='update'),
    path('excel/', Excel.as_view(), name='excel'), 
    path('allupdate/', AllUpdate.as_view(), name='allupdate'),
 
    ]