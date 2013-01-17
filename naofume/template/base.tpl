{% load staticfiles %}<!DOCTYPE HTML>
<!-- 
#    FOCA NO CODIGO
#        .....
#       /o   o\
#    __(=  "  =)__
#     //\'-=-'/\\
#        )   (_
#       /      `#"=-._
#      /       \     ``"=.
#     /  /   \  \         `=..-.-.
# ___/  /     \  \___      _,  , #`\
#`....-' `""""`'....-``"""`  \  \_/
#                             `-`
 -->
<html lang="pt-BR" xmlns:og="http://ogp.me/ns#">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}NãoFu.me{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/css.css' %}?v=3">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
    <script type="text/javascript" src="//www.google.com/jsapi"></script>
    <script src="{% static 'js/js.js' %}?v=3" type="text/javascript"></script>
    <meta property="og:image" content="{% static 'img/logo-square.png' %}"/>
    <meta property="og:site_name" content="NãoFu.me"/>
    <meta property="fb:app_id" content="487995457879029"/>
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Não Fu.me - Um jeito simples de traçar sua meta para largar de vez o cigarro."/>
</head>
<body {% block body_attr %}{% endblock %}>
<div id="fb-root"></div>
{% block body %}
{% endblock %}
<footer class="footer">
    <div class="g960">
        <p>
            NãoFu.me - criado e desenvolvido por 
            <a href="https://github.com/CiceroComp">Cicero Verneck</a>, 
            <a href="https://github.com/diogocorrea">Diogo Corrêa</a>, 
            <a href="https://github.com/pantuza">Gustavo Pantuza</a>, 
            <a href="https://github.com/vitalbh">Victor Hugo</a>
        </p>
        <p>
            <a href="/sobre">sobre</a> &middot;
            <a href="/termos">termos</a> &middot;
            <a href="/midia-kit">media-kit</a>
        </p>
    </div>
</footer>
</body>
</html>
