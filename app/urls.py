from app import views
from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'autor', views.AutorView, basename='autor')
router.register(r'user', views.UserView, basename='user')
router.register(r'article', views.ArticleView, basename='article')
router.register(r'article_by_tag', views.ArticleByTagView, basename='article_by_tag')
router.register(r'link_files', views.FilesView, basename='link_files')
router.register(r'file_by_article', views.FileByArticleView, basename='file_by_article')

urlpatterns = router.urls