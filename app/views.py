from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets, status


class AutorView(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    def retrieve(self, request, *args, **kwargs):
        serializer=self.get_serializer(self.queryset, many=True)
        dat=[]
        for j in serializer.data:
            g={
                'level': j['level'],
                'faculty': j['faculty'],
                'chair': j['chair'],
            }
            dat.append(g)
        return Response({'id_buyicha_dats':dat})

    def list(self, request, *args, **kwargs):
        serializer=self.get_serializer(self.queryset, many=True)
        autors=[]
        for i in serializer.data:
            names=Article.objects.filter(autor=i['id'])
            name=[]
            for n in names:
                nn={
                    'name':n.name
                }
                name.append(nn)

            d={
                'id':i['id'],
                'level':i['level'],
                'faculty':i['faculty'],
                'chair':i['chair'],
                'user':i['user'],
                'names': name
            }
            autors.append(d)
        return Response({'autors':autors})


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        datas=[]
        for i in serializer.data:
            files = LinkedFiles.objects.filter(article=i['id'])
            f=[]
            for file in files:
                ff={
                    'url':file.fileURL
                }
                f.append(ff)
            d={
                'id':i['id'],
                'name':i['name'],
                'text':i['text'],
                'tags':i['tags'],
                'autor':i['autor'],
                'files':f
            }
            datas.append(d)
        return Response({'datas':datas})

class ArticleByTagView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleByTagSerializer
    def retrieve(self, request, *args, **kwargs):
        tag=kwargs['pk']
        articles=self.queryset.filter(tags__contains=tag)
        datas=[]
        for art in articles:
            f={
                'id': art.id,
                'name': art.name,
                'text': art.id,
                'tags': art.tags,
                'autor': art.autor.id,
            }
            datas.append(f)
        return Response({'art':datas})

class FilesView(viewsets.ModelViewSet):
    queryset = LinkedFiles.objects.all()
    serializer_class = LinkedFilesSerializer

class FileByArticleView(viewsets.ModelViewSet):
    queryset = LinkedFiles.objects.all()
    serializer_class = FileByArticleSerializer
    def retrieve(self, request, *args, **kwargs):
        article_id=kwargs['pk']
        files=self.queryset.filter(article_id=article_id)
        serializer=self.get_serializer(files, many=True)
        return Response(serializer.data)
