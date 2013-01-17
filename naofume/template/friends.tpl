{% extends 'base.tpl' %}
{% block title %}{{ USER.name }} - Amigos | NãoFu.me{% endblock %}
{% block body_attr %}data-page="amigos" data-username="{{ USER.username }}" class="interna"{% endblock %}
{% block body %}
{% include 'nav_header.tpl' %}
{% include 'includes/header.tpl' %}
<div class="g960 page">
    <div class="perfil-lateral g300">
        {% include 'includes/user_card.tpl' %}
    </div>
    <div class="lista-amigos g610 sep">
        {% if USER.friends_privacy %}
            <h2 class="h2">Amigos parando de fumar</h2>
            {% for friend in USER.friends_privacy %}
                <a href="/{{ friend.username }}/">
                    <img src="{{ friend.picture_square }}" alt="" width="50" height="50"/>
                    <span>{{ friend.name }}</span>
                </a>
            {% endfor %}
        {% else %}
            <h3 class="h3">Você não possui amigos no naofu.me! Convide-os e troque incentivos para te ajudar a alcançar sua meta!</h3>
        {% endif %}
        <br clear="all">
        <div class="center">
            <button class="bt">Convide mais amigos</button>
        </div>
    </div>
</div>
{% endblock %}
