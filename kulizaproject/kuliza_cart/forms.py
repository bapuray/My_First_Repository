from kuliza_cart.models import Product, Cart, ItemCategory, ItemSubCategory, MyCatalog
from django import forms


class ProductForm(forms.ModelForm):
	name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	desc = forms.CharField(label='Product Description', widget=forms.Textarea(attrs={'class':'form-control'}))
	sub_category = forms.ModelChoiceField(label='Sub Category', queryset=ItemSubCategory.objects.all() ,widget=forms.Select(attrs={'class':'form-control'}))
	price = forms.CharField(label='Price', widget=forms.TextInput(attrs={'class':'form-control'}))
	img = forms.ImageField(label='Image', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['sub_category'].label_from_instance = self.label_from_instance

	def label_from_instance(self, obj):
		return obj.subcat_name + ' (' + obj.category.cat_name + ')'

	class Meta:
		model = Product
		fields = ['name', 'desc', 'sub_category','price']


class ItemCategoryForm(forms.ModelForm):
	cat_name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	cat_desc = forms.CharField(label='Category Description', widget=forms.Textarea(attrs={'class':'form-control'}))

	class Meta:
		model = ItemCategory
		fields = ['cat_name', 'cat_desc']


class ItemSubCategoryForm(forms.ModelForm):
	subcat_name = forms.CharField(label='Sub Category Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	subcat_desc = forms.CharField(label='Sub Category Description', widget=forms.Textarea(attrs={'class':'form-control'}))
	category = forms.ModelChoiceField(label='Category', queryset=ItemCategory.objects.all() ,widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = ItemSubCategory
		fields = ['subcat_name', 'subcat_desc', 'category']


class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CatalogForm(forms.ModelForm):
	"""docstring for CatalogForm"""
	name = forms.CharField(label='Item Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	desc = forms.CharField(label='Item Description', widget=forms.Textarea(attrs={'class':'form-control'}))
	sub_category = forms.ModelChoiceField(label='Sub Category', queryset=ItemSubCategory.objects.all() ,widget=forms.Select(attrs={'class':'form-control'}))
	price = forms.CharField(label='Price', widget=forms.TextInput(attrs={'class':'form-control'}))
	img = forms.ImageField(label='Image', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	def __init__(self, *args, **kwargs):
		super(CatalogForm, self).__init__(*args, **kwargs)
		self.fields['sub_category'].label_from_instance = self.label_from_instance

	def label_from_instance(self, obj):
		return obj.subcat_name + ' (' + obj.category.cat_name + ')'

	class Meta:
		model = MyCatalog
		fields = ['name', 'desc', 'sub_category','price']