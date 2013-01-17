{% extends 'base.tpl' %}
{% block body_attr %}data-page="landing"{% endblock %}
{% block title %}NãoFu.me - Um jeito simples de traçar sua meta para largar de vez o cigarro.{% endblock %}
{% block body %}
    {% load staticfiles %}
    {% include 'nav_header.tpl' %}
    <div class="g960 landing">
        <header>
            <div class="g455">
                <h1 class="logo"><a href="/">Não Fu.me</a></h1>
                <h2>Menos fumaça, <br> Mais saúde.</h2>
                <p>Um jeito simples de traçar sua meta para largar de vez o cigarro.</p>
                <a href="/login/" class="bt-conectar">Entre com o seu <span>Facebook</span></a>
            </div>
            <div class="g455" id="js-slider">
                <img src="/static/img/slide1.jpg" width="455" height="300" alt="">
            </div>
        </header>
        <section></section>
    </div>
{% endblock %}