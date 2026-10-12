from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Associação Comunitária Esperança</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f1f5f9;
                    color: #1e293b;
                    text-align: center;
                    padding: 60px 20px;
                }
                main {
                    max-width: 650px;
                    margin: auto;
                    background: white;
                    padding: 35px;
                    border-radius: 14px;
                }
                a {
                    display: inline-block;
                    background: #166534;
                    color: white;
                    padding: 12px 20px;
                    border-radius: 8px;
                    text-decoration: none;
                    margin-top: 15px;
                }
            </style>
        </head>
        <body>
            <main>
                <h1>Associação Comunitária Esperança</h1>
                <p>Bem-vindo ao sistema da Associação Comunitária Esperança.</p>
                <p>Um espaço para apoiar a organização das atividades comunitárias.</p>
                <a href="/admin/">Acessar administração</a>
            </main>
        </body>
        </html>
    """)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("admin/", admin.site.urls),
]