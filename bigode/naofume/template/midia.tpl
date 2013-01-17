{% extends 'base.tpl' %}
{% block body_attr %}data-page="landing"{% endblock %}
{% block title %}Sobre - Não Fu.me - Um jeito simples de traçar sua meta para largar de vez o cigarro.{% endblock %}
{% block body %}
{% load staticfiles %}
{% include 'nav_header.tpl' %}

    <div class="g960 landing">

        <header>
            <div class="g555">
                <h1 class="logo"><a href="/">Não Fu.me</a></h1>
                <h2>Menos fumaça, <br> Mais saúde.</h2>
                <p>Um jeito simples de traçar sua meta para largar de vez o cigarro.</p>
            </div>
        </header>

        <h2 class="h2">Media Kit</h2>

        <p>Estamos coletando informações para construir nossos planos de parceria. Aguarde!</p>
        <p>Enquanto isso você pode entrar em contato por mensagem em nossa <a target="_blank" href="http://www.facebook.com/naofumeApp">página do facebook</a> .</p>

    </div>
{% endblock %}