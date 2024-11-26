# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス
        
        Attributes:
          model:連携するUserモデル
          fields:フォームで使用するフィールド
        '''
        # 連携するUserモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード、パスワード(確認用)
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['placeholder']=\
            'お名前を入力してください'
        
        self.fields['email'].widget.attrs['placeholder']=\
        'メールアドレスを入力してください'
        
        self.fields['password1'].widget.attrs['placeholder']=\
        'パスワードを入力してください'
        
        self.fields['password2'].widget.attrs['placeholder']=\
        '同じパスワードを入力してください'
        
        
        
    
        
      
        
        