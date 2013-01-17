{% extends 'base.tpl' %}
{% block title %}NãoFu.me{% endblock %}
{% block body_attr %}data-page="home" class="interna"{% endblock %}
{% block body %}
{% include 'nav_header.tpl' %}
{% include 'includes/header.tpl' %}
    <div class="g960 page">
        <div class="perfil-lateral g300">
            {% include 'includes/user_card.tpl' %}
            {% include 'includes/form_post_history.tpl' %}
            {% include 'includes/user_friends.tpl' %}
        </div>
        <div class="stream g610 sep">
            {% include 'includes/form_post_comment.tpl' %}
            {% include 'includes/wall_posts.tpl' %}
        </div>
    </div>
{% endblock %}
