{% extends 'base.tpl' %}
{% block title %}{{ POST.message|truncatewords:9 }} | NãoFu.me{% endblock %}
{% block body %}
    {% include 'nav_header.tpl' %}
    {% include 'includes/header.tpl' %}
    <div class="g455 page-post">
        <div class="post {% if POST.type == '2' %}system{% else %}user{% endif %}">
            <a href="/{{ POST.user.username }}/"><img src="{{ POST.user.picture }}" alt="" width="100" height="100"></a>
            <p class="post-cnt">
                <strong>{{ POST.user.username }}</strong>
                {{ POST.message }}
            </p>
        </div>
    </div>
{% endblock %}