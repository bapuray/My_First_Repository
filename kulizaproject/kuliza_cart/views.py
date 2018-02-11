from django.shortcuts import render
from kuliza_cart.models import Product, ItemSubCategory, ItemCategory, Cart, MyCatalog
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from kuliza_cart.forms import LoginForm, ProductForm, ItemSubCategoryForm, ItemCategoryForm, CatalogForm
from django.contrib.auth.decorators import login_required
 


def login_user(request):
	if request.method == 'GET':
		form = LoginForm()
		context = {
			'form':form
		}
		return render(request,'login.html',context)
	elif request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/home/')		
		context = {
			'form':form
		}
		return render(request,'login.html',context)

@login_required(login_url='/login/')
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/login/')	

@login_required(login_url='/login/')
def products(request):
	products_list = Product.objects.all()
	if request.method == 'GET':
		form = ProductForm()
		context = {
			'form':form,
			'products_list':products_list
		}
		return render(request,'products.html',context)
	elif request.method == 'POST':
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			form_save = form.save(commit=False)
			form_save.img = form.cleaned_data['img']
			form_save.save()
			return HttpResponseRedirect('/products/')
		context = {
			'form':form,
			'products_list':products_list
		}
		return render(request,'products.html',context)


@login_required(login_url='/login/')
def update_product(request, pk):
	obj = Product.objects.get(pk=pk)
	if request.method == 'GET':
		form = ProductForm(instance=obj)
		context = {
			'form':form
		}
		return render(request,'products.html',context)
	elif request.method == 'POST':
		form = ProductForm(request.POST,request.FILES,instance=obj)
		if form.is_valid():
			form_save = form.save(commit=False)
			form_save.img = form.cleaned_data['img']
			form_save.save()
			return HttpResponseRedirect('/products/')
		context = {
			'form':form
		}
		return render(request,'products.html',context)

@login_required(login_url='/login/')
def add_to_cart(request, pk):
	obj = Product.objects.get(pk=pk)
	if request.method == 'GET':
		created, exists = Cart.objects.get_or_create(product=obj,item_qty=0,user=request.user.id,sold=False)
		return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def delete_product(request, pk):
	obj = Product.objects.get(pk=pk)
	if request.method == 'GET':
		obj.delete()
		return HttpResponseRedirect('/products/')

@login_required(login_url='/login/')
def update_category(request, pk):
	obj = ItemCategory.objects.get(pk=pk)
	if request.method == 'GET':
		form = ItemCategoryForm(instance=obj)
		context = {
			'form':form
		}
		return render(request,'category.html',context)
	elif request.method == 'POST':
		form = ItemCategoryForm(request.POST,instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/category/')
		context = {
			'form':form
		}
		return render(request,'category.html',context)

@login_required(login_url='/login/')
def delete_category(request, pk):
	obj = ItemCategory.objects.get(pk=pk)
	if request.method == 'GET':
		obj.delete()
		return HttpResponseRedirect('/category/')

@login_required(login_url='/login/')
def update_subcategory(request, pk):
	obj = ItemSubCategory.objects.get(pk=pk)
	if request.method == 'GET':
		form = ItemSubCategoryForm(instance=obj)
		context = {
			'form':form
		}
		return render(request,'subcategory.html',context)
	elif request.method == 'POST':
		form = ItemSubCategoryForm(request.POST,instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/subcategory/')
		context = {
			'form':form
		}
		return render(request,'subcategory.html',context)

@login_required(login_url='/login/')
def delete_subcategory(request, pk):
	obj = ItemSubCategory.objects.get(pk=pk)
	if request.method == 'GET':
		obj.delete()
		return HttpResponseRedirect('/subcategory/')

@login_required(login_url='/login/')
def subcategory(request):
	subcategory_list = ItemSubCategory.objects.all()
	if request.method == 'GET':
		form = ItemSubCategoryForm()
		context = {
			'form':form,
			'subcategory_list':subcategory_list
		}
		return render(request,'subcategory.html',context)
	elif request.method == 'POST':
		form = ItemSubCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/subcategory/')
		context = {
			'form':form,
			'subcategory_list':subcategory_list
		}
		return render(request,'subcategory.html',context)

@login_required(login_url='/login/')
def category(request):
	category_list = ItemCategory.objects.all()
	if request.method == 'GET':
		form = ItemCategoryForm()
		context = {
			'form':form,
			'category_list':category_list
		}
		return render(request,'category.html',context)
	elif request.method == 'POST':
		form = ItemCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/category/')
		context = {
			'form':form,
			'category_list':category_list
		}
		return render(request,'category.html',context)

@login_required(login_url='/login/')
def index(request):
	# print(request.user)
	products_list = Product.objects.all()
	cart_objects = Cart.objects.filter(user=request.user.id,sold=False)
	context = {
		'user':request.user,
		'products_list':products_list,
		'count':cart_objects.count()
	}
	return render(request,'home.html',context)

@login_required(login_url='/login/')
def cart_checkout(request):
	cart_objects = Cart.objects.filter(user=request.user.id,sold=False)
	context = {
		'user':request.user,
		'items':cart_objects
	}
	return render(request,'cart.html',context)

def about(request):
	return render(request,'about.html')

@login_required(login_url='/login/')
def catalog(request):
	catalog_list = MyCatalog.objects.all()
	if request.method == 'GET':
		form = CatalogForm()
		context = {
			'form':form,
			'catalog_list':catalog_list,
			'user': request.user
		}
		return render(request,'my_catalog.html',context)
	elif request.method == 'POST':
		form = CatalogForm(request.POST,request.FILES)
		if form.is_valid():
			form_save = form.save(commit=False)
			form_save.img = form.cleaned_data['img']
			form_save.save()
			return HttpResponseRedirect('/catalog/')
		context = {
			'form':form,
			'catalog_list':catalog_list
		}
		return render(request,'my_catalog.html',context)

@login_required(login_url='/login/')
def update_catalog(request, pk):
	obj = MyCatalog.objects.get(pk=pk)
	if request.method == 'GET':
		form = CatalogForm(instance=obj)
		context = {
			'form':form
		}
		return render(request,'my_catalog.html',context)
	elif request.method == 'POST':
		form = CatalogForm(request.POST,request.FILES,instance=obj)
		if form.is_valid():
			form_save = form.save(commit=False)
			form_save.img = form.cleaned_data['img']
			form_save.save()
			return HttpResponseRedirect('/catalog/')
		context = {
			'form':form
		}
		return render(request,'my_catalog.html',context)

@login_required(login_url='/login/')
def delete_catalog(request, pk):
	obj = MyCatalog.objects.get(pk=pk)
	if request.method == 'GET':
		obj.delete()
		return HttpResponseRedirect('/catalog/')

@login_required(login_url='/login/')
def my_catalog(request):
	# print(request.user)
	catalog_list = MyCatalog.objects.all()
	# cart_objects = Cart.objects.filter(user=request.user.id,sold=False)
	context = {
		'user':request.user,
		'catalog_list':catalog_list,
		# 'count':cart_objects.count()
	}
	return render(request,'catalog.html',context)
