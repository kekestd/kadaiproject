from django.forms import ModelForm

from .models import CategoryAppend

class CategoryForm(ModelForm):
    '''ModelFormのサブクラス'''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = CategoryAppend
        fields = ['category', 'append_content1', 'append_image1']
    
    