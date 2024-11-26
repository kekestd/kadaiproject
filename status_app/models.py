from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser


class CategoryAppend(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    
    CATEGORY =(('comic','漫画'),
               ('anime','アニメ'),
               ('game','ゲーム'),
               ('music','音楽'),
               ('sports','スポーツ'),
               ('sonota','その他'))
    # CustomUserモデル(のuser_id)とPhotoPostモデルを
    # 1対多の関係で結び付ける
    # CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE,
        related_name='categories'
        )
    category = models.CharField(
        verbose_name='趣味',# フィールドのタイトル
            max_length=20,
           choices=CATEGORY,
           
           )
    
    
    # イメージのフィールド2
    append_content1 = models.CharField(
        verbose_name='詳細',# フィールドのタイトル
        max_length=50,
        blank=True,            # フィールド値の設定は必須でない
        null=True 
    )
    append_image1 = models.ImageField(
        verbose_name='画像',# フィールドのタイトル
        upload_to = 'photos',
        blank=True,            # フィールド値の設定は必須でない
        null=True # MEDIA_ROOT以下のphotosにファイルを保存  
        )
    
    def __str__(self):
        return str(self.category)
class ContentAppend(models.Model):
    
    Category = models.ForeignKey(
        CategoryAppend,
        verbose_name='趣味',
        on_delete=models.CASCADE
    )
    
    append_content2 = models.CharField(
        verbose_name='追加詳細',# フィールドのタイトル
        max_length=50,
    )
    
class ImageAppend(models.Model):
    
    Category= models.ForeignKey(
        CategoryAppend,
        verbose_name='趣味',
        on_delete=models.CASCADE 
    )
    append_image2 = models.ImageField(
        verbose_name='追加画像',# フィールドのタイトル
        upload_to = 'photos',
        # MEDIA_ROOT以下のphotosにファイルを保存  
        )
    
        
    

    
    
