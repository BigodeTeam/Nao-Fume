{% if USER.friends_privacy %}
    <div class="perfil-amigos">
        <h3 class="h3">Amigos parando de fumar</h3>
        {% for friend in USER.friends_privacy|slice:":8" %}
            <a href="/{{ friend.username }}/" ><img src="{{ friend.picture_square }}" alt="{{ friend.name }}" title="{{ friend.name }}" width="50" height="50" /></a>
        {% endfor %}
    <br clear="all"/>
        <button class="bt">Convide mais amigos</button>
    </div>

{% else %}
    <div class="perfil-amigos">
        <button class="bt">Convide seus amigos</button>
    </div>
{% endif %}

