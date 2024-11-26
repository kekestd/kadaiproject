from django.shortcuts import render, redirect
# django.views.generic.baseから　TemplateViewをインポート
from django.views.generic.base import TemplateView
#TemplateViewはすでに色々継承されているクラスでtemplatesの場所を読み込んでいる
from django.views.generic import ListView ,CreateView,DetailView


from django.urls import reverse_lazy

from accounts.models import CustomUser
from .models  import CategoryAppend
from .forms import CategoryForm


class MyIndexView(ListView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承
    
    Attributes:
        template_name レンダリングするテンプレート
        '''
    model = CategoryAppend
    
    #append_content1, append_image1, category, contentappend, id, imageappend, user, user_id
    #index.htmlをレンダリングする
    template_name = 'index.html'
    STATIC ='static/'
    
    
    def get_queryset(self):
    
        queryset = CategoryAppend.objects.filter(
        user=self.request.user)
        return queryset

class AccessView(CreateView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承
    
    Attributes:
        template_name レンダリングするテンプレート
        '''
    model = CategoryAppend
    form_class = CategoryForm
    #index.htmlをレンダリングする
    success_url = reverse_lazy('status_app:index')
    template_name = 'access.html'
    STATIC ='static/'  
    
    
    
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        data = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        data.user = self.request.user
        # 投稿データをデータベースに登録
        data.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
class CourseView(ListView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承
    
    Attributes:
        template_name レンダリングするテンプレート
        '''
    model = CustomUser
    
    #index.htmlをレンダリングする
    template_name = 'course.html'
    STATIC ='static/'

class UserView(ListView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承
    
    Attributes:
        template_name レンダリングするテンプレート
        '''
    #Gallery.htmlをレンダリングする
    template_name = 'index2.html'
    STATIC ='static/'
    def get_queryset(self):
    
            id=self.kwargs['user']
            user_list = CategoryAppend.objects.filter(
            
            user_id=id)
            return user_list


