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
        <h3 class="h2">Como o NãoFu.me usa informações pessoais</h3>
        <p>As informações pessoais são aquelas capazes de identificar você de modo pessoal, tais como, nome, endereço, e-mail ou número de telefone, e que não estão disponíveis ao público.</p>
        <h3 class="h2">Compartilhamento e divulgação de informações</h3>
        <p>O NãoFu.me não aluga, não vende e não compartilha as informações pessoais com outras pessoas ou com empresas, exceto com objetivo de fornecer a você os produtos e serviços solicitados, tendo obtido para tanto a sua permissão.</p>
    </div>
{% endblock %}