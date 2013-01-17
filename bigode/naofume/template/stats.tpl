{% extends 'base.tpl' %}

{% block title %}{{ USER.name }} | NãoFu.me{% endblock %}

{% block body_attr %}data-page="profile" data-username="{{ USER.username }}" class="interna"{% endblock %}

{% block body %}
    {% include 'nav_header.tpl' %}
    {% include 'includes/header.tpl' %}
    <div class="g960 page">
        <div class="perfil-lateral g300">
            {% include 'includes/user_card.tpl' with page="profile" %}
            {% include 'includes/user_friends.tpl' %}
        </div>

        <div class="stream g610 sep">
            <h2 class="h2">Economia em dinheiro e cigarros</h2>
                <div id="stats-chart" style="width: 570px;height: 250px"></div>
                <div class="legenda cigarro">
                    <strong></strong>
                    <span>cigarros a menos</span>
                </div>
                <div class="legenda dinheiro">
                    <strong></strong>
                    <span>reais economizados</span>
                </div>
                <div class="legenda media">
                    <strong></strong>
                    <span>reais por dia</span>
                </div>
                <div id="analisys center"></div>
        </div>
    </div>
    <script >
        google.load('visualization', '1', {packages: ['corechart']});
        google.setOnLoadCallback(function (){userStats.start('simples');});
    </script>

{% endblock %}
