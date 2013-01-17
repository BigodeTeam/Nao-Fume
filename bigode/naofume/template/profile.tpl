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
            <h2 class="h2">Progresso</h2>
            <div id="js-chart" style="width:570px;height:90px;margin-bottom:30px"></div>
            {% if IS_OWNER %}
                {% include 'includes/form_post_comment.tpl' %}
            {% endif %}
            {% include 'includes/wall_posts.tpl' %}
        </div>
    </div>
<script type="text/javascript">
google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(Chart.init);
</script>
{% endblock %}
