from django.urls import path
from . import views

urlpatterns = [
	
	
	path('', views.home, name = 'home'),
	path('second', views.second, name = 'second'),
	path('modal', views.modal, name = 'modal'),
	path('modalsec', views.modalsec, name = 'modalsec'),
	path('third', views.third, name = 'third'),
	path('forth', views.forth, name = 'forth'),
	path('fifth', views.fifth, name = 'fifth'),
	path('sixth/<int:id>', views.sixth, name = 'sixth'),
	path('seventh/<int:id>', views.seventh, name = 'seventh'),
	path('test', views.test, name = 'test'),
	path('delete/<int:id>', views.delete, name = 'delete'),
	path('deleter/<int:id>', views.deleter,	 name = 'deleter'),
	path('editor/<int:id>/<slug:temp2>/<slug:temp1>', views.editor, name = 'editor'),
	path('edit/<int:id>/<slug:temp5>', views.edit, name = 'edit'),
	path('backtest', views.backtest, name = 'backtest'),
	path('thirdback', views.thirdback, name = 'thirdback'),
	path('exit', views.exit, name = 'exit'),
	
	]