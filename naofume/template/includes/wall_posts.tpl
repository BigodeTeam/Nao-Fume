{% for post in WALL|slice:":10" %}
    <div class="post {% if post.type == '2' %}system{% else %}user{% endif %}" data-id="{{ post.id }}">
        <a href="/{{ post.user.username }}/">
            <img src="{{ post.user.picture_square }}" alt=""
                 width="50"
                 height="50"/>
        </a>
        <p class="post-cnt">
            {% if post.type == '2' %}
                <strong>{{ post.user.username }}</strong> {{ post.message|safe }}
            {% else %}
                <strong>{{ post.user.username }}</strong> {{ post.message }}
            {% endif %}
            {% if post.user == USER %}
                <a href="#" title="excluir mensagem" class="post-delete">-</a>
            {% endif %}
        </p>
    </div>
{% endfor %}

<a href="#" id="js-show-more" class="bt bt_more"
   {% if WALL.count < 11 %}style="display:none;"{% endif %}>mostrar mais</a>