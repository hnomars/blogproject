from django.urls import path
from . import views
from .views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate, Excel, AllList, AllUpdate
from .views import SRMList, SRMDetail, SRMUpdate, SRMCreate, SRMCreate2, SRM_opupdate, Top, St_List, St_Create, St_Update, SRM_OpList, Options, Word_Update, Word_List, Word_Create, St_Opupdate, St_Oplist, St_Opcreate
from .views import Exer_Create, Exer_List, Exer_Update, Exer_Detile, Exer_Delete, Moni_Create, Moni_List, Moni_Update, Moni_Detile, Moni_Delete 
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
    path('SRM/SRMcreate2/', SRMCreate2.as_view(), name='SRMcreate2'),
    
    path('stpoint/st_list/', St_List.as_view(), name='St_list'),
    path('stpoint/st_create/', St_Create.as_view(), name='St_create'),
    path('stpoint/st_update/<str:pk>/', St_Update.as_view(), name='St_update'),
    
    path('monitoring/list/', Moni_List.as_view(), name='Moni_List'),
    path('monitoring/create/', Moni_Create.as_view(), name='Moni_Create'),
    path('monitoring/update/<str:pk>/', Moni_Update.as_view(), name='Moni_Update'),
    path('monitoring/delete/<str:pk>/', Moni_Delete.as_view(), name='Moni_Delete'),
    path('monitoring/detail/<str:pk>/', Moni_Detile.as_view(), name='Moni_Detile'),

    path('exercise/list/', Exer_List.as_view(), name='Exer_List'),
    path('exercise/create/', Exer_Create.as_view(), name='Exer_Create'),
    path('exercise/update/<str:pk>/', Exer_Update.as_view(), name='Exer_Update'),
    path('exercise/delete/<str:pk>/', Exer_Delete.as_view(), name='Exer_Delete'),
    path('exercise/detail/<str:pk>/', Exer_Detile.as_view(), name='Exer_Detile'),

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