<div class="perfil-topo">
    <a href="/{{ USER.username }}/"><img src="{{ USER.picture }}" alt="" width="100"></a>
    <h2 class="h2">{{ USER.name }}</h2>
    {% if USER.history.amount == 0 %}
        {% if USER.history.date_subs.STATUS == 0 %}
            <p>
                {% if page == "profile" %}
                    A meta foi cumprida, e {{ USER.name }} parou de fumar hoje! <b>De os parabéns !!</b>
                {% else %}
                    A meta foi cumprida, parabens !!! Compartilhe sua felicidade por ter vencido esse desafio!</b>
                {% endif %}
            </p>
        {% else %}
            {% if page == "profile" %}
                A meta foi cumprida, {{ USER.name }} parou de fumar em <b>{{ USER.history.date|date:"d/m/Y"}}</b>.
            {% else %}
                Você cumpriu sua meta e parou de fumar em <b>{{ USER.history.date|date:"d/m/Y" }}</b>.
            {% endif %}
            <p>
                Dias sem fumar:
                <b>
                    {% if USER.history.date_subsdate_subs.YEAR %}{{ USER.history.date_subs.YEAR }} ano{{ USER.history.date_subs.YEAR|pluralize }}{% endif %}
                    {% if USER.history.date_subs.MONTH %}{{ USER.history.date_subs.MONTH }} mes{{ USER.history.date_subs.MONTH|pluralize:"es" }}{% endif %}
                    {% if USER.history.date_subs.DAY %}{{ USER.history.date_subs.DAY }} dia{{ USER.history.date_subs.DAY|pluralize }}{% endif %}
                </b>
            </p>
        {% endif %}
    {% else %}
    <p>
        {% if page == "profile" %}
            Pretende parar de fumar em
        {% else %}
            Sua meta é parar de fumar em
        {% endif %}
        <b>
            {% if USER.m.YEAR %}{{ USER.m.YEAR }} ano{{ USER.m.YEAR|pluralize }}{% endif %}
            {% if USER.m.MONTH %}{{ USER.m.MONTH }} mes{{ USER.m.MONTH|pluralize:"es" }}{% endif %}
            {% if USER.m.DAY %}{{ USER.m.DAY }} dia{{ USER.m.DAY|pluralize }}{% endif %}
        </b>
    </p>
    <p>Fuma {{ USER.history.amount }} cigarro{{ USER.history.amount|pluralize }} por dia ({{ USER.history.cigarette.name }})</p>
    {% endif %}

    {% if IS_LOGGED  %}
        <p><a href="/{{ USER.username }}/estatistica/" >ver estatísticas</a></p>
    {% endif %}
</div>
