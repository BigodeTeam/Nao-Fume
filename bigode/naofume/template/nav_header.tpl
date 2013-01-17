<nav class="main-nav" {% if IS_LOGGED  %}data-user-id="{{ LOGGED_USER.pk }}"{% endif %}>
    <ul class="g960">
    {% if IS_LOGGED  %}
        <li><a href="/">Home</a></li>
        {% if USER.friends_privacy %}
            <li><a href="/amigos/">Amigos</a></li>
        {% endif %}
        <li><a href="/{{ LOGGED_USER.username }}/">Perfil</a></li>
        <li><a href="/editar/">Editar</a></li>
        <li><a href="/logout/">Sair</a></li>
    {% else %}
        <li><a href="/login/">Entrar</a></li>
    {% endif %}
    </ul>
    <div class="fb-like" data-href="https://www.facebook.com/pages/N%C3%A3o-Fume/463064950391447" data-send="false" data-layout="button_count" data-width="450" data-show-faces="false"></div>
</nav>
