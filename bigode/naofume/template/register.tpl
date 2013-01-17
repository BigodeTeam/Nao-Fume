{% extends 'base.tpl' %}
{% block title %}NãoFu.me - Cadastro{% endblock %}
{% block body_attr %}data-page="register"{% endblock %}
{% block body %}

    {% include 'nav_header.tpl' %}

    {% include 'includes/header.tpl' %}

    <div class="g960 page">
        <div class="g455">
            {% if not EDIT %}
                <h1 class="h1">Crie sua meta</h1>
            {% else %}
                <h1 class="h1">Edite sua meta</h1>
            {% endif %}
            <form action="{% if not EDIT %}/registrar/{% else %}/editar/{% endif %}" method="POST" class="cadastro-form"> {% csrf_token %}

                <div>
                    Em quanto tempo pretende parar de fumar?

                    <input id="js-goal-number" value="{% if goal_date %}{{ goal_date }}{% endif %}" name="goal-num" class="input input-inline" type="number" />
                    <select name="goal-time" class="input input-inline">
                        <option {% if goal_time == 'day'%}selected="selected"{% endif %} value="day">dia(s)</option>
                        <option {% if goal_time == 'week'%}selected="selected"{% endif %} value="week">semana(s)</option>
                        <option {% if goal_time == 'month'%}selected="selected"{% endif %} value="month">mes(es)</option>
                        <option {% if goal_time == 'year'%}selected="selected"{% endif %} value="year">ano(s)</option>
                    </select>
                    <span class="erro" style="display:none;">Precisamos que você estabeleça uma meta :)</span>
                </div>

                <div>
                    Quantos cigarros você fuma por dia?
                    <input id="js-amount-number" value="{% if amount or amount == 0 %}{{ amount }}{% endif %}" type="number" name="amount" min="0" max="200" maxlength="3" class="input" />
                    <span class="erro" style="display:none;">Se você já parou de fumar digite 0, se não conseguiu ainda especifique um valor medio.</span>
                </div>

                <div>
                    Qual a marca de cigarro você fuma?
                    <select name="cigarette" class="input">
                    {% for cigar in CIGARETTE %}
                        <option  {% if cigarette_id == cigar.id %}selected="selected"{% endif %} value="{{ cigar.id }}">{{ cigar.name }}</option>
                    {% endfor %}
                    </select>
                </div>

                <div>
                    Visibilidade dos seus posts <br>
                    <label class="label-inline"><input {% if privacy == '1'%}checked="checked"{% endif %} name="privacy" value="1" type="radio"> somente eu</label>
                    <label class="label-inline"><input {% if privacy == '3'%}checked="checked"{% endif %} name="privacy" value="3" type="radio"> amigos</label>
                    <label class="label-inline"><input {% if privacy == '2' or not EDIT %}checked="checked"{% endif %} name="privacy" value="2" type="radio"> publico</label>
                </div>

                <input type="submit" value=" {% if not EDIT %}Criar meta!{% else %}Editar meta!{% endif %}" class="bt">
            </form>

        {% if EDIT %}
            <br/>
            <a href="/excluir/" onclick="return confirm('Tem certeza que quer apagar sua conta?')">
                Exclur perfil
            </a>
        {% endif %}
        </div>

        <div class="g455 sep">
            <section class="estao-parando">
                <h3 class="h3">Veja quem já está parando de fumar</h3>
                {% for user in USERS %}
                    <img src="{{user.picture_square}}" alt="{{ user.name }}" width="50" height="50">
                {% endfor %}
            </section>
            <section class="estatisticas">
                <h3 class="h3">O que o NãoFu.me já fez</h3>
                <span><b>{{ TOTAL_USERS }}</b> pessoas estão parando de fumar</span>
                <span><b>{{ TOTAL_STOP_USERS }}</b> {% if TOTAL_STOP_USERS != 1 %}pessoas já pararam{% else %}pessoa já parou{% endif %}</span>
                <span><b>{{ SAVINGS }}</b> reais economizados</span>
            </section>
        </div>
    </div>
{% endblock %}